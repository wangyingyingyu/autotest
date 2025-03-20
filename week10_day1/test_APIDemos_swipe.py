# 滑动的方式
# swipe 方法
# 从一个点滑动到另一个点，可选择持续时间，具有滑动的惯性。需要的参数如下：
#
# start_x：开始坐标 x。
# start_y：开始坐标 y。
# end_x：结束坐标 x。
# end_y：结束坐标 y。
# duration（可选）：滑动持续的时间，默认为 0。
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
                "platformName": "android",
                "appium:automationName": "uiautomator2",
                "appium:deviceName": "emulator-5554",
                "appium:appPackage": "io.appium.android.apis",
                "appium:appActivity": ".ApiDemos"
            }
        )
    # 初始化 Webdriver，连接 Appium 服务器
        self.driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        self.driver.quit()
    def test_demos_swipe(self):
        # 点击Views
        self.driver.find_element(by=AppiumBy.XPATH,value='//*[@resource-id="android:id/text1" and @text="Views"]').click()
        # 下划
        # 先获取模拟器窗口大小
        window_size = self.driver.get_window_size()
        print(window_size)
        print(type(window_size))
       # {'width': 720, 'height': 1280} <class 'dict'>
        window_width = float(window_size.get("width"))
        window_height = float(window_size.get("height"))
        # print(type(window_width))  # int

        start_x = window_width*0.5
        start_y = window_height*0.8
        end_x = window_width*0.5
        end_y = window_height*0.2
        self.driver.swipe(start_x,start_y, end_x, end_y,duration=2000)
        # 点击PopupMenu
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Popup Menu").click()
        # 点击Make a Popup!
        self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID,value="Make a Popup!").click()
        # 点击搜索
        self.driver.find_element(AppiumBy.XPATH,'//*[@resource-id="android:id/title" and @text="Search"]').click()
        # 获取页面源码 查找Toast元素
        page_source = self.driver.page_source
        print(page_source)
#<android.widget.Toast index="1" package="com.android.settings" class="android.widget.Toast" text="Clicked popup menu item Search" displayed="true" />

        toast_text = self.driver.find_element(AppiumBy.XPATH,'//*[@class="android.widget.Toast"]').text
        assert toast_text == "Clicked popup menu item Search"











