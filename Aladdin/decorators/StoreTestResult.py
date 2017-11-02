import os
import socket

import Aladdin.AladdinUtils
import datetime
from datetime import  timedelta

import prozorro


def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

def create_result_DB(test_method):
    def wraper(self):
        #wts = Aladdin.AladdinUtils.WebTestSession( test_method(self))
        wts = test_method(self)
        """Создане в БД пустого документа с результатом теста """
        if wts.test_name is None:
            raise Exception("Не указано имя теста для сохранеия результата в БД")

        wts.result_id = wts.__mongo__.create_result()
        res=wts.__mongo__.test_result.find_one({"_id": wts.result_id})

        res["test_name"]= wts.test_name
        res["test_timestamp"]=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f%z")
        res["run_info"]["user"] =os.path.split(os.path.expanduser('~'))[-1]
        res["run_info"]["ip"]=get_ip_address()

        wts.__mongo__.test_result.save(res)

        print("init res, ID=", wts.result_id)
    return wraper

def add_res_to_DB(test_method,screenshotOK=False,screenshotERROR=True):
    def wraper(self):
        test_method_result={
            "name" : "",
            "status" : "",
            "screen_id":"",
            "duration" : 0,
            "exception_msg" : "",
            "logs" : {}
        }

        test_method_result["name"]=test_method.__name__
        start_test_method = datetime.datetime.now()
        try:
            self.tlog.clear()
            test_method(self)
            test_method_result["status"]="OK"
            if screenshotOK:
                pngOK=self.wts.drv.get_screenshot_as_png()
                test_method_result["screen_id"]=self.wts.__mongo__.fs.put(pngOK)

        except Exception as e:
            test_method_result["status"] = "ERROR"
            test_method_result["exception_msg"] =e.__str__()
            if screenshotERROR:
                pngERROR = self.wts.drv.get_screenshot_as_png()
                test_method_result["screen_id"] = self.wts.__mongo__.fs.put(pngERROR)
            raise e
        finally:
            final_test_method = datetime.datetime.now()
            test_method_result["duration"]= (final_test_method-start_test_method).total_seconds()
            test_method_result["logs"] = self.tlog

            if test_method_result["screen_id"] != "":
                dir=os.path.dirname(os.path.abspath( prozorro.__file__ ))
                dir+="\\Aladdin\\output\\"
                self.wts.drv.get_screenshot_as_file(dir + test_method.__name__+"_"+str(test_method_result["screen_id"]) + ".png")

            self.wts.__mongo__.test_result.find_one_and_update({"_id": self.wts.result_id},
                                                               {"$push": {"results": test_method_result}})


    return wraper