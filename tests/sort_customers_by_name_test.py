import allure

from pages.list_customers_page import ListCustomersPage


@allure.feature('globalsqa.com')
@allure.title('Сортировка клиентов по имени (First Name)')
@allure.description("""
    Цель: Проверить сортировка клиентов по имени

    Предусловие: Открыть браузер

    Шаги:
    1. Открыть страницу "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"
    2. Нажать на пункт меню "Customers"
    3. Дважды нажать на заголовок таблицы "First Name" для сортировки пользователей по имени
    4. Проверить, что имена отсортирована в алфавитном порядке
    """)
def test_sort_by_first_name(driver):
    with allure.step("Открыть страницу 'https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager'"):
        list_customers_page = ListCustomersPage(driver)
        list_customers_page.open()

    with allure.step("Сортировать пользователей по имени"):
        list_customers_page.click_on_item_menu("Customers")
        list_customers_page.sort_by_first_name()

    with allure.step("Проверить, что имена отсортированы в алфавитном порядке "):
        all_customers = list_customers_page.get_all_customers_list()
        sorted_all_customers = sorted(all_customers, key=lambda first_name: first_name[0])

        assert all_customers == sorted_all_customers, "Клиенты не отсортированы по имени"
