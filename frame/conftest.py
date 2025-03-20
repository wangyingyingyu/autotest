"""
__author__ = '霍格沃兹测试开发学社'
__desc__ = '更多测试开发技术探讨，请访问：https://ceshiren.com/t/topic/15860'
"""
import os
import sys
from frame.utils.log_util import logger

# 获取当前工具文件所在的路径
root_path = os.path.dirname(os.path.abspath(__file__))
logger.info(f"当前项目的绝对路径为 {root_path}")
# 把当前项目的绝对路径添加到环境变量中
sys.path.append(root_path)

# 解决用例描述中中文乱码的问题
def pytest_collection_modifyitems(
        session, config, items
) -> None:
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')