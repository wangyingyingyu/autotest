# def count_pairs(lst):
#     # 初始化一个字典来存储每种元素的成对数
#     pairs_count = {}
#
#     # 从第二个元素开始遍历（如果有的话）
#     for i in range(1, len(lst)):
#         # 如果当前元素和前一个元素相同，则进行计数
#         if lst[i] == lst[i - 1]:
#             # 如果这个元素以前已经成对出现过，那么就在原来的基础上加1
#             if lst[i] in pairs_count:
#                 pairs_count[lst[i]] += 1
#             else:
#                 # 如果是首次发现成对，初始化为1对
#                 pairs_count[lst[i]] = 1
#
#     return pairs_count
#
#
# # 示例列表
# example_list = ['a', 'a', 'a', 'b', 'c', 'c', 'd', 'd', 'd']
#
# # 调用函数并打印结果
# result = count_pairs(example_list)
# print(result)  # 应输出：{'a': 2, 'c': 1, 'd': 2}
import yaml
with open('./data/example.yaml','r',encoding='utf-8') as f:
    data = yaml.safe_load(f)
print(data)

result = {'create': [
    [{'name': '广州研发中心', 'name_en': 'GZYFZX', 'parentid': 1, 'order': 1, 'id': 2}, 0],
    [{'name': '', 'name_en': 'JISHU2', 'parentid': 1, 'order': 3, 'id': 3}, 40058],
    [{'name': '南京研发中心', 'name_en': 'NJYFZX', 'parentid': None, 'order': 3, 'id': 3}, 60004],
    [{'name': '北京研发中心', 'name_en': 'BJYFZX', 'parentid': 1, 'order': 2, 'id': 3}, 0],
    [{'name': '上海研发中心', 'name_en': 'SHYFZX', 'parentid': 1, 'order': 1, 'id': 4}, 0]
]}

