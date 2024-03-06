from pages.base_page import BasePage


class ListCustomersPage(BasePage):
    TABLE_DATA_ROWS_LIST = ("xpath", "(//table//tbody//tr)")
    FIRST_NAME_TITLE = ("xpath", "//a[contains(text(),'First Name')]")

    FIRST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[1])")
    LAST_NAMES_LIST = ("xpath", "(//tr[@class='ng-scope']//td[2])")
    POST_CODE_LIST = ("xpath", "(//tr[@class='ng-scope']//td[3])")
    DELETE_BTN_LIST = ("xpath", "(//button[@ng-click='deleteCust(cust)'])")

    def sort_by_first_name(self):
        column = self.element_to_be_clickable(self.FIRST_NAME_TITLE)
        column.click()
        column.click()

    def delete_customers(self):
        delete_records_element_list = self.get_delete_records_element_list()
        for elem in delete_records_element_list:
            elem[3].click()

    def get_all_records_elements_list(self):
        count_data_row = len(self.presence_of_all_elements_located(self.TABLE_DATA_ROWS_LIST))

        all_records_elements_list = []
        for i in range(1, count_data_row + 1):
            first_name_element_locator = ("xpath", f"{self.FIRST_NAMES_LIST[1]}[{i}]")
            last_name_element_locator = ("xpath", f"{self.LAST_NAMES_LIST[1]}[{i}]")
            post_code_element_locator = ("xpath", f"{self.POST_CODE_LIST[1]}[{i}]")
            delete_btn_element_locator = ("xpath", f"{self.DELETE_BTN_LIST[1]}[{i}]")

            record = tuple(self.presence_of_element_located(i) for i in [
                first_name_element_locator,
                last_name_element_locator,
                post_code_element_locator,
                delete_btn_element_locator
            ])
            all_records_elements_list.append(record)

        return all_records_elements_list

    def get_delete_records_element_list(self):
        all_records_element_list = self.get_all_records_elements_list()
        lengths_names_list = [len(elem[0].text) for elem in all_records_element_list]
        comparison_value = self.value_with_min_deviation_from_avg(lengths_names_list)

        delete_records_element_list = [
            elem for elem in all_records_element_list if len(elem[0].text) == comparison_value
        ]

        return delete_records_element_list

    def get_all_data_customers(self):
        all_records_element_list = self.get_all_records_elements_list()
        all_data_element_list = [i[:-1] for i in all_records_element_list]
        all_data_customers = [tuple(i.text for i in elem) for elem in all_data_element_list]
        return all_data_customers

    @staticmethod
    def value_with_min_deviation_from_avg(number_list):
        avg_value = sum(number_list) / len(number_list)
        min_deviation_value = min(list(map(lambda x: abs(x - avg_value), number_list)))

        for item in number_list:
            if abs(item - avg_value) == min_deviation_value:
                return item
