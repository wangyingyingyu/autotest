from selenium.webdriver.common.by import By
from web_auto_ERP_test.po.page.order_create import OrderCreate

from web_auto_ERP_test.po.page.base_page import BasePage

class MainPage(BasePage):
    _ORDER_MANAGE = (By.XPATH, '/html/body/div[1]/div[1]/div[1]/div/div[1]/div/ul/div[9]')
    _ORDER_IN = By.XPATH, '//*[@id="app"]/div[1]/div[1]/div/div[1]/div/ul/div[9]/li/ul/div[4]'
    _AUTO_CREATE = By.XPATH, '//*[@id="app"]/div[1]/div[2]/section/div/div/div[2]/div/p[1]'
    def main_page(self):
        """
        # 点击订单管理
        # 点击订单录入
        # 点击手动创建按钮，进入创建订单页面
        :return: 返回创建订单-文本输入页面
        """
        self.find_click(*self._ORDER_MANAGE)
        self.find_click(*self._ORDER_IN)
        self.find_click(*self._AUTO_CREATE)
        return OrderCreate(self._driver)