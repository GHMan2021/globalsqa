import time

from pages.add_customer_page import AddCustomerPage
from pages.list_customers_page import ListCustomersPage
from pages.manager_page import ManagerPage
from data.data import Customer


def test_create_customer_and_delete_specific_customer(
        driver,
        first_name=Customer.first_name,
        last_name=Customer.last_name,
        post_code=Customer.post_code
):
    manager_page = ManagerPage(driver)
    manager_page.open()

    manager_page.click_add_customer_btn()
    add_customer_page = AddCustomerPage(driver)
    add_customer_page.enter_first_name(first_name)
    add_customer_page.enter_last_name(last_name)
    add_customer_page.enter_post_code(post_code)
    add_customer_page.click_add_customer_submit_btn()
    add_customer_page.accept_alert()

    list_customers_page = ListCustomersPage(driver)
    list_customers_page.open()
    list_customers_page.sort_by_first_name()
    list_customers_page.delete_specific_customers()
    time.sleep(3)
