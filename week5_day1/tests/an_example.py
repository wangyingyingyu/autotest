# goods_list = []
# name = 'aa'
# good_count = 2
# good_price = 10
# # for i in goods_list:
# #     if name == i["name"]:
# #         i["count"] += good_count
# #         i["total"] += good_count * good_price
# #     else:
# #         good_data = {}
# #         good_data["name"] = name
# #         good_data["count"] = good_count
# #         good_data["price"] = good_price
# #         good_data["total"] = good_count * good_price
# #         goods_list.append(good_data)
# # print(goods_list)
# # 标志变量，表示是否找到了已有商品
# found = False
#
# # 遍历现有商品列表
# for item in goods_list:
#     if name == item["name"]:
#         # 如果商品已经存在，更新数量和总价
#         item["count"] += good_count
#         item["total"] += good_count * good_price
#         found = True
#         break  # 找到后可以提前退出循环
#
# # 如果商品不存在，添加新商品
# if not found:
#     good_data = {}
#     good_data["name"] = name
#     good_data["count"] = good_count
#     good_data["price"] = good_price
#     good_data["total"] = good_count * good_price
#     goods_list.append(good_data)
#
# print(16000+2500+480)
#
#
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Division by zero is not allowed.")
#     return a / b
#
# try:
#     result = divide(10, 0)
# except ValueError as e:
#     print(f"Error occurred: {e}")
# file = open("data.txt","r")
# try:
#     # 写入数据时可能会有问题
#     file.write("写入的数据")
# except IOError as err:
#     print("文件不能写入", err)
#
# file.close()
from week5_day1.src.weather_forecast import Weather
import pytest
def get_yaml():
    weather = Weather()  # 创建 Weather 类的实例
    data_weather = weather.read_weather()  # 通过实例调用 read_weather()
    d = []
    for i in data_weather:
        d.append(i)
    return d

print(get_yaml())





