import allure

from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class ListCustomersPage(BasePage):
    FIRST_NAME_TITLE = ("xpath", "//a[contains(text(),'First Name')]")
    DELETE_BTN_LIST = ("xpath", "(//button[@ng-click='deleteCust(cust)'])")

    @allure.step("Сортировать пользователей по имени")
    def sort_by_first_name(self):
        column = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME_TITLE))
        column.click()
        column.click()

    @allure.step("Удалить клиентов")
    def delete_customers(self):
        names_elements = self.wait.until(EC.presence_of_all_elements_located(self.FIRST_NAMES_LIST))

        names_list = [i.text for i in names_elements]
        lengths_names_list = list(map(len, names_list))
        avg_value = sum(lengths_names_list) / len(lengths_names_list)
        min_deviation_value = min(list(map(lambda x: abs(float(x) - avg_value), lengths_names_list)))

        delete_btn_elements = []
        delete_records_list = []
        for i in range(1, len(names_elements) + 1):
            deviation_value = abs(len(names_list[i - 1]) - avg_value)

            if deviation_value == min_deviation_value:
                delete_btn_element_locator = ("xpath", f"{self.DELETE_BTN_LIST[1]}[{i}]")
                first_name_element_locator = ("xpath", f"{self.FIRST_NAMES_LIST[1]}[{i}]")
                last_name_element_locator = ("xpath", f"{self.LAST_NAMES_LIST[1]}[{i}]")
                post_code_element_locator = ("xpath", f"{self.POST_CODE_LIST[1]}[{i}]")

                delete_btn_element = self.wait.until(EC.element_to_be_clickable(delete_btn_element_locator))
                first_name_element = self.wait.until(EC.presence_of_element_located(first_name_element_locator))
                last_name_element = self.wait.until(EC.presence_of_element_located(last_name_element_locator))
                post_code_element = self.wait.until(EC.presence_of_element_located(post_code_element_locator))

                delete_btn_elements.append(delete_btn_element)

                record = (first_name_element.text, last_name_element.text, post_code_element.text)
                delete_records_list.append(record)

        for i in delete_btn_elements:
            i.click()

        return delete_records_list
