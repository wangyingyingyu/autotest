import logging

from web_auto_test3.po.page.base_page import LiteMall

from web_auto_test3.po.utils.good_info import get_name,get_ID,get_price,get_quantity


# 商品添加页面显示等待

# 添加商品 点击上架跳转到商品列表页面
class AddGood(LiteMall):
    def add_good(self):
        from web_auto_test3.po.page.good_list import GoodList
        self.web_wait(*self._WAIT_ADD_PAGE)
        logging.info("显示等待加载添加商品页面")
        self.find_send_keys(*self._GOOD_ID,texts=get_ID())
        logging.info("输入商品编号")
        self.find_send_keys(*self._GOOD_NAME,texts=get_name())
        logging.info("输入商品名称")
        self.find_click(*self._SETTING)
        logging.info("点击设置")
        self.find_send_keys(*self._GOOD_PRICE,texts=get_price())
        logging.info("输入货品售价")
        self.find_send_keys(*self._GOOD_QUANTITY,texts=get_quantity())
        logging.info("输入货品数量")
        # self.find_send_keys(*self._GOOD_PICTURE,texts=get_price())
        self.find_click(*self._YES)
        logging.info("点击确定")
        self.find_click(*self._LISTING)
        logging.info("点击上架")
        return GoodList(self._driver)

