import allure
import pytest
import requests
import jsonpath
"""
实战
设计接口测试用例
编写查找宠物主人的接口自动化测试用例
查询所有的宠物主人，断言响应状态码
查询所有宠物主人的城市，断言所有城市中包含“nanjing”
查询名字为"Black"的宠物主人，断言响应状态码
查询不存在的宠物主人，断言响应状态码"""

@allure.epic("宠物医院")
@allure.feature("搜索功能")
class TestPetClinic:

    def setup_class(self):
        self.url = "https://spring-petclinic-rest.k8s.hogwarts.ceshiren.com/petclinic/api/owners"

    @pytest.mark.P0
    @allure.story("Owner搜索")
    @allure.title("搜索全部主人")
    def test_search_all(self):
        """
        查询所有宠物主人，断言响应状态码
        """
        r = requests.get(self.url, verify=False)

        """
        [{'firstName': 'George',
         'lastName': 'Franklin', 
         'address': '110 W. Liberty St.', 
         'city': 'Madison', 'telephone': '6085551023',
          'id': 1, 'pets': []}, 
        {'firstName': 'Betty', 
        'lastName': 'Davis',
         'address': '638 Cardinal Ave.',
          'city': 'Sun Prairie', 
          'telephone': '6085551749',
           'id': 2, 
           'pets': [{'name': 'Basil', 'birthDate': '2012-08-06', 'type': {'name': 'hamster', 'id': 6}, 'id': 2, 'ownerId': 2, 'visits': []}]}, 
        """

        # 查询所有的宠物主人
        owners_firstname = [c["firstName"] for c in r.json()]
        owners_lastname = [c["lastName"] for c in r.json()]
        full_names = [f"{first} {last}" for first, last in zip(owners_firstname,owners_lastname)]
        print(full_names)

        # ['George Franklin', 'Betty Davis', 'Eduardo Rodriquez', 'Harold Davis', 'Peter McTavish', 'Jean Coleman',
        #  'Jeff Black', 'Maria Escobito', 'David Schroeder', 'Carlos Estaban', 'George Franklin', 'Bushi Runner',
        #  'Bushi Rapper', 'Bushi Joker', 'Bushi test', 'Bushi test', 'test Tester', 'test Tester', 'Li qiang',
        #  'George Franklin', 'George Franklin', 'George Franklin', 'George Franklin', 'George Franklin', 'Fu Lifang',
        #  'Liu Ruiqin', 'Liu Ruiqin', 'Liu Ruiqin', 'Liu Ruiqin', 'Fu Lifang', 'Wang Xiucai', 'Hou mengkai',
        #  'George Franklin', 'Wu yifan', 'George Franklin', 'Chen Junhao', 'Hou mengkai', 'cai xukun', 'Wu yifan',
        #  'Zhang Yanmeng', 'IKUN IKUN', 'Zhang Yanmeng', 'chen chen', 'sad yiasdasdasd', 'Luo Kaiyue', 'George Franklin',
        #  'George Franklin', 'George Franklin', 'Hou Mengkai', 'George Franklin', 'George Franklin', 'zz Yanmeng',
        #  'feng yiZhe', 'feng yiZhe', 'feng yiZhe', 'Cai Xunkun', 'cai xukun', 'George Franklin', 'George Franklin',
        #  'George Franklin', 'George Franklin', 'cai xukun', 'George Franklin', 'George Franklin', 'zz Yanmeng',
        #  'Fu Lifang', 'Fulifang Franklin', 'George Franklin', 'tony black']

        #print(r.text)
        assert r.status_code == 200
    @pytest.mark.P0
    @allure.story("Owner搜索")
    @allure.title("搜索宠物主人的城市")
    def test_city(self):
        """
        查询所有宠物主人的城市，断言包含nanjing
        """
        r = requests.get(self.url, verify=False)
        # 所有城市
        w = [c["city"] for c in r.json()]
        print(w)
        assert "beijing" in w

        # ['Madison', 'Sun Prairie', 'McFarland', 'Windsor', 'Madison', 'Monona', 'Monona', 'Madison', 'Madison',
        #  'Waunakee', 'Madison', 'Madison', 'Madison', 'Madison', '33', '22', 'Madison', 'Madison', 'Zhengzhou',
        #  'Madison', 'Madison', 'Madison', 'Madison', 'Madison', 'Zhengzhou', 'Zhengzhou', 'Zhengzhou', 'Zhengzhou',
        #  'Zhengzhou', 'Zhengzhou', 'Zhengzhou', 'Madison', 'Madison', 'zz', 'chinese', 'Madison', 'Fugou', 'Madison',
        #  'zz', 'Zhengzhou', 'city', 'Zhengzhou', 'zhengzhou', 'zz', 'ZhengZhou', 'Madison', 'Madison', 'Madison',
        #  'Fugou', 'Madison', 'Madison', 'zz', 'zhengZhou', 'zhengZhou', 'zhengZhou', 'Zhengzhou', 'lizhi', 'Madison',
        #  'Madison', 'Madison', 'Madison', 'lizhi', 'Madison', 'Madison', 'zz', 'zhengzhou', 'Madison', 'Madison',
        #  'beijing']

    @pytest.mark.P0
    @allure.story("Owner搜索")
    @allure.title("搜索已存在的主人")
    def test_owner(self):
        """
        查询名字为"Black"的宠物主人，断言响应状态码
        """

        params = {
            "lastName": "Black"
        }
        r = requests.get(self.url, verify=False, params=params)
        print(r.text)
        assert r.status_code == 200

        # [{"firstName": "Jeff", "lastName": "Black", "address": "1450 Oak Blvd.", "city": "Monona",
        #   "telephone": "6085555387", "id": 7, "pets": [
        #         {"name": "Lucky", "birthDate": "2011-08-06", "type": {"name": "bird", "id": 5}, "id": 9, "ownerId": 7,
        #          "visits": []}]},
        #  {"firstName": "tony", "lastName": "black", "address": "beijing", "city": "beijing", "telephone": "1234",
        #   "id": 186, "pets": []}]

    @pytest.mark.P1
    @allure.story("Owner搜索")
    @allure.title("搜索不存在主人")
    def test_not_owner(self):
        """
        查询不存在的宠物主人，断言响应状态码
        """
        params = {
            "lastName": "Tom"
        }
        r = requests.get(self.url,verify=False,params=params)
        print(r.status_code)

        assert r.status_code == 404




