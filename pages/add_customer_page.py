import allure

from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    FIRST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//form[@name='myForm']//button[@type='submit']")

    @allure.step("Ввести имя")
    def enter_first_name(self, first_name):
        self.wait_element_to_be_clickable(self.FIRST_NAME_FIELD).send_keys(first_name)

    @allure.step("Ввести фамилию")
    def enter_last_name(self, last_name):
        self.wait_element_to_be_clickable(self.LAST_NAME_FIELD).send_keys(last_name)

    @allure.step("Ввести почтовый код")
    def enter_post_code(self, post_code):
        self.wait_element_to_be_clickable(self.POST_CODE_FIELD).send_keys(post_code)

    @allure.step("Нажать кнопку 'Add Customer'")
    def click_add_customer_submit_btn(self):
        self.wait_element_to_be_clickable(self.ADD_CUSTOMER_SUBMIT_BTN).click()

    @allure.step("Проверка сообщения об успешном создании клиента")
    def get_alert_message(self):
        self.wait_alert_is_present()
        return self.driver.switch_to.alert.text[:-1]

    @allure.step("Нажать кнопку 'OK'")
    def click_alert(self):
        self.wait_alert_is_present()
        self.driver.switch_to.alert.accept()
