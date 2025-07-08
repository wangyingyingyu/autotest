import logging

from web_auto_test3.po.page.base_page import LiteMall

from web_auto_test3.po.utils.good_info import get_name,get_ID,get_price,get_quantity


# 商品添加页面显示等待

# 添加商品 点击上架跳转到商品列表页面
class AddGood(LiteMall):
    def add_good(self):
        from web_auto_test3.po.page.good_list import GoodList
        self.web_wait(*self._WAIT_ADD_PAGE)

        self.find_send_keys(*self._GOOD_ID,texts=get_ID())

        self.find_send_keys(*self._GOOD_NAME,texts=get_name())

        self.find_click(*self._SETTING)

        self.find_send_keys(*self._GOOD_PRICE,texts=get_price())

        self.find_send_keys(*self._GOOD_QUANTITY,texts=get_quantity())

        self.find_click(*self._YES)

        self.find_click(*self._LISTING)

        return GoodList(self._driver)

