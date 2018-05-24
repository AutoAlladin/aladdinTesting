import datetime
import os
import socket

import prozorro


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]


def create_result_DB(init_params_test):
    def wrapper(bro):
        pts = init_params_test(bro)
        """Создане в БД пустого документа с результатом теста """
        if 'test_name' not in pts:
            raise Exception("Не указано имя теста для сохранеия результата в БД")

        pts['wts'].result_id = pts["wts"].__mongo__.create_result()
        res=pts['wts'].__mongo__.test_result.find_one({"_id": pts["wts"].result_id})

        res["test_name"]= pts['test_name']
        res["test_timestamp"]=datetime.datetime.utcnow()  #.strftime("%Y-%m-%d %H:%M:%S.%f%z")
        res["run_info"]["user"] =os.path.split(os.path.expanduser('~'))[-1]
        res["run_info"]["ip"]=get_ip_address()

        pts['wts'].__mongo__.test_result.save(res)

        print("init res, ID=", pts['wts'].result_id)
        return pts
    return wrapper


def add_res_to_DB(test_name=None,
                  test_description=None,
                  screenshotOK=True,
                  screenshotERROR=True,
                  parent=None):
    def inner_decorator(test_method):
        def wrapper(self):

            tt = None
            if test_name is None:
                tt = test_method.__name__
            else:
                tt=test_name

            test_method_result = {
                "name": tt,
                "status": "STARTED",
                "timing": {"end": None,
                           "start": None,
                           "duration": 0}
            }

            if test_description is not None: test_method_result.update({"description": test_description})

            start_test_method = datetime.datetime.utcnow()
            test_method_result["timing"]["start"]=start_test_method  #.strftime("%Y-%m-%d %H:%M:%S.%f%z")

            try:
                if parent is None:
                    self.tlog.clear()
                    self.wts.__mongo__.test_result.update({"_id": self.wts.result_id},
                                                          {"$push": {"results": test_method_result}})
                # else: 0639552988
                #     self.wts.__mongo__.test_result.update({"_id": self.wts.result_id, "results.name": parent },
                #                                           {"$push": {"results.$.sub": test_method_result}})

                test_method(self)

                test_method_result["status"]="PASSED"
                if screenshotOK and self.wts.drv is not None :
                    pngOK=self.wts.drv.get_screenshot_as_png()
                    test_method_result.update({"screen_id": self.wts.__mongo__.fs.put(pngOK, file_name=test_method.__name__+"OK.png")})

            except Exception as e:
                test_method_result["status"] = "ERROR"
                test_method_result.update({"exception_msg": e.__str__()})
                if screenshotERROR and self.wts.drv is not None:
                    pngERROR = self.wts.drv.get_screenshot_as_png()
                    test_method_result.update({"screen_id": self.wts.__mongo__.fs.put(pngERROR, file_name=test_method.__name__+"ERROR.png")})

                raise Exception(tt,
                                os.path.dirname(os.path.abspath( prozorro.__file__ ))+"\\Aladdin\\output\\"+test_method.__name__+"ERROR.png"     )
            finally:
                if test_method_result["status"]=="":
                    test_method_result["status"] = "NOT RUNED"
                final_test_method = datetime.datetime.now()
                test_method_result["timing"]["end"]= final_test_method #  .strftime("%Y-%m-%d %H:%M:%S.%f%z")
                test_method_result["timing"]["duration"]= (final_test_method-start_test_method).total_seconds()

                if len(self.tlog)>0 :
                    test_method_result.update({"logs":self.tlog});

                if self.wts.drv is not None \
                and "screen_id" in test_method_result \
                and test_method_result["screen_id"] != "":
                    dir= os.path.dirname(os.path.abspath( prozorro.__file__ ))+"\\Aladdin\\output\\"
                    self.wts.drv.get_screenshot_as_file(dir + test_method.__name__+"_"+str(test_method_result["screen_id"]) + ".png")

                if parent is None:
                    tmp_result = self.wts.__mongo__.test_result.find_one({"_id": self.wts.result_id})["results"]
                    tmp = list(filter(lambda x: x["name"] == tt, tmp_result))
                    if "sub" in tmp[0]:
                        test_method_result.update(tmp[0])
                    self.wts.__mongo__.test_result.update(
                        {"_id": self.wts.result_id,"results.name": test_method_result["name"]},
                        {"$set": {"results.$": test_method_result}})
                else:
                    self.wts.__mongo__.test_result.update({"_id": self.wts.result_id, "results.name": parent},
                                                          {"$push": {"results.$.sub": test_method_result}})
                # else:
                #     self.wts.__mongo__.test_result.update(
                #         {"_id": self.wts.result_id,
                #          "results.name": parent,
                #          "results.sub.name": test_method_result["name"]},
                #         {"$set": {"results.$.sub.$": test_method_result}})

            return test_method_result
        return wrapper
    return inner_decorator

