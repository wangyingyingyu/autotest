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
    def test_xueqiu(self):
        # 点击输入框 /child::*
        el1 = self.driver.find_element(by=AppiumBy.XPATH, value="//*[@resource-id='com.xueqiu.android:id/tv_banner']/child::*")
        # 输入框是否可用
        print(el1.is_enabled())
        # # 获取输入框，text属性 resource-id="com.xueqiu.android:id/tv_banner/*/*"
        # ele = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_banner/child::*")
        # print(ele.get_attribute("text"))
        # 输入框坐标
        print(el1.location)
        # 输入框格式大小
        print(el1.size)
        # 输入 alibaba
        el1.click()
        # com.xueqiu.android:id/search_input_text
        #el2 = self.driver.find_element(AppiumBy.ID,'com.xueqiu.android:id/search_input_text')
        # 等待搜索输入框出现并可交互
        el2 = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((AppiumBy.ID, "com.xueqiu.android:id/search_input_text"))
        )
        el2.send_keys("alibaba")
        #
        el3 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/tv_text")
        # # 点击搜索 com.xueqiu.android:id/current_price_dtv
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="com.xueqiu.android:id/current_price_dtv")
        price = float(el4.text)
        # assert price == '147.57'
        # el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="com.xueqiu.android:id/stock_name_tv")
        # # 获取搜索结果页面文本信息
        # texts = el3.text
        # assert texts == "阿里巴巴"
        # 计算 137 上下 10% 的浮动范围
        lower_bound = 147 * 0.9  # 下界
        upper_bound = 147 * 1.1  # 上界

        # 断言价格是否在范围内
        assert lower_bound <= price <= upper_bound, f"股票价格 {price} 在 147 上下 10% 的范围内"
