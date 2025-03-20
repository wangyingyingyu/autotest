from appium.webdriver.common.appiumby import AppiumBy
from frame.page.first_result_page import First_result_page
from frame.base.base_page import BasePage
class ResultPage(BasePage):
    '''
    获取第一个搜索结果的文本信息
    result = self.find_ele(AppiumBy.XPATH, f"//*[@text='{search_key}']")

    '''
    _GET_TEXT = (AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/stock_name_tv"]')
    # _GET_FIRST_RESULT = (AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/stock_name_tv" and @text="search_text"]')
    _GO_BACK2 = (AppiumBy.ID, 'com.xueqiu.android:id/back_iv')
    def get_first_text(self):
        """

        :return: 返回搜索结果页的第一个搜索结果文本信息
        """
        result_els = self.find_els(*self._GET_TEXT)
        result_text =self.get_list(result_els)
        return result_text[0]
    def click_first_result(self,search_text):
        """
        点击第一个搜索结果
        :return:
        """

        self.find_click(AppiumBy.XPATH, f"//*[@text='{search_text}']")
        return self
    def get_first_result_page(self):
        """
        跳转到第一个搜索结果页
        :return:
        """
        return First_result_page(self.driver)
    def go_back_main_page(self):
        """
        点击回退按钮，返回首页
        :return:首页
        """
        self.find_click(*self._GO_BACK2)
        from frame.page.main_page import MainPage
        return MainPage(self.driver)

