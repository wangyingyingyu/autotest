from appium.webdriver.common.appiumby import AppiumBy

from frame.page.search_page import SearchPage
from frame.base.base_page import BasePage
class MainPage(BasePage):
    '''
    1、点击搜索框
    2、跳转到搜索页面
    '''
    _CLICK_SEARCH = (AppiumBy.XPATH, "//*[@resource-id='com.xueqiu.android:id/tv_banner']/child::*")
    _CLICK_SELECT = (AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/tab_name" and @text="自选"]')

    # def click_search(self):
    #     self.find_click(*self._CLICK_SEARCH)
    #     return self
    def go_to_search(self):
        """
        点击搜索栏,跳转到搜索页面
        :return: 搜索页面
        """
        self.find_click(*self._CLICK_SEARCH)
        return SearchPage(self.driver)
    def click_select(self):
        """
        点击自选，跳转到自选页面
        :return:
        """
        from frame.page.my_select_page import MySelectPage
        self.find_click(*self._CLICK_SELECT)
        return MySelectPage(self.driver)



