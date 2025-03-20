import time

import allure
import yaml
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from week10_day1.log_configuration import LogSet
from frame.page.main_page import MainPage
from frame.base.base_page import BasePage


# data = ["阿里","美的","腾讯"]
# with open("../datas/stock_name.yaml",'w') as f:
#     yaml.dump(data, f, allow_unicode=True)



class XueQiu(BasePage):
    '''
    1、打开app，要调用同类中的方法，返回自身实例对象
    2、跳转到首页,返回MainPage实例对象
    3、设置资源销毁，关闭webdriver对象
    '''
    _XUE_QIU = (AppiumBy.XPATH,'//*[@text="雪球"]')
    def app_start(self):
        options = AppiumOptions()
        options.load_capabilities(
            {
                "appium:platformName": "Android",
                "appium:platformVersion": "6.0.1",
                "appium:automationName": "UiAutomator2",
                "appium:deviceName": "MuMu",
                "appium:appPackage": "com.xueqiu.android",
                "appium:appActivity": "com.xueqiu.android.mainnesting.view.MainNestingActivity",
                "appium:noReset": True
            }
        )
        # 初始化webdriver并连接appium服务器
        self.driver = webdriver.Remote('http://127.0.0.1:4723',options=options)
        # 设置隐式等待
        self.driver.implicitly_wait(5)
        return self
    def app_end(self):
        """
        点击雪球按钮
        返回雪球首页
        关闭 appium_server
        :return:
        """
        # self.find_click(*self._XUE_QIU)
        self.driver.quit()
    def go_to_main(self):

        return MainPage(self.driver)
    def click_xueqiu(self):
        """
        点击雪球回到首页
        :return:
        """

    # def stop(self):
    #     '''
    #     关闭 app
    #     :return:
    #     '''
    #     self.driver.terminate_app("com.xueqiu.android")
    #     self.driver.quit()