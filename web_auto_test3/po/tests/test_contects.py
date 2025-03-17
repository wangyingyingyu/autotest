import logging

import allure

from web_auto_test3.po.page.login_page import Login
from web_auto_test3.po.page.base_page import LiteMall
import pytest

@allure.feature("正向功能")
class TestContects:
    def setup_class(self):
        base_action = LiteMall()
        base_action.action_log()
        # 实例化登录页面对象
#`login_Page` 类通常是与你的应用的主页交互的页面对象，它可能会包含多种方法，用于导航向往后的各个页面。
        log_in = Login()
        # 登录页面跳转到主页
        # self.homepage是HomePage类的实例对象
        self.homepage = log_in.login()
        # self.goodlist1是 GoodList类的实例对象
        # 主页跳转到商品列表页
        self.goodlist1 = self.homepage.click_good_manage()

        #商品列表页跳转到添加商品页
        # self.add 是AddGood类的实例对象
        self.add = self.goodlist1.click_add()

        # -添加商品-跳转到商品列表页，self.goodlist是Good List类的实例对象
        self.goodlist = self.add.add_good()

        # 查找商品
        self.goodlist.find_good()
        # 删除商品

    @allure.story("添加-删除-查询")
    @allure.title("用例1")
    def test_delete(self):
        res = self.goodlist.delete_good_refind()
        logging.info("断言重新查找已经删除的商品是否存在")

        assert res == "暂无数据"
