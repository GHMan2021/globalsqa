from pages.base_page import BasePage


class ManagerPage(BasePage):
    BTN_MENU_LIST = ("xpath", "(//div[@class='center']//button)")

    def click_on_item_menu(self, item_title: str) -> None:
        btn_menu_elements = self.presence_of_all_elements_located(self.BTN_MENU_LIST)
        for i in btn_menu_elements:
            if i.text == item_title:
                i.click()
                break
