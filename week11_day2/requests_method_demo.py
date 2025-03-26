# 课堂练习
# 演练环境：https://httpbin.ceshiren.com/
# 使用 requests 对演练环境发起 get 请求并打印响应信息
# 使用 requests 对演练环境发起 post 请求并打印响应信息
# 使用 requests 对演练环境发起 put 请求并打印响应信息
# 使用 requests 对演练环境发起 delete 请求并打印响应信息
import requests
import jsonpath
# 基础url
base_url = "https://httpbin.ceshiren.com"
# 发起requests.get请求并打印详细信息
def test_get():
    url = f'{base_url}/get'
    r = requests.get(url)
    print(r.text)

    #assert r.url == "https://httpbin.ceshiren.com/get"
    assert r.status_code == 200
# 使用requests对演练环境发起post请求并打印响应信息
def test_post():
    url = f'{base_url}/post'
    r = requests.post(url)
    print(r.text)

    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/post"

def test_put():
    url = f'{base_url}/put'
    r = requests.put(url)
    print(r.text)

    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/put"
# 发起delete请求并打印响应信息
def test_delete():
    url = f'{base_url}/delete'
    r = requests.delete(url)
    print(r.text)
    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/delete"


# 添加请求参数，直接在url中拼接
def test_get_demo1():
    url = f'{base_url}/get?name=Tom&hobby=dancing,reading'
    r = requests.get(url)
    print(r.text)

    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/get?name=Tom&hobby=dancing,reading"
# 添加请求参数，使用params形式添加请求参数到请求url中
def test_get_params():
    url = f'{base_url}/get'
    params = {
        'name':'Tom',
        'hobby':'dancing,reading'
    }
    r = requests.get(url=url,params=params)
    print(r.text)
    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/get"

# headers构造请求头信息
def test_send_headers():
    url = f'{base_url}/get'
    headers = {
        'Introduce-Myself':'dancing-reading',
        "User-Agent": "/hhhhh"
    }
    r = requests.get(url=url,headers=headers)
    print(r.text)
    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/get"


# 课堂练习
# 简历系统只接收 JSON 格式请求
# 帮小明发送简历到演练环境 post 接口
# 演练环境：https://httpbin.ceshiren.com
def test_json():
    url = f'{base_url}/post'
    json = {
        "name": "xiaoming",
        "gender": "male",
        "mail":"24786812512@qq.com",
        "address":{
            "province":"北京市",
            "city":"北京市",
            "distinct":"昌平区"
        },
        "skills":{
            "python": "熟练",
            "pytest": "熟练",
            "allure": "熟练",
            "selenium": "熟练",
            "appium": "熟练",
        }
    }
    r = requests.post(url=url,json=json)
    print(r.text)
    print(r.json())
    assert r.status_code == 200
    assert r.url == "https://httpbin.ceshiren.com/post"
# 响应是json响应，如果打印.text文本信息，会出现编码形式的结果，如果要打印json格式的
#响应信息，必须使用.json方法将json响应信息转换成python格式的响应信息


"""课堂练习
对小明提交的简历的进行断言
断言小明现在在北京市
断言小明所在的区是昌平区
断言小明熟练使用 pytest
断言小明熟练使用 selenium
断言小明熟练使用 appium"""
def test_assert_json():
    url = f'{base_url}/post'
    json = {
        "name": "xiaoming",
        "gender": "male",
        "mail": "24786812512@qq.com",
        "address": {
            "province": "北京市",
            "city": "北京市",
            "distinct": "昌平区"
        },
        "skills": {
            "python": "熟练",
            "pytest": "熟练",
            "allure": "熟练",
            "selenium": "熟练",
            "appium": "熟练",
        }
    }
    r = requests.post(url=url, json=json)
    print(r.text)
    print(r.json())



    # assert r.json()["json"]["address"]["province"] == "北京市"
    # assert r.json()["json"]["skills"]["distinct"] == "昌平区"
    # assert r.json()["json"]["skills"]["python"] == "熟练"
    # assert r.json()["json"]["skills"]["selenium"] == "熟练"
    # assert r.json()["json"]["skills"]["appium"] == "熟练"

# jsonpath.jsonpath返回值是一个列表
def test_assert_jsonpath():
    url = f'{base_url}/post'
    json = {
        "name": "xiaoming",
        "gender": "male",
        "mail": "24786812512@qq.com",
        "address": {
            "province": "北京市",
            "city": "北京市",
            "distinct": "昌平区"
        },
        "skills": {
            "python": "熟练",
            "pytest": "熟练",
            "allure": "熟练",
            "selenium": "熟练",
            "appium": "熟练",
        }
    }
    r = requests.post(url=url, json=json)
    print(r.text)
    print(r.json())

    # 断言 jsonpath返回值是一个列表[]   jsonpath.jsonpath(r.json(), "jsonpath表达式")
    res = jsonpath.jsonpath(r.json(),"$..province")[0]
    print(res)
    assert res == "北京市"

    res = jsonpath.jsonpath(r.json(), "$..allure")[0]
    print(res)
    assert res == "熟练"




