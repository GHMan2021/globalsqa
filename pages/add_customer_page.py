from pages.base_page import BasePage


class AddCustomerPage(BasePage):
    FIRST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='fName']")
    LAST_NAME_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='lName']")
    POST_CODE_FIELD = ("xpath", "//form[@name='myForm']//input[@ng-model='postCd']")
    ADD_CUSTOMER_SUBMIT_BTN = ("xpath", "//form[@name='myForm']//button[@type='submit']")

    def enter_first_name(self, first_name: str) -> None:
        self.element_to_be_clickable(self.FIRST_NAME_FIELD).send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        self.element_to_be_clickable(self.LAST_NAME_FIELD).send_keys(last_name)

    def enter_post_code(self, post_code: str) -> None:
        self.element_to_be_clickable(self.POST_CODE_FIELD).send_keys(post_code)

    def click_add_customer_submit_btn(self) -> None:
        self.element_to_be_clickable(self.ADD_CUSTOMER_SUBMIT_BTN).click()

    def get_alert_message(self) -> str:
        self.alert_is_present()
        return self.driver.switch_to.alert.text[:-1]

    def click_alert(self) -> None:
        self.alert_is_present()
        self.driver.switch_to.alert.accept()
