import allure
import pytest
import logging
import os
import time

# 配置日志
class LogSet:
    def action_log(self):
        log_folder = "./data/logs"
        # 如果日志文件夹不存在，则创建
        if not os.path.exists(log_folder):
            os.makedirs(log_folder)

        # 设置日志文件的路径
        log_file = os.path.join(log_folder, "log.log")

        # 配置日志
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file),  # 输出到文件
                logging.StreamHandler()  # 输出到控制台
            ]
        )

    def screen(self):
        # 获取当前时间，并将其格式化为YYYYMMDDHHMMSS的字符串格式
        now_time = time.strftime('%Y%m%d%H%M%S')
        # 将当前时间作为文件名，生成一个PNG格式的文件
        image_name = f'{now_time}.png'
        # 拼接路径前提要有上一层目录
        filepath = f"./data/img/{image_name}"
        # 当前屏幕截图保存到指定的文件路径
        self.driver.get_screenshot_as_file(filepath)
        allure.attach.file(filepath,
        # 这里需改成自己想要的图片的路径,
        name = "截图",
        attachment_type = allure.attachment_type.PNG,
        extension = "png")

    def get_page_source(self):
        # 获取当前时间，并将其格式化为YYYYMMDDHHMMSS的字符串格式
        now_time = time.strftime('%Y%m%d_%H%M%S')  # 使用下划线作为分隔符
        # 将当前时间作为文件名，生成一个html格式的文件
        page_source_name = f'{now_time}.html'

        # 使用os.path.join构建文件路径，确保跨平台兼容性
        filepath = os.path.join(".", "data", "html", page_source_name)

        # 如果目录不存在，则创建
        os.makedirs(os.path.dirname(filepath), exist_ok=True)

        # 获取页面源码
        page_source = self.driver.page_source

        # 将页面源码写入文件
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(page_source)
        allure.attach(page_source,
                      '附件是HTML类型',
                      allure.attachment_type.HTML,
                      extension = "html")
    def get_picture_source(self):
        self.screen()
        self.get_page_source()