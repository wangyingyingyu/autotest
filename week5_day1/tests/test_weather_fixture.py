from week5_day1.src.weather_forecast import Weather
import pytest

def get_yaml():
    weather = Weather()  # 创建 Weather 类的实例
    data_weather = weather.read_weather()  # 通过实例调用 read_weather()

    # 这里假设 data_weather 是一个字典，包含城市名的键
    city_list = list(data_weather.keys())  # 获取字典的键，以获得城市名称列表
    return city_list
"""测试要求：
Pytest 标记测试用例：使用 @pytest.mark 对不同场景的测试进行标记，区分正常情况和异常情况。
Pytest 设置跳过、预期失败用例：对一些特定的测试用例进行跳过（例如，查询未来天气的用例），
使用 @pytest.mark.skip 和 @pytest.mark.xfail 设置跳过或预期失败的用例。
Pytest 异常处理：测试查询不存在城市或日期的情况，验证异常是否按照预期抛出。
Pytest 结合数据驱动-yaml：使用 YAML 文件提供不同的城市和日期数据，进行参数化测试。"""


def setup_modul():
    print("模块测试开始")

def teardown_modul():
    print("模块测试结束")

class TestWeather:
    def setup_class(self):
        self.weather = Weather()
        self.weather.write_weather()
        print("类测试开始")

    def teardown(self):
        print("类测试结束")

    def setup_method(self):
        print("方法测试开始")

    def tear_down(self):
        print("方法测试结束")


    @pytest.mark.current
    @pytest.mark.parametrize("city_name, expected", [
        ("Shanghai", {'humidity': 61, 'temp': 24, 'windspeed': 12}),
        ("Beijing", {'humidity': 66, 'temp': 24, 'windspeed': 15})
    ], ids=['shanghai', 'beijing'])
    def test_current_weather(self, city_name, expected,):
        assert self.weather.get_current_weather(city_name) == expected

    @pytest.mark.history
    @pytest.mark.skip(result='输入城市名称不正确')
    def test_history_weather(self):
        expected = {'humidity': 66, 'temp': 24, 'windspeed': 15}
        assert self.weather.history_weather("shanghai", "2023-10-01") == expected

    @pytest.mark.xfail
    def test_history_weather(self):
        expected = {'humidity': 60, 'temp': 20, 'windspeed': 10}
        assert self.weather.history_weather("Beijing", "2023-10-01") == expected



    @pytest.mark.parametrize("city", ['Beijing', 'Shanghai'])
    def test_show_weather(self,city,weather_data):
        expected_results = weather_data[city]

        actual_result = self.weather.show_weather(city)  # 调用方法获取天气信息
        assert actual_result == expected_results  # 断言比较结果









