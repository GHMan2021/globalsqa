import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    PAGE_URL = None

    BTN_MENU_LIST = ("xpath", "(//div[@class='center']//button)")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10, poll_frequency=1)

    def open(self):
        with allure.step(f"Открыть {self.PAGE_URL} адрес"):
            self.driver.get(self.PAGE_URL)

    def is_open(self):
        with allure.step(f"Страница {self.PAGE_URL} открыта"):
            self.wait.until(EC.url_to_be(self.PAGE_URL))

    def click_on_item_menu(self, item_title):
        with allure.step(f"Нажать на пункт меню '{item_title}'"):
            btn_menu_elements = self.wait.until(
                EC.visibility_of_all_elements_located(self.BTN_MENU_LIST)
            )
            for i in btn_menu_elements:
                if i.text == item_title:
                    i.click()
                    break
