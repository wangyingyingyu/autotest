import requests
import pytest
import allure
import jsonpath

class TestQiYeWeiXin:
    def setup_class(self):
        self.base_url = "https://qyapi.weixin.qq.com"
        url = f'{self.base_url}/cgi-bin/gettoken'
        SECRET = '-O1EaM2IcBxVPmSsEKPiDM_g1ymA_AIdSJjCzsPMV1M'
        ID = 'wwaba5e80f616dd925'
        params = {
            "corpid": ID,
            "corpsecret": SECRET
        }
        r = requests.request(method="GET",url=url, params=params)
        self.token = r.json()["access_token"]
        print(r.json())

    def test_create_department(self):
        """
        创建部门
        最后更新：2023/08/15
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/create?access_token=ACCESS_TOKEN

        请求包体{
           "name": "广州研发中心",
           "name_en": "RDGZ",
           "parentid": 1,
           "order": 1,
           "id": 2
        }
        """
        url = f'{self.base_url}/cgi-bin/department/create'
        params = {
            "access_token": {self.token}
        }
        json = {
           "name": "北京研发中心",
           "name_en": "BJYFZX",
           "parentid": 1,
           "order": 1,
           "id": 2
        }
        # r = requests.request(method="POST", url=url, params = params,json=json)
        r = requests.post(url=url,json=json,params=params)
        print(r.json())


