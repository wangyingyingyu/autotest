# 课堂练习：天气预测系统测试
# 设计一个天气预测系统
import os.path

import yaml


class Weather:
    def __init__(self):
        self.file_name = '../data/weather.yaml'
    def read_weather(self):
        try:
            if not os.path.exists(self.file_name):
                with open(self.file_name,'w'):
                    pass
                return "文件不存在创建文件 weather.yaml"
            else:
                with open(self.file_name,'r') as file:
                    return yaml.safe_load(file)
        except Exception as error:
            print('文件不能读取',error)
    def write_weather(self):
        weather_data = {
                "Beijing": {
                    "2023-10-01": {
                        # 温度
                        "temp": 20,
                        # 湿度
                        "humidity": 60,
                        # 风速
                        "windspeed": 10
                    },
                    "today": {
                        # 温度
                        "temp": 24,
                        # 湿度
                        "humidity": 66,
                        # 风速
                        "windspeed": 15
                    },
                    "2025-02-10": {
                        # 温度
                        "temp": -7,
                        # 湿度
                        "humidity": 60,
                        # 风速
                        "windspeed": 10
                    }
                },
                "Shanghai": {
                    "2023-10-01": {
                        "temp": 25,
                        "humidity": 40,
                        "windspeed": 5
                    },
                    "today": {
                        # 温度
                        "temp": 24,
                        # 湿度
                        "humidity": 61,
                        # 风速
                        "windspeed": 12
                    },
                }

            }
        with open(self.file_name,'w') as file:
            yaml.safe_dump(weather_data,file)
            return
            # 获取当前天气：输入城市名称，返回该城市的当前天气，包括温度、湿度、风速等。
            # 获取历史天气：输入城市名称和日期，返回历史上的天气数据（温度、湿度、风速）。
            # 异常处理：如果查询的城市名无效（不存在），系统应抛出异常。

        # 输入城市的名称字符串
    def get_current_weather(self,city_name):
        data = self.read_weather()

        if city_name in data:
            return data[city_name]["today"]
        else:
            raise ValueError("城市名无效（不存在）")


    def history_weather(self,city_name,date_time):
        data = self.read_weather()

        if city_name in data:
            if date_time in data[city_name]:
                return data[city_name][date_time]
            else:
                return f"没有{city_name}城市{date_time}的天气数据"
        else:
            raise ValueError("城市名无效（不存在）")
    def show_weather(self,name):
        data = self.read_weather()
        return f"{name}:{data[name]}"




# weather = Weather()
# weather.write_weather()
# a = weather.get_current_weather('Shanghai')
# aa = weather.get_current_weather('Beijing')
# b = weather.history_weather('Shanghai','2023-10-01')
# bb = weather.history_weather('Beijing','2023-10-01')
# print(a)
# print(b)
# print(aa)
# print(bb)
# data = weather.read_weather()
#
# d = []
# for i in data:
#     d.append(i)
# print(d)
# for j in d:
#     print(weather.show_weather(j))








