"""
# 遍历字典时默认遍历key值
# 同时遍历key值和value值有两种方法
课堂练习
创建一个字典，包含以下信息：
姓名（name）
年龄（age）
性别（gender）
城市（city）
添加新的键值对：
国家（country）: “中国”
职业（job）: “软件工程师”
删除字典中的“年龄”项。
检查字典中是否存在“性别”这一键，并输出其对应的值。
遍历字典，打印出所有的键和对应的值。
"""
dict = {'name':'Tom','age':20,'gender':'man','city':'shanghai'}
#dict['country'] = '中国'
#dict['job'] = '软件工程师'

new = {'country':'中国','job':'软件工程师'}
dict.update(new)
print(dict)
# 删除年龄
#dict.pop('age')
del dict['age']
print(dict)
print(dict.values())

print(dict.get('gender'))
for i in dict.items():
    print(i)
for i ,j in dict.items():
    print(i,j)