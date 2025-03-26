import requests
import pytest
import allure
import jsonpath

"""实战：电子商城接口自动化测试
完成商品管理 API 自动化测试
编写新增商品接口测试用例
编写查询商品接口测试用例
编写删除商品接口测试用例"""
@allure.epic("Litemall电子商城接口自动化")
@allure.feature("商品管理")
class TestLiteMall:
    def setup_class(self):
        self.base_url = "https://litemall.hogwarts.ceshiren.com/admin"
        self.headers = {'X-Litemall-Admin-Token': '2f9f787c-d298-4f6c-ab29-9adb3b730822'}

    @pytest.mark.P0
    @allure.story("登录页面")
    @allure.title("获取Token-冒烟用例")
    def test_login(self):
        """
        备注：X-Litemall-Admin-Token
        使用方法：在每个业务接口的headers中添加token键值对，键为“X-Litemall-Admin-Token”，值为具体的token值。
        """
        url = f'{self.base_url}/auth/login'
        json = {
            'username':'hogwarts',
            'password':'test12345'
        }
        r = requests.post(url=url,json=json)
        print(r.text)
        print(r.json())
        # print(type(r.text))
        # print(type(r.json()))
        # {'errno': 0,
        #  'data': {
        #      'adminInfo': {'nickName': 'hogwarts','avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'},
        #      'token': '2f9f787c-d298-4f6c-ab29-9adb3b730822'
        #  },
        #  'errmsg': '成功'}
        assert r.json()['errmsg'] == '成功'

    @pytest.mark.P0
    @allure.story("商品上架")
    @allure.title("新增商品-冒烟用例")
    def test_add(self):
        url = f'{self.base_url}/goods/create'

        json = {
                "goods":{
                    "picUrl":"",
                    "gallery":[

                    ],
                    "isHot":True,
                    "isNew":True,
                    "isOnSale":True,
                    "goodsSn":"000001",
                    "name":"黄色小番茄",
                    "counterPrice":"10"
                },
                "specifications":[
                    {
                        "specification":"规格",
                        "value":"标准",
                        "picUrl":""
                    }
                ],
                "products":[
                    {
                        "id":111111,
                        "specifications":[
                            "标准"
                        ],
                        "price":10,
                        "number":100,
                        "url":""
                    }
                ],
                "attributes":[
                    {
                        "attribute":"种类",
                        "value":"有机蔬菜"
                    }
                ]
            }
        # 发出 POST 请求，r 接收接口响应
        r = requests.post(url, headers=self.headers,json=json)
        # 打印接口响应
        print(r.headers)  # 打印接口响应的头信息，即返回的响应头信息
        print(r.json())
        assert r.json()['errmsg'] == '成功'

    @pytest.mark.P0
    @allure.story("商品列表")
    @allure.title("查询商品-冒烟用例")
    def test_good_list(self):
        """
        请求方式：GET (HTTP)**
        请求地址：https://litemall.hogwarts.ceshiren.com/admin/goods/list

        参数说明:
        参数	字段类型	是否必填	说明
        goodsSn	字符串	否	商品编号
        name	字符串	否	商品名称
        goodsId	字符串	否	商品ID
        """
        url = f'{self.base_url}/goods/list'
        params = {
            "goodsSn": "000001",
            "name": "黄色小番茄"
        }
        r = requests.get(url=url,params=params,headers=self.headers)
        print(r.text)
        # {
        #     "errno": 0,
        #      "data": {
        #          "total": 1,
        #          "pages": 1,
        #          "limit": 10,
        #          "page": 1,
        #          "list": [{
        #              "id": 1468753,
        #              "goodsSn": "000001",
        #              "name": "黄色小番茄",
        #              "categoryId": 0,
        #              "brandId": 0,
        #              "gallery": [],
        #              "keywords": "",
        #              "brief": "",
        #              "isOnSale": true,
        #              "sortOrder": 100,
        #              "picUrl": "",
        #              "isNew": true,
        #              "isHot": true,
        #              "unit": "’件‘",
        #              "counterPrice": 10.00,
        #              "retailPrice": 10.00,
        #              "addTime": "2025-03-26 03:19:48",
        #              "updateTime": "2025-03-26 03:19:48",
        #              "deleted": false}]
        #      },
        #      "errmsg": "成功"}
        res = jsonpath.jsonpath(r.json(), '$.data.list[0].name')
        print(res)
        assert res[0] == "黄色小番茄"

    @pytest.mark.P0
    @allure.story("商品列表")
    @allure.title("删除商品-冒烟用例")
    def test_delete_good(self):
        """
        请求方式：POST(HTTP)
        请求地址：https://litemall.hogwarts.ceshiren.com/admin/goods/delete
        "id": "1468727"
        """
        url = f'{self.base_url}/goods/delete'
        json = {
            "id":"1468753"
        }

        r = requests.post(url=url,json=json,headers=self.headers)
        # print(r.text)
        print(r.json())
        # "errmsg":"成功"
        assert r.json()["errmsg"] == "成功"



