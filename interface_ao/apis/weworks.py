# 获取与业务无关的token
import os

from interface_ao.apis.base_api import BaseApi
from interface_ao.utils.utils import Utils


class WeWork(BaseApi):
    def __init__(self):

        # 获取配置文件yaml的绝对路径
        yaml_path = os.sep.join([Utils.get_path(), "python_learn\interface_ao\config\wework.yaml"])
        #print(yaml_path)
        # 读取yaml文件内容
        datas = Utils.get_yaml_data(yaml_path)
        self.base_url = datas["base_url"]
        self.corpid=datas["corpid"]
        self.corpsecret=datas["corpsecret"]
        # 组装获取token的url
        self.url = f"{self.base_url}/gettoken"
        #调用获取token的封装方法进而赋值给变量，方便后面继承者使用

        self.token = self.get_token()


    def get_token(self):
        """
        获取token
        :return:
        """
        params = {
            "corpid": self.corpid,
            "corpsecret": self.corpsecret
        }
        method="GET"
        seq = {
            "method":method,
            "url": self.url,
            "params": params
        }

        r=self.send(seq)
        # r = requests.get(url, params)
        return r.json()["access_token"]
