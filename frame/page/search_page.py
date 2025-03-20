from appium.webdriver.common.appiumby import AppiumBy

from frame.page.result_page import ResultPage
from frame.base.base_page import BasePage

class SearchPage(BasePage):
    '''
    1、显示等待搜索页面，搜索框输入文本信息
    2、点击搜索
    3、跳转到搜索结果页
    '''
    _GO_TO_SEARCH = (AppiumBy.ID, "com.xueqiu.android:id/search_input_text")
    # 点击搜索
    _CLICK_FIRST = (AppiumBy.ID, "com.xueqiu.android:id/tv_text")
    def input_search(self,input_text):
        """
        1、显示等待搜索页面，搜索框输入文本信息
        :param input_text: 搜索框输入文本信息
        :return:
        """
        self.explicit_wait_visibility(*self._GO_TO_SEARCH).send_keys(input_text)
        return self
    def click_first(self):
        """
        2、点击搜索
        :return:
        """
        self.find_click(*self._CLICK_FIRST)
        return self
    def go_to_result_page(self):
        """
        3、跳转到搜索结果页
        :return:
        """
        return ResultPage(self.driver)
