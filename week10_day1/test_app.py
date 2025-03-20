from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

class TestAppium:
    def setup_method(self):
        options = AppiumOptions()
        options.load_capabilities(
            {
                "platformName": "android",
                "appium:automationName": "uiautomator2",
                "appium:ensureWebviewsHavePages": True,
                "appium:nativeWebScreenshot": True,
                "appium:newCommandTimeout": 3600,
                "appium:connectHardwareKeyboard": True
            }
        )
    # 初始化 Webdriver，连接 Appium 服务器
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

    def teardown_method(self):
        self.driver.quit()
    def test_appium(self):
        el1 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="App")
        el1.click()
        el2 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Search")
        el2.click()
        el3 = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Invoke Search")
        el3.click()
        el4 = self.driver.find_element(by=AppiumBy.ID, value="io.appium.android.apis:id/txt_query_prefill")
        el4.send_keys("hogwarts")
        self.driver.back()
        self.driver.back()
        self.driver.back()

# 参数化创建成员
# 参数化搜索成员





