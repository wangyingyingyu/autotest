

# import json
#
# # 定义一个Python字典
# data = {
#     "name": "Alice",
#     "age": 30,
#     "city": "New York"
# }
#
# # 将Python字典序列化为JSON格式的字符串
# json_str = json.dumps(data)
# print(json_str)
# print(type(json_str))
# for i in dict(json_str):
#     print(i)
# # - 如果您希望遍历原始字典，请直接遍历 `data`。
# # - 如果您希望遍历 JSON 字符串，需先使用 `json.loads()` 将其转换为字典。
# # 将 Python 字典序列化为 JSON 并写入文件
# with open('data.json', 'w') as json_file:
#     json.dump(data, json_file, indent=4)  # 使用缩进格式化 JSON 输出
#
# print("数据已成功写入 data.json 文件。")

b = max(6,7)
print(b)