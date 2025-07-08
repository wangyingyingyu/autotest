import time

from selenium.webdriver.common.by import By

from web_auto_ERP_test.po.page.base_page import BasePage
from web_auto_ERP_test.po.page.waiting_sent_flow import WaitingSent
from web_auto_ERP_test.po.utils.get_datas import get_data

_SELECT_CHANNEL = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div[1]/div/input')
_CHANNEL = (By.XPATH, '/html/body/div[2]/div[1]/div[1]/ul/li[1]')
_WRITE_TEXT = (By.XPATH, "//*[@autocomplete='off' and @rows='9']")
_RECOGNIZE_TEXT = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[1]/button')
_SELECT_GOOD_LIST = (By.XPATH, '(//*[@placeholder="请选择"])[1]')
_SELECT_GOOD = (By.XPATH, '/html/body/div[3]/div[1]/div/div/span/span')
_FIRST_GOOD = (By.XPATH, '/html/body/div[4]/div[1]/div[1]/span')
_ALL_FIX = (By.XPATH, '//*[@class="el-button el-button--default el-button--small el-button--primary "]')
_XIA_LA_TIAO = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]')
_CLICK_NUM = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div')
_INPUT_NUM = (By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[1]/td[6]/div/div/div/input')
_SECOUND_NUM = (By.XPATH, '/html/body/div[1]/div[1]/div[2]/section/div/div[2]/div[1]/div[3]/table/tbody/tr[2]/td[6]')
_FIX_TOGTHER = (By.XPATH, '/html/body/div[3]/div/div[3]/button[2]')
_ALL_SUBMIT = (By.XPATH, '//*[text()="全部提交"]')
class OrderCreate(BasePage):

    def order_create(self):
        """
        1、添加订单，
        2、选择渠道测试
        3、自动文本识别录入
        4、选择系统中已存在的商品列表的第一个商品，一起修改商品输入框，输入商品数量，一起修改商品数量
        5、点击全部提交
        :return:
        """
        # 点击请选择所属渠道,展示系统中存在的渠道列表
        self.find_click(*_SELECT_CHANNEL)
        # 点击所选渠道
        time.sleep(1)
        self.find_click(*_CHANNEL)
        # 文本框输入收件人、收件人电话、收件人地址
        self.find_send_keys(*_WRITE_TEXT,texts=get_data())

        # 点击识别文本信息按钮
        self.find_click(*_RECOGNIZE_TEXT)
        # 双击商品下拉框，展示系统中已存在商品
        self.wait_clickable_click(*_SELECT_GOOD_LIST,wait_time=20)
        self.wait_clickable_click(*_SELECT_GOOD_LIST,wait_time=20)
        time.sleep(1)
        # 等待商品列表的第一行商品出现，点击第一行商品
        self.wait_present_click(*_SELECT_GOOD,wait_time=30)
        time.sleep(1)
        # 点击第一行商品的第一个规格
        self.wait_present_click(*_FIRST_GOOD)
        # 点击是一起修改
        self.find_click(*_ALL_FIX)

        # 向右滑动到商品数量输入框
        element = self.find(*_XIA_LA_TIAO)
        self.scroll_right(element)
        # 或者使用 scrollTo 方法来滚动特定的距离
        # driver.execute_script("arguments[0].scrollTo(arguments[0].scrollLeft + 100, 0);", element)
        time.sleep(2)
        # 点击数量输入框
        self.find_click(*_CLICK_NUM)
        self.web_wait_present_sendkeys(*_CLICK_NUM ,wait_time=10,text='100')
        # 点击第二个数量框
        self.find_click(*_SECOUND_NUM)
        # 点击一起修改商品数量按钮
        self.wait_visibility_click(*_FIX_TOGTHER,wait_time=60)
        # 点击全部提交按钮

        self.find_click(*_ALL_SUBMIT)
        return WaitingSent(self._driver)