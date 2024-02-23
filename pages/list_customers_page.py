import allure

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ListCustomersPage(BasePage):
    FIRST_NAME_TITLE = ("xpath", "//a[contains(text(),'First Name')]")
    FIRST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[1])")
    DELETE_BTN_LIST = ("xpath", "(//button[@ng-click='deleteCust(cust)'])")

    @allure.step("Пользователи отсортированы по имени")
    def sort_by_first_name(self):
        column = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_TITLE))
        column.click()
        column.click()

    @allure.step("Пользователь/и удален/ы")
    def delete_specific_customers(self):
        names_elements = self.wait.until(
            EC.presence_of_all_elements_located(self.FIRST_NAMES_LIST),
            "Don't find name elements"
        )

        names_list = [i.text for i in names_elements]
        lengths_names_list = list(map(len, names_list))
        avg_value = sum(lengths_names_list) / len(lengths_names_list)
        min_deviation_value = min(list(map(lambda x: abs(x - avg_value), lengths_names_list)))

        delete_btn_elements = []
        for i in range(1, len(names_elements) + 1):
            deviation_value = abs(len(names_list[i - 1]) - avg_value)

            if deviation_value == min_deviation_value:
                delete_btn_element_locator = ("xpath", f"{self.DELETE_BTN_LIST[1]}[{i}]")
                delete_btn_element = self.wait.until(
                    EC.element_to_be_clickable(delete_btn_element_locator),
                    "Don't find button element"
                )
                delete_btn_elements.append(delete_btn_element)

        for i in delete_btn_elements:
            i.click()
