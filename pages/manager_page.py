import allure

from pages.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class ManagerPage(BasePage):
    PAGE_URL = Links.HOST

    ADD_CUSTOMER_BUTTON = ("xpath", "//div[@class='center']//button[@ng-class='btnClass1']")

    @allure.step("Click on 'Add Customer' button")
    def click_add_customer_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_CUSTOMER_BUTTON)).click()
