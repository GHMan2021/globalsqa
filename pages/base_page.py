import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import WAIT_TIMEOUT


class BasePage:
    PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    BTN_MENU_LIST = ("xpath", "(//div[@class='center']//button)")
    FIRST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[1])")
    LAST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[2])")
    POST_CODE_LIST = ("xpath", "(//tr[@class='ng-scope']//td[3])")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    def open(self):
        with allure.step(f"Открытие страницы {self.PAGE_URL}"):
            self.driver.get(self.PAGE_URL)

    def click_on_item_menu(self, item_title):
        with allure.step(f"Нажать на пункт меню '{item_title}'"):
            btn_menu_elements = self.wait.until(
                EC.visibility_of_all_elements_located(self.BTN_MENU_LIST)
            )
            for i in btn_menu_elements:
                if i.text == item_title:
                    i.click()
                    break

    def get_all_customers_list(self):
        self.click_on_item_menu('Customers')

        first_name_elements = self.wait.until(EC.presence_of_all_elements_located(self.FIRST_NAMES_LIST))
        count_of_records = len(first_name_elements)

        all_customers_list = []
        for i in range(1, count_of_records + 1):
            first_name_element_locator = ("xpath", f"{self.FIRST_NAMES_LIST[1]}[{i}]")
            last_name_element_locator = ("xpath", f"{self.LAST_NAMES_LIST[1]}[{i}]")
            post_code_element_locator = ("xpath", f"{self.POST_CODE_LIST[1]}[{i}]")

            first_name_element = self.wait.until(EC.presence_of_element_located(first_name_element_locator))
            last_name_element = self.wait.until(EC.presence_of_element_located(last_name_element_locator))
            post_code_element = self.wait.until(EC.presence_of_element_located(post_code_element_locator))

            record = (first_name_element.text, last_name_element.text, post_code_element.text)
            all_customers_list.append(record)

        return all_customers_list

