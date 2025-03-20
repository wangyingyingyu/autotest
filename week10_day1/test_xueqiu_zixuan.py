from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestAppium:
    def setup_method(self):
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

    def teardown_method(self):
        self.driver.quit()
    def test_xueqiu_zixuan(self):
        # 点击自选
        el1 = self.driver.find_element(AppiumBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/tab_name' and @text='自选']")
        el1.click()
        # 点击全部
        el2 = self.driver.find_element(AppiumBy.XPATH,"//*[@class='android.widget.TextView' and @text='全部']")
        el2.click()
        # 点击最新价
        el3 = self.driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/item_layout" and @text="最新价"]')
        el3.click()
        # 获取价格
        eles = self.driver.find_elements(AppiumBy.XPATH,"//*[@resource-id='com.xueqiu.android:id/content_recycler']//*[@resource-id='com.xueqiu.android:id/row_recycler']/android.widget.FrameLayout[1]//*[@resource-id='com.xueqiu.android:id/item_layout']")
        ele_price = []
        for e in eles:
            ele_price.append(float(e.text))
        print(ele_price)
        # 点击两次最新价，复原状态
        # el3.click()
        # el3.click()
        sorted_list = sorted(ele_price, reverse=True)
        print(f"排序之后的列表为{sorted_list}")
        assert ele_price == sorted_list
        # print(el4)
        # print(type(el4))


