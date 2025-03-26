import requests
import pytest
import allure
import jsonpath
from week11_day3.utils import Utils


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
    @pytest.mark.parametrize("data,expect",Utils.get_yaml_data("../data/department.yaml").get("create"),
                             ids=["id:2-添加广州研发中心，父id为1","必填参数name为空","必填参数父id为空","id:3-添加北京研发中心，父id为1","id:4-添加上海研发中心，父id为1"])
    def test_create_department(self,data,expect):
        url = f'{self.base_url}/cgi-bin/department/create'
        params = {
            "access_token": {self.token}
        }

        r = requests.post(url=url,json=data,params=params)
        assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("update"),
                             ids=["更新广州研发中心的英文简称","更新北京研发中心的英文简称","更新上海研发中心的英文简称，父id为2"])
    def test_update_department(self,data,expect):
        """
        更新部门
        最后更新：2023/08/15
        请求方式：POST（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/update?access_token=ACCESS_TOKEN

        请求包体（如果非必须的字段未指定，则不更新该字段）：

        {
           "id": 2,
           "name": "广州研发中心",
           "name_en": "RDGZ",
           "parentid": 1,
           "order": 1
        }
        """
        url = f'{self.base_url}/cgi-bin/department/update'
        params = {
            "access_token": {self.token}
        }

        r = requests.post(url=url, json=data, params=params)
        assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("get_list"),
                             ids=["部门ID为1的列表","不存在部门ID为9的列表","部门ID为2的列表","部门ID为4的列表"])
    def test_get_department_list(self,data,expect):
        """
        获取子部门ID列表
        最后更新：2023/09/06
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/simplelist?access_token=ACCESS_TOKEN&id=ID

        参数说明 ：

        参数	必须	说明
        access_token	是	调用接口凭证
        id	否	部门id。获取指定部门及其下的子部门（以及子部门的子部门等等，递归）。 如果不填，默认获取全量组织架构
        """
        url = f'{self.base_url}/cgi-bin/department/simplelist'
        params = {
            "access_token": self.token,
            "id": data['id']
        }

        r = requests.post(url=url, params=params)
        print(r.json())
        assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("delete"),
                             ids=["删除ID为1的根部门","删除部门ID为2含有子部门的部门","删除部门ID为3的部门","删除部门ID为4的部门"])
    def test_delete_department(self,data,expect):
        """
        删除部门
        最后更新：2020/03/30
        请求方式：GET（HTTPS）
        请求地址：https://qyapi.weixin.qq.com/cgi-bin/department/delete?access_token=ACCESS_TOKEN&id=ID
        参数说明 ：
        参数	必须	说明
        access_token	是	调用接口凭证
        id              是	部门id。（注：不能删除根部门；不能删除含有子部门、成员的部门）
        """
        url = f'{self.base_url}/cgi-bin/department/delete'
        params = {
            "access_token": self.token,
            "id": data['id']
        }

        r = requests.post(url=url, params=params)
        assert r.json()['errcode'] == expect


