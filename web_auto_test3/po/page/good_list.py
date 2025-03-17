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
        logging.info("点击删除")
        self.find_clear(*self._ID)
        logging.info("清空商品编号")
        self.find_clear(*self._NANE)
        logging.info("清空商品名称")
        self.find_good()
        return self.get_toast_text(*self._REFIND)


# 查找商品
    def find_good(self):
        self.web_wait(*self._WAIT_GOOD_LIST_PAGE)
        logging.info("显示等待加载商品列表页面")
        self.find_send_keys(*self._ID,texts=get_ID())
        logging.info("输入商品编号")
        self.find_send_keys(*self._NANE,texts=get_name())
        logging.info("输入商品名称")
        self.find_click(*self._FIND)
        logging.info("点击查找")
