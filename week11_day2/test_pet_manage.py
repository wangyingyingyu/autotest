import allure
import pytest
import requests
import jsonpath
"""
作业：宠物商店接口测试
对宠物商店宠物管理接口完成自动化冒烟测试
宠物商店接口文档：https://petstore.swagger.io
对应接口
新增：https://petstore.swagger.io/v2/pet
删除：https://petstore.swagger.io/v2/pet
更新：https://petstore.swagger.io/v2/pet
查询：https://petstore.swagger.io/v2/pet/findByStatus
添加 allure 描述并生成 allure 报告
"""



@allure.epic("宠物商店")
@allure.feature("宠物管理")
class TestPetClinic:

    def setup_class(self):
        self.url = "https://petstore.swagger.io/v2/pet"

    @pytest.mark.P0
    @allure.story("宠物增删减查")
    @allure.title("新增宠物-冒烟用例")
    def test_search_all(self):
        """
        新增宠物信息
        断言宠物分类名为猫
        """
        url = f'{self.url}'
        json = {
          "id": 6,
          "category": {
            "id": 6,
            "name": "猫"
          },
          "name": "咪咪",
          "photoUrls": [
            "string"
          ],
          "tags": [
            {
              "id": 0,
              "name": "狸花猫"
            }
          ],
          "status": "available"
        }
        r = requests.post(url=url, json=json)
        res = jsonpath.jsonpath(r.json(),'$.tags[0].name')
        print(res)
        assert res[0] == '狸花猫'


    @pytest.mark.P0
    @allure.story("宠物增删减查")
    @allure.title("删除宠物-冒烟用例")
    def test_city(self):
        """
        删除宠物信息
        判断删除宠物的名字为咪咪
        https://petstore.swagger.io/v2/pet/6
        """
        url = f'{self.url}/6'

        r = requests.delete(url)
        print(r.text)
        assert r.status_code == 200



    @pytest.mark.P0
    @allure.story("宠物增删减查")
    @allure.title("更新宠物-冒烟用例")
    def test_owner(self):
        """
        更新宠物信息 https://petstore.swagger.io/v2/pet
        更新ID为6的宠物tags名字为 三花猫
        """
        url = f'{self.url}'
        json = {
            "id": 6,
            "category": {
                "id": 6,
                "name": "猫"
            },
            "name": "咪咪",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "三花猫"
                }
            ],
            "status": "available"
        }
        r = requests.put(url=url, json=json)
        res = jsonpath.jsonpath(r.json(), '$.tags[0].name')
        print(res)
        assert res[0] == '三花猫'

    @pytest.mark.P1
    @allure.story("宠物增删减查")
    @allure.title("查询宠物-冒烟用例")
    def test_not_owner(self):
        """

        """
        url = f'{self.url}/6'

        r = requests.get(url)
        print(r.text)
        assert r.status_code == 200
        res = jsonpath.jsonpath(r.json(), '$.tags[0].name')
        print(res)
        assert res[0] == '狸花猫'
