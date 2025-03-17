from selenium.webdriver.common.by import By

from web_auto_test.po2.page.base_page import BasePage
from web_auto_test.po2.page.contacts_page import ContactsPage


class MainPage(BasePage):
    _CONTACTS = (By.CSS_SELECTOR, '#menu_contacts')

    def goto_contacts(self):
        self.find_click(*self._CONTACTS)
        return ContactsPage(self._driver)