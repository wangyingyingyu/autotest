import time

from selenium.webdriver.common.by import By
from web_auto_test.po2.page.base_page import BasePage
from web_auto_test.po2.utils.tools import gen_phone


class ContactsPage(BasePage):
    _ADD_MEMBER = (By.CSS_SELECTOR, '.js_has_member .js_add_member')
    _USERNAME = (By.CSS_SELECTOR, '#username')
    _USER_ACCTID = (By.CSS_SELECTOR, '#memberAdd_acctid')
    _USER_PHONE = (By.CSS_SELECTOR, '#memberAdd_phone')
    _SAVE = (By.CSS_SELECTOR, '.js_btn_save')
    _ADD_SUCCESS = (By.CSS_SELECTOR, '.ww_tip.success')

    _NOT_SAVE_BTN = (By.CSS_SELECTOR, '.js_btn_cancel')
    _NOT_SAVE_TEXT = (By.CSS_SELECTOR, '.msgDlg_right_text')
    _CANCEL_BUTTON = (By.CSS_SELECTOR, '[node-type="cancel"]')

    def add_contacts_save(self):
        self.find_click(*self._ADD_MEMBER)
        self.find_and_send(*self._USERNAME, text=f'test_{int(time.time())}')
        self.find_and_send(*self._USER_ACCTID, text=f'test_{int(time.time())}')
        self.find_and_send(*self._USER_PHONE, text=gen_phone())
        self.find_click(*self._SAVE)
        result = self.wait_element_located(*self._ADD_SUCCESS).text
        return result

    def add_contacts_not_save(self):
        self.find_click(*self._ADD_MEMBER)
        self.find_and_send(*self._USERNAME, text=f'test_{int(time.time())}')
        self.find_and_send(*self._USER_ACCTID, text=f'test_{int(time.time())}')
        self.find_and_send(*self._USER_PHONE, text=gen_phone())
        self.find_click(*self._NOT_SAVE_BTN)
        result = self.get_attr(*self._NOT_SAVE_TEXT, name='text')
        self.find_click(*self._CANCEL_BUTTON)
        return result