import allure

from pages.list_customers_page import ListCustomersPage


@allure.feature('globalsqa.com')
@allure.title('Удаление клиента')
@allure.description("""
    Цель: Проверить удаление клиента

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    2. Нажать на пункт меню "Customers"
    3. Нажать кнопу "Delete" у тех записей, имена которых соответствует специальному критерию
    4. Проверить, что выбранные клиенты отсутствуют в таблице
    """)
def test_delete_customers(driver):
    with allure.step("Открыть страницу 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        list_customers_page = ListCustomersPage(driver)
        list_customers_page.open()

    with allure.step("Удалить клиентов"):
        list_customers_page.click_on_item_menu("Customers")
        delete_records_list = list_customers_page.delete_customers()

    with allure.step("Проверить, что выбранные клиенты отсутствуют в таблице"):
        all_customers_list = list_customers_page.get_all_customers_list()

        assert list(set(all_customers_list) & set(delete_records_list)) == [], "Клиенты не удалены"