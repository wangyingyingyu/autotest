import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class TestWebdriverWait:

    driver = webdriver.Chrome()

    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://vip.ceshiren.com/#/ui_study")
    def teardown(self):
        self.driver.quit()
    def test_webdriver_wait(self):
        # 解决的问题：有的按钮点击一次没有反应，可能要点击多次，比如企业微信的添加成员
        # 解决的方案：一直点击按钮，直到下个页面出现，封装成显式等待的一个条件
        #- **内部方法**：定义了一个内部函数 `muliti_click`，
        # 该函数需要两个参数：`button_element` 表示按钮元素的 XPath 表达式，`until_ele` 表示期望出现的元素的 XPath 表达式。
        def muliti_click(button_element,until_ele):
            # 函数封装
            def inner(driver):
                # 封装点击方法
                #- **点击按钮**：在 `inner` 函数中，使用 `find_element` 方法找到指定的按钮元素并点击它
                driver.find_element(By.XPATH,button_element).click()
                #- **返回值**：查找到期望的元素并返回。当 `inner` 函数成功返回该元素时，`muliti_click` 函数的条件就满足了。
                return driver.find_element(By.XPATH,until_ele)
            #- **返回内部函数**：`muliti_click` 返回 `inner` 函数，使得外部可以在 `WebDriverWait` 中调用它
            return inner
        time.sleep(5)
        # 在限制时间内会一直点击按钮，直到展示弹框
        WebDriverWait(self.driver,10).until(muliti_click("//*[text()='点击两次响应']","//*[text()='该弹框点击两次后才会弹出']"))
        time.sleep(5)
    # until必须传入method函数参数until(method)，这里传入了muliti_click()函数返回了inner函数名，即将inner函数作为参数传进until方法中，
    #这时inner函数中作为判断语句，执行1、点击指定XPATH按钮，执行return语句这句是要求找到期望的元素是返回Trueuntil在指定时间内结束循环，
    # 若没有找到期望元素（一个页面的标题）返回False或None，until方法收到False或None结果后，会再次执行inner函数内的操作即点击按钮，直到显示出指定标题或期望页面
    #