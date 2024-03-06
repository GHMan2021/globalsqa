from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from data.config import WAIT_TIMEOUT


class BasePage:
    PAGE_URL = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/manager"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout=WAIT_TIMEOUT, poll_frequency=1)

    def open(self):
        self.driver.get(self.PAGE_URL)

    def element_to_be_clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def alert_is_present(self):
        return self.wait.until((EC.alert_is_present()))

    def presence_of_element_located(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def presence_of_all_elements_located(self, locator):
        return self.wait.until(EC.presence_of_all_elements_located(locator))
