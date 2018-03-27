from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Aladdin.Accounting.decorators.ParamsTestCase import ParamsTestCase
from Aladdin.Accounting.decorators.StoreTestResult import add_res_to_DB
from Prozorro.Pages.LoginPage import LoginPage
from Prozorro.Utils import waitFadeIn


class Qualification(ParamsTestCase):
    @add_res_to_DB(test_name='Авторизация заказчика')
    def login_owner(self):
        self.wts.drv.get(self.parent_suite.suite_params["login_url"])
        if "new_owner_login" in self.parent_suite.suite_params:
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["new_owner_login"],
                    self.parent_suite.suite_params["new_owner_password"]
                )
        else:
            with self.subTest("авторизация"):
                LoginPage(self.wts.drv).login(
                    self.parent_suite.suite_params["tender_json"]["below"]["login"],
                    self.parent_suite.suite_params["tender_json"]["below"]["password"]
                )

        myTendersList = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "myTendersList")))
        myTenders = WebDriverWait(self.wts.drv, 10).until(
            expected_conditions.visibility_of_element_located((By.ID, "myTenders")))

        if (myTendersList.get_attribute("aria-expanded") == "true"
            or self.wts.drv.find_element_by_xpath("//div[@id='myTenders']/div"). \
                    get_attribute("class") == "filter-title"
            ):
            waitFadeIn(self.drv)
            myTenders.click()

        self.log("login_owner OK - " + self.parent_suite.suite_params["tender_json"]["below"]["login"] +
                 " - url: " + self.wts.drv.current_url)

    @add_res_to_DB(test_name='Ожидание статуса')
    def wait_for_status(self):
        # 5 - Кваліфікація
        if "wait_status" in self.parent_suite.suite_params:
            wst = self.parent_suite.suite_params["wait_status"]
            url = self.wts.drv.current_url
            for m in range(1, 100 ):
                status =self.wts.drv.execute_script("return $('#purchaseStatus').text()")
                if status !=wst :
                    sleep(5)
                    self.wts.drv.get(url)
                else:
                    break

    @add_res_to_DB(test_name='Вкладки квалификации')
    def q_tabs(self):
        with("results-award-tab"):
            results_award_tab = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "results-award-tab")))
            self.assertEqual(results_award_tab, "ПРОТОКОЛ РОЗКРИТТЯ")
            self.log("Вкладка ПРОТОКОЛ РОЗКРИТТЯ ОК")

        with("results-bids-tab"):
            results_bids_tab = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "results-bids-tab")))
            self.assertEqual(results_bids_tab, "ПРОПОЗИЦІЇ")
            self.log("Вкладка ПРОПОЗИЦІЇ ОК")

        with("processing-tab"):
            processing_tab = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.ID, "processing-tab")))
            self.assertEqual(processing_tab, "ОБРОБКА")
            self.log("Вкладка ОБРОБКА ОК")

    @add_res_to_DB(test_name='Вкладка 1 кандидат ПРОТОКОЛ РОЗКРИТТЯ')
    def q_tab_result_award_1(self):
        with("results-award"):
            parti = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='results-award']//table")))

            partiS = WebDriverWait(self.wts.drv, 10).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='results-award']//table/tbody/tr/td[3]")))

            bid_sum = self.params["bid_json"]["bidAmount"]
            sum, = partiS.partition(" ")

            self.assertEqual(sum, bid_sum)

    #results-bids-tab    ПРОПОЗИЦІЇ
        # //div[@id='results-bids']//table
        # //div[@id='results-bids']//table/tbody/tr) == 2
    #processing-tab      ОБРОБКА
