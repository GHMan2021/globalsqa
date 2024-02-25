import allure
import pytest

from pages.add_customer_page import AddCustomerPage
from data.data import Customer


@allure.feature('globalsqa.com')
@allure.title('Создание клиента (Add Customer)')
@allure.description("""
    Цель: Проверить создание клиента

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"    
    2. Нажать на пункт меню "Add Customer"
    3. Ввести данные в поля "Last Name", "Post Code", "First Name"
    4. Нажать на кнопку создания клиента "Add Customer"
    5. Проверить, что появилось сообщение об успешной регистрации
    6. Проверить, что клиент был добавлен
    """)
@pytest.mark.parametrize(
    'first_name, last_name, post_code',
    [(Customer.first_name, Customer.last_name, Customer.post_code)]
)
def test_create_customer(driver, first_name, last_name, post_code):
    with allure.step("Открыть страницу 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        add_customer_page = AddCustomerPage(driver)
        add_customer_page.open()

    with allure.step("Создать нового клиента"):
        add_customer_page.click_on_item_menu("Add Customer")
        add_customer_page.enter_first_name(first_name)
        add_customer_page.enter_last_name(last_name)
        add_customer_page.enter_post_code(post_code)
        add_customer_page.click_add_customer_submit_btn()

    with allure.step("Проверить, что появилось сообщение об успешной регистрации"):
        msg = add_customer_page.check_successful_message()

        assert msg == "Customer added successfully with customer id :", "Клиент не создан"

    with allure.step("Принять сообщение"):
        add_customer_page.click_alert()

    with allure.step("Проверить, что клиент добавлен"):
        assert (first_name, last_name, post_code) in add_customer_page.get_all_customers_list(), f"Клиент {first_name} {last_name} с почтовым кодом {post_code} не найден в списке всех клиентов"
