# a = [123]
# # 转换第一个元素为字符串并打印第一位元素
# print(str(a[0])[0])
a = '123'
print(a[0])
stu = {'name': 'Tom', 'age': 23, 'gender': 'male', 'address': 'BeiJing'}
# print(stu["name"])
# print(stu["hobby"])
print(stu.get("name"))
print(stu.get("hobby"))
print(stu.get("name","无数据"))

stu_management = {
    'aa': {'name':'aa', 'math':90},
    'bb':{'name':'bb', 'math':91},
    'cc':{'name':'cc', 'math':98}
}

hh = stu_management['aa']['math']
print(hh)



