import allure
import pytest

from pages.add_customer_page import AddCustomerPage
from pages.base_page import BasePage
from pages.list_customers_page import ListCustomersPage
from data.data import Customer


@allure.feature('globalsqa.com')
@allure.story('UI')
@allure.title('Создание пользователя и удаление пользователя/ей')
@allure.description("""
    Цель: Проверить создание пользователя и удаление пользователя/ей по специальному критерию
    
    Предусловие: Открыть браузер
    
    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    2. Проверить правильность открытой страницы
    3. Нажать на пункт меню "Add Customer"
    4. Ввести данные в поля "Last Name", "Post Code", в поле "First Name" значение сформировать на данных "Post Code" 
    5. Нажать на кнопку создания пользователя "Add Customer"
    6. Нажать на кнопку "ОК" во всплывающем окне подтверждения создания нового пользователя
    7. Нажать на пункт меню "Customers"    
    8. Дважды нажать на заголовок таблицы "First Name" для сортировки пользователей по именам 
    10. Нажать кнопу "Delete" у тех записей, имена которых соответствует специальному критерию""")
@pytest.mark.parametrize(
    'first_name, last_name, post_code',
    [(Customer.first_name, Customer.last_name, Customer.post_code)]
)
def test_create_customer_and_delete_specific_customer(driver, first_name, last_name, post_code):
    with allure.step("Открытие страницы 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        manager_page = BasePage(driver)
        manager_page.PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
        manager_page.open()

    with allure.step("Проверка правильности адреса открытой страницы"):
        manager_page.is_open()

    with allure.step("Создание нового пользователя"):
        manager_page.click_on_item_menu("Add Customer")
        add_customer_page = AddCustomerPage(driver)
        add_customer_page.enter_first_name(first_name)
        add_customer_page.enter_last_name(last_name)
        add_customer_page.enter_post_code(post_code)
        add_customer_page.click_add_customer_submit_btn()
        add_customer_page.accept_alert()
        add_customer_page.click_on_item_menu("Customers")

    with allure.step("Сортировать пользователей по имени"):
        list_customers_page = ListCustomersPage(driver)
        list_customers_page.sort_by_first_name()

    with allure.step("Удаление пользователя/ей согласно заданному критерию"):
        list_customers_page.delete_specific_customers()
