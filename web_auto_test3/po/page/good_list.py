import logging

from web_auto_test3.po.page.base_page import LiteMall
from web_auto_test3.po.page.good_add_page import AddGood
from web_auto_test3.po.utils.good_info import get_name,get_ID

# 点击添加按钮
class GoodList(LiteMall):
    def click_add(self):
        self.find_click(*self._ADD_GOOD)
        logging.info("点击商品管理")
        return AddGood(self._driver)




    def delete_good_refind(self):
        self.find_click(*self._DELETE)

        self.find_clear(*self._ID)

        self.find_clear(*self._NANE)

        self.find_good()
        return self.get_toast_text(*self._REFIND)


# 查找商品
    def find_good(self):
        self.web_wait(*self._WAIT_GOOD_LIST_PAGE)

        self.find_send_keys(*self._ID,texts=get_ID())

        self.find_send_keys(*self._NANE,texts=get_name())

        self.find_click(*self._FIND)

