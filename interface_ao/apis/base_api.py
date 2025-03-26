# 单独管理通讯录-部门管理相关接口
import requests
from interface_ao.utils.log_utils import logger
class BaseApi:
    """
    直接字典的结构体进去，然后解包字典，获得关键字参数
    """
    def send(self,seq):
        """
        对request进行二次封装
        :param seq:
        :return:返回请求对象
        """
        # seq = {
        #     "method":"POST",
        #     "url": "http://域名：端口号/资源路径",
        #     "params": "url后拼接的参数",
        #     "json":"json格式的请求体"
        #
        # }
        # r = requests.request(method=method,url=url,params=params,json=json)
        r = requests.request(**seq)
        logger.info("调用接口成功")
        return r


