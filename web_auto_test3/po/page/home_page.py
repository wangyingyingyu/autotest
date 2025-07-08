import logging

from web_auto_test3.po.page.base_page import LiteMall
from web_auto_test3.po.page.good_list import GoodList
# 首页
class HomePage(LiteMall):
    # 点击商品管理\商品列表按钮，返回商品列表页

    def click_good_manage(self):
        self.find_click(*self._GOOD_MANAGE)


        self.find_click(*self._GOOD_LIST)


        return GoodList(self._driver)

