from appium.webdriver.common.appiumby import AppiumBy

from frame.base.base_page import BasePage
class MySelectPage(BasePage):
    _CLICK_ALL = (AppiumBy.XPATH,'//*[@text="全部"]')
    _GET_ALL = (AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/content_recycler"]//*[@resource-id="com.xueqiu.android:id/portfolio_stockName"]')

    def click_all(self):
        """
        点击全部按钮
        :return:
        """
        self.find_click(*self._CLICK_ALL)
        return self
    def get_all(self):
        """
        获取已经添加到自选的公司的元素对象
        for循环遍历多元素对象
        :return:返回元素文本信息列表
        """
        els = self.find_els(*self._GET_ALL)

        return self.get_list(els)