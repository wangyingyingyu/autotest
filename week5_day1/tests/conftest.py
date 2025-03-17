import pytest
@pytest.fixture(scope="module")
def weather():
     print("天气预报")

@pytest.fixture(scope="class")
def weather_class():
    print("地区天气预报")

@pytest.fixture(scope='module')
def weather_data():
    print("测试上海、北京天气")
    # 模拟天气数据
    weather_datas = {
            'Beijing': ("Beijing:{'2023-10-01': {'humidity': 60, 'temp': 20, 'windspeed': 10}, "
                        "'2025-02-10': {'humidity': 60, 'temp': -7, 'windspeed': 10}, "
                        "'today': {'humidity': 66, 'temp': 24, 'windspeed': 15}}"),
            'Shanghai': ("Shanghai:{'2023-10-01': {'humidity': 40, 'temp': 25, 'windspeed': 5}, "
                         "'today': {'humidity': 61, 'temp': 24, 'windspeed': 12}}")
        }

    yield weather_datas