def return_for_DB(test_name=None,
                  test_description=None,
                  screenshotOK=True,
                  screenshotERROR=True,):
    def inner_decorator(test_method):
        def wrapper(self):

            tt = None
            if test_name is None:
                tt = test_method.__name__
            else:
                tt=test_name

            test_method_result = {
                "name": tt,
                "status": "STARTED",
                "timing": {"end": None,
                           "start": None,
                           "duration": 0}
            }

            if test_description is not None: test_method_result.update({"description": test_description})

            start_test_method = datetime.datetime.now()
            test_method_result["timing"]["start"]=start_test_method #.strftime("%Y-%m-%d %H:%M:%S.%f%z")

            try:
                test_method(self)

                test_method_result["status"]="PASSED"
                if screenshotOK:
                    pngOK=self.wts.drv.get_screenshot_as_png()
                    test_method_result.update({"screen_id": pngOK})

            except Exception as e:
                test_method_result["status"] = "ERROR"
                test_method_result.update({"exception_msg": e.__str__()})
                if screenshotERROR:
                    pngERROR = self.wts.drv.get_screenshot_as_png()
                    test_method_result.update({"screen_id":pngERROR})
                e.test_method=tt
                raise  Exception(tt,
                                os.path.dirname(os.path.abspath( prozorro.__file__ ))+"\\Aladdin\\output\\",

                       )
            finally:
                if "status" in test_method_result:
                    test_method_result["status"] = "NOT RUNED"
                final_test_method = datetime.datetime.utcnow()
                test_method_result["timing"]["end"]= final_test_method  #.strftime("%Y-%m-%d %H:%M:%S.%f%z")
                test_method_result["timing"]["duration"]= (final_test_method-start_test_method).total_seconds()

                if len(self.tlog)>0 :
                    test_method_result.update({"logs":self.tlog});

                if test_method_result["screen_id"] != "":
                    dir=os.path.dirname(os.path.abspath( prozorro.__file__ ))
                    dir+="\\Aladdin\\output\\"
                    self.wts.drv.get_screenshot_as_file(dir + test_method.__name__+"_"+str(test_method_result["screen_id"]) + ".png")

                if parent is None:
                    tmp_result = self.wts.__mongo__.test_result.find_one({"_id": self.wts.result_id})["results"]
                    tmp = list(filter(lambda x: x["name"] == tt, tmp_result))
                    if "sub" in tmp[0]:
                        test_method_result.update(tmp[0])
                    self.wts.__mongo__.test_result.update(
                        {"_id": self.wts.result_id,"results.name": test_method_result["name"]},
                        {"$set": {"results.$": test_method_result}})
                else:
                    self.wts.__mongo__.test_result.update({"_id": self.wts.result_id, "results.name": parent},
                                                          {"$push": {"results.$.sub": test_method_result}})
                # else:
                #     self.wts.__mongo__.test_result.update(
                #         {"_id": self.wts.result_id,
                #          "results.name": parent,
                #          "results.sub.name": test_method_result["name"]},
                #         {"$set": {"results.$.sub.$": test_method_result}})

            return test_method_result
        return wrapper
    return inner_decorator