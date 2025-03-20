"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os
import time

import yaml

from frame.conftest import root_path
from frame.utils.log_util import logger


class Utils:

    @classmethod
    def get_file_path(cls, path_name):
        '''
        通过相对路径，获取文件的绝对路径
        :param path_name: 文件的相对路径
        :return:
        '''
        # 拼接文件的绝对路径
        path = os.sep.join([root_path, path_name])
        logger.info(f"文件的绝对路径为 {path}")
        return path

    @classmethod
    def get_yaml_data(cls, yaml_path):
        '''
        读取 yaml 文件数据
        :param yaml_path: yaml 文件路径
        :return: 读取到的数据
        '''
        with open(yaml_path, "r", encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas

    @classmethod
    def get_current_time(cls):
        '''
        获取当前的日期与时间
        :return:
        '''
        return time.strftime("%Y-%m-%d-%H-%M-%S")

    @classmethod
    def save_source_datas(cls, source_type):
        '''
        获取保存文件的绝对路径
        :param source_type: 要保存的文件的类型：images 表示保存图片，pagesource 表示保存页面源码
        :return: 绝对路径
        '''
        if source_type == "images":
            end = ".png"
            path = "images"
        elif source_type == "pagesource":
            end = "_pagesource.xml"
            path = "page_source"
        else:
            return None
        # 用当前的时间命令
        source_name = Utils.get_current_time() + end
        # 拼接当前要输出的路径
        source_dir_path = os.sep.join([root_path, path])
        # 如果对应的目录不存在，则创建该目录
        if not os.path.isdir(source_dir_path):
            os.mkdir(source_dir_path)
        # 拼接资源保存的绝对路径
        source_path = os.sep.join([source_dir_path, source_name])
        logger.info(f"资源保存的绝对路径为 {source_path}")
        return source_path