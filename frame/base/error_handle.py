"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import allure
from appium.webdriver.common.appiumby import AppiumBy

from frame.utils.log_util import logger

# 弹窗黑名单
# 放可能出现的弹窗的关闭元素的定位方式
black_list = [
    (AppiumBy.XPATH, "//*[@text='确定']"),
    (AppiumBy.XPATH, "//*[@text='取消']"),
]


# 传入的 fun 相当于 find(self, by, value):
def black_wrapper(fun):

    def run(*args, **kwargs):
        # 相当于传入的第一个参数 self
        basepage = args[0]
        try:
            logger.info(f"开始查找元素：{args[1]}, {args[2]}")
            # 恢复隐式等待设置
            basepage.set_implicitly_wait(20)
            return fun(*args, **kwargs)
        except Exception as e:
            # 设置隐式等待时间为 1 s
            basepage.set_implicitly_wait()
            logger.warning("未找到元素，处理异常")
            # 遇到异常截图
            image_path = basepage.screenshot()
            allure.attach.file(
                image_path,
                name="查找元素异常截图",
                attachment_type=allure.attachment_type.PNG
            )
            # 保存页面源码
            pagesource_path = basepage.save_page_source()
            allure.attach.file(
                pagesource_path,
                name="查找元素异常页面源码",
                attachment_type=allure.attachment_type.TEXT
            )
            for b in black_list:
                #  查找黑名单中的每一个元素
                eles = basepage.driver.find_elements(*b)
                if len(eles) > 0:
                    # 点击弹框
                    basepage.driver.find_elements(*b)[0].click()
                    # 恢复隐式等待设置
                    basepage.set_implicitly_wait(20)
                    # 继续查找元素
                    return fun(*args, **kwargs)
            logger.error(f"遍历黑名单，仍未找到元素，异常信息为 ====> {e}")
            # 恢复隐式等待设置
            basepage.set_implicitly_wait(20)
            raise e
    return run