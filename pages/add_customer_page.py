import allure

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class AddCustomerPage(BasePage):
    FIRST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//form[@name='myForm']//button[@type='submit']")

    @allure.step("Ввести имя")
    def enter_first_name(self, login):
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_FIELD)).send_keys(login)

    @allure.step("Ввести фамилию")
    def enter_last_name(self, password):
        self.wait.until(EC.element_to_be_clickable(self.LAST_NAME_FIELD)).send_keys(password)

    @allure.step("Ввести почтовый код")
    def enter_post_code(self, post_code):
        self.wait.until(EC.element_to_be_clickable(self.POST_CODE_FIELD)).send_keys(post_code)

    @allure.step("Нажать кнопку 'Add Customer'")
    def click_add_customer_submit_btn(self):
        self.wait.until(EC.element_to_be_clickable(self.ADD_CUSTOMER_SUBMIT_BTN)).click()

    @allure.step("Подтвердить нажатием 'OK' во всплывающем окне")
    def accept_alert(self):
        self.wait.until((EC.alert_is_present()))
        alert = self.driver.switch_to.alert
        alert.accept()
