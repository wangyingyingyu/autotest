import time

import yaml
from selenium.webdriver.common.by import By

from web_auto_test.po1.page.base_page import BasePage
from web_auto_test.po1.page.contacts_page import ContactsPage



class MainPage(BasePage):

    # 点击通讯录
    def goto_contacts(self):
        self.driver.find_element(By.XPATH, '//*[@id="menu_contacts"]/span').click()
        return ContactsPage()




