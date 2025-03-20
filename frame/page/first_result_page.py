from appium.webdriver.common.appiumby import AppiumBy

from frame.base.base_page import BasePage
class First_result_page(BasePage):
    _CLICK_AUTO_SELECT = (AppiumBy.XPATH,
            '//*[@resource-id="com.xueqiu.android:id/floating_action_text_view_id" and @text="加自选"]')
    _GO_BACK1 = (AppiumBy.ID,'com.xueqiu.android:id/action_back')
    _IS_DISPLAYED = (AppiumBy.ID,'com.xueqiu.android:id/iv_close')
    _SET_AUTO_SELECT = (AppiumBy.XPATH,'//*[@resource-id="com.xueqiu.android:id/floating_action_text_view_id" and @text="设自选"]')
    _CLICK_DELETE_AUTO_SELECT = (AppiumBy.XPATH,'//*[@text="删除自选"]')

    def click_add_select(self):
        """
        显示等待:
        如果是自选按钮出现点击加自选按钮
        如果是设自选按钮等待
            点击设自选按钮，出现小页面
            点击删除自选

        如果出现相关活跃用户弹窗，点击关闭
        :return:
        """
        # if self.find_is_displayed(*self._CLICK_AUTO_SELECT):
        #     self.explicit_visibility_click(*self._CLICK_AUTO_SELECT)
        # else:
        #     if self.find_is_displayed(*self._SET_AUTO_SELECT):
        #         self.explicit_visibility_click(*self._SET_AUTO_SELECT)  # 点击设自选按钮
        #         self.explicit_visibility_click(*self._CLICK_DELETE_AUTO_SELECT)  # 点击删除自选按钮
        # if self.find_is_displayed(*self._IS_DISPLAYED):
        #     self.find_click(*self._IS_DISPLAYED)

        self.explicit_visibility_click(*self._CLICK_AUTO_SELECT)
        if self.find_is_displayed(*self._IS_DISPLAYED):
            self.find_click(*self._IS_DISPLAYED)

        # self.explicit_visibility_click(*self._SET_AUTO_SELECT)
        # self.explicit_visibility_click(*self._CLICK_DELETE_AUTO_SELECT)
        return self

    def go_back_result_page(self):
        """
        点击回退上一页按钮,回到搜索结果页
        :return:
        """

        # self.find_click(*self._GO_BACK1)
        self.explicit_visibility_click(*self._GO_BACK1)
        from frame.page.result_page import ResultPage
        return ResultPage(self.driver)
