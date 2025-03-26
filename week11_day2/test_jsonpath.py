import jsonpath
import requests
"""课堂练习
测试人论坛的帖子的 json 数据： https://ceshiren.com/t/topic/24002.json
请完成右侧练习
使用 jsonpath 获取该帖子的 title 并断言其包含 为什么要做接口测试
使用 jsonpath 获取发布任务的人的 username 为 lingxi"""

def test_get_jsonpath():
    url = "https://ceshiren.com/t/topic/24002.json"
    r = requests.get(url)

    titles = jsonpath.jsonpath(r.json(),"$..title")
    print(titles)
    assert "为什么要做接口测试" in titles[0]


    # 使用 in 检查整个列表（字符串匹配）
    # 检查 search_str 是否在任意一个 title 中（部分匹配）
    search_str = "为什么要做接口测试"
    assert any(search_str in title for title in titles), f"'{search_str}' 未在 titles 列表中找到"


def test_get_jsonpath2():
    url = "https://ceshiren.com/t/topic/24002.json"
    r = requests.get(url)
    usernames = jsonpath.jsonpath(r.json(),"$..username")
    print(usernames)
    assert "lingxi" == usernames[0]
