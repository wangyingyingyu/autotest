import time

import allure
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from week10_day1.log_configuration import LogSet

@allure.epic("雪球APP测试")
@allure.feature("搜索-自选")
class TestAppium(LogSet):
    def setup_method(self):
        self.action_log()
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
    # 初始化 Webdriver，连接 Appium 服务器
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.find_element(AppiumBy.XPATH,'//*[@text="雪球"]').click()
        self.driver.quit()
    @allure.title("搜索企业并设置自选")
    def test_xueqiu(self):
        # 点击输入框
        self.get_picture_source()
        with allure.step("测试步骤一：点击输入框"):
            self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tv_banner']/child::*").click()
        # 设置显示等待，等待搜索输入框出现并可交互
        el2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.xueqiu.android:id/search_input_text"))
        )
        # 文本框输入 美的
        self.get_picture_source()
        with allure.step("测试步骤一：点击输入框"):
            el2.send_keys("美的")
        # 点击搜索
        self.get_picture_source()
        self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_text").click()

        time.sleep(1)
        # 获取第一个搜索结果文本信息
        self.get_picture_source()
        result_eles = self.driver.find_elements(AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/stock_name_tv"]')
        result_list = []
        for e in result_eles:
            result_list.append(e.text)
        first_ele = result_list[0]
        # 点击第一个搜索结果
        self.get_picture_source()
        self.driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/stock_name_tv" and @text="美的集团"]').click()
        # 点击加自选按钮
        time.sleep(1)
        self.get_picture_source()
        self.driver.find_element(AppiumBy.XPATH,
        '//*[@resource-id="com.xueqiu.android:id/floating_action_text_view_id" and @text="加自选"]').click()
        # 点击回退上一页按钮
        self.get_picture_source()
        self.driver.find_element(AppiumBy.ID,'com.xueqiu.android:id/action_back').click()
        # 点击搜索页回退按钮
        self.get_picture_source()
        self.driver.find_element(AppiumBy.ID,'com.xueqiu.android:id/back_iv').click()

        # 点击自选
        self.get_picture_source()
        self.driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="自选"]').click()
        # 点击全部
        self.get_picture_source()
        self.driver.find_element(AppiumBy.XPATH,'//*[@text="全部"]').click()
#com.xueqiu.android:id/portfolio_stockName
        # 获取已加自选公司的对象
        self.get_picture_source()
        eles = self.driver.find_elements(AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/content_recycler"]//*[@resource-id="com.xueqiu.android:id/portfolio_stockName"]')
        # 获取公司名称文本信息
        e_list = []
        for e in eles:
            e_list.append(e.text)
        print(e_list)
        assert first_ele in e_list
