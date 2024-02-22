import time

from pages.add_customer_page import AddCustomerPage
from pages.base_page import BasePage
from pages.list_customers_page import ListCustomersPage
from data.data import Customer


def test_create_customer_and_delete_specific_customer(
        driver,
        first_name=Customer.first_name,
        last_name=Customer.last_name,
        post_code=Customer.post_code
):
    manager_page = BasePage(driver)
    manager_page.PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    manager_page.open()
    manager_page.is_open()
    manager_page.click_on_item_menu("Add Customer")

    add_customer_page = AddCustomerPage(driver)
    add_customer_page.enter_first_name(first_name)
    add_customer_page.enter_last_name(last_name)
    add_customer_page.enter_post_code(post_code)
    add_customer_page.click_add_customer_submit_btn()
    add_customer_page.accept_alert()
    add_customer_page.click_on_item_menu("Customers")

    list_customers_page = ListCustomersPage(driver)
    list_customers_page.sort_by_first_name()
    list_customers_page.delete_specific_customers()
    time.sleep(5)
