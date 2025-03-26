import requests
import pytest
import allure
import jsonpath

"""
接口鉴权
获取接口调用凭证-企业 ID（需要有管理员权限）
Corpid（企业 ID）
每个企业都拥有唯一的 corpid
查看：管理后台【我的企业】--【企业信息】下查看【企业 ID】
获取接口调用凭证-Secret（需要开启【API 接口同步】）
Secret（应用的凭证密钥）
通讯录管理 secret
查看：【管理工具】--通讯录同步
"""

class TestQiYeWeiXin:
    def setup_class(self):
        self.base_url = "https://qyapi.weixin.qq.com"



    # def test_get_token(self):
    #     """
    #     获取token的第一种方法 直接拼接在url后面
    #     """
    #     SECRET = '-O1EaM2IcBxVPmSsEKPiDLt6PFkQrWDxf6km0S03qrs'
    #     ID = 'wwaba5e80f616dd925'
    #     url = f'{self.base_url}/cgi-bin/gettoken?corpid={ID}&corpsecret={SECRET}'
    #     r = requests.get(url=url)
    #     print(r.json())
    #     # {
    #     #     'errcode': 0,
    #     #     'errmsg': 'ok',
    #     #     'access_token': 'tjNcDbnEKdB1dgxImBdpwbLWqHIqTXHv8ysxEtyD0T25Fsgc7wlQbFQJOSUlCZFRsoSNuER3T8FN2RNS8MfG9aa2DzCKMXO4PtFqlNw263OpsXItOdPYV_vTSltXTGzoAjv2tAZimsqPPfROWEljDhtjHYeb89RkCONqMvZQOH42pCMonch3jlTKi0kpor7g254LWoyfsyd3TdqGuD12pA',
    #     #     'expires_in': 7200
    #     # }
    #
    def test_get_token2(self):
        """
        传入params参数
        """
        url = f'{self.base_url}/cgi-bin/gettoken'
        SECRET = '-O1EaM2IcBxVPmSsEKPiDM_g1ymA_AIdSJjCzsPMV1M'
        ID = 'wwaba5e80f616dd925'
        params = {
            "corpid": SECRET,
            "corpsecret": ID
        }
        r = requests.get(url=url,params=params)
        print(r.json())
