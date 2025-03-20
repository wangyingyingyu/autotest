from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.webdriver import WebDriver
from selenium.common import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from frame.base.error_handle import black_wrapper
from frame.utils.utils import Utils


class BasePage:
    def __init__(self,driver:WebDriver=None):
        self.driver = driver

    @black_wrapper
    def find_ele(self,by,value):
        return self.driver.find_element(by,value)

    @black_wrapper
    def find_els(self,by,value):
        return self.driver.find_elements(by,value)

    @black_wrapper
    def find_click(self,by,value):
        return self.driver.find_element(by,value).click()
    def set_implicitly(self,wait_time=10):
        """

        :param wait_time: 等待时间
        :return:
        """
        return self.driver.implicitly_wait(wait_time)


    def explicit_wait_presence(self,by,value,wait_time=10):
        """
        设置显示等待直到元素存在
        :param by: 元素定位方法
        :param value: 元素定位表达式
        :param wait_time: 显示等待时间
        :return: 返回显示等待表达式
        """
        return WebDriverWait(self.driver,wait_time).until(EC.presence_of_element_located((by,value)))
    def explicit_wait_visibility(self,by,value,wait_time=10):
        """
        设置显示等待直到元素可见
        :param by:
        :param value:
        :param wait_time:
        :return:
        """
        els = WebDriverWait(self.driver,wait_time).until(EC.visibility_of_element_located((by,value)))
        return els

    @black_wrapper
    def explicit_visibility_click(self,by,value):
        return self.explicit_wait_visibility(by,value,wait_time=30).click()



    def get_list(self,els):
        """
        使用for循环遍历获得的元素对象，这个对象包含了多个同类型的元素
        :param els: 显示等待返回的多元素对象
        :return: 元素对象文本信息列表的第一个元素的文本信息
        """
        els_list = []
        for e in els:
            els_list.append(e.text)
        return els_list
    def find_is_displayed(self,by,value):
        """
        判断元素是否可见，是返回True，不是返回False
        :return:
        """
        return self.explicit_wait_visibility(by,value).is_displayed()

    def set_implicitly_wait(self, time=1):
        '''
        设置隐式等待的时间
        :param time: 时间
        '''
        self.driver.implicitly_wait(time)

    def go_back(self, num=1):
        '''
        返回上一个页面
        :param num: 点击返回按钮的次数
        '''
        for i in range(num):
            self.driver.back()

    def wait_ele_locate(self, by, value, time=10):
        '''
        显示等待某个元素可以被定位
        :param by: 定位方式
        :param value: 定位表达式
        :param time: 等待时间
        '''
        ele = WebDriverWait(self.driver, time).until(
            EC.visibility_of_element_located((by, value))
        )
        return ele

    def wait_ele_clickable(self, by, value, time=10):
        '''
        等待元素可以被点击
        :param by: 定位方式
        :param value: 定位表达式
        :param time: 等待时间
        '''
        ele = WebDriverWait(self.driver, time).until(
            EC.element_to_be_clickable((by, value))
        )
        return ele

    def swipe_window(self):
        '''
        滑动界面
        '''
        # 先获取到界面屏幕的大小
        window_size = self.driver.get_window_size()
        # {'width': 900, 'height': 1600}
        print(window_size)
        # 根据界面的宽和高，计算需要的坐标值
        width = window_size.get("width")
        height = window_size.get("height")
        # 起始点的坐标
        start_x = width * 0.5
        start_y = height * 0.8
        end_x = start_x
        end_y = height * 0.2
        # 执行滑动操作
        self.driver.swipe(start_x, start_y, end_x, end_y, duration=1000)

    def swipe_find_text(self, text, max_num=10):
        '''
        滑动查找文本
        :param text: 要查找的文本元素
        :param max_num: 最多滑动屏幕的次数
        '''
        # 为了能滑动的更快，需要先把隐式等待的时间设置短一些
        self.set_implicitly_wait()
        for i in range(max_num - 1):
            try:
                ele = self.find_ele(AppiumBy.XPATH, f"//*[@text='{text}']")
                # 找到元素之后，把隐式等待时间设置到原来的长度
                self.set_implicitly_wait(20)
                return ele
            except Exception as e:
                print(e)
                # 滑动屏幕
                self.swipe_window()
        # 如果最终没有找到元素，也需要把隐式等待的时间设置复原
        self.set_implicitly_wait(20)
        raise NoSuchElementException(f"滑动{max_num}之后，没有找到 {text} 元素")

    def screenshot(self):
        '''
        截图
        :return: 截图保存的路径
        '''
        file_path = Utils.save_source_datas("images")
        # 截图
        self.driver.save_screenshot(file_path)
        return file_path

    def save_page_source(self):
        '''
        保存页面源码
        :return:
        '''
        file_path = Utils.save_source_datas("pagesource")
        # 写 page source 文件
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)
        return file_path