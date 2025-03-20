import pytest

from frame.base.xueqiu_app import XueQiu
from frame.utils.utils import Utils


class TestXueqiu:
    def setup_method(self):
        '''
        1、实例化雪球app实例对象
        2、 用实例对象调用打开app方法和跳转到首页方法
        3、用一个变量接收首页实例对象
        '''
        self.xue_qiu = XueQiu()
        self.page_main = self.xue_qiu.app_start().go_to_main()
    def teardown_method(self):
        self.xue_qiu.app_end()
    # @pytest.mark.parametrize('search_text',["美的"])
    # @pytest.mark.parametrize(
    #     "search_text",
    #     Utils.get_yaml_data(Utils.get_file_path("datas/stock_name.yaml"))
    # )
    # 获取两个 YAML 文件的数据
    stock_names = Utils.get_yaml_data(Utils.get_file_path("datas/stock_name.yaml"))
    result_text = Utils.get_yaml_data(Utils.get_file_path("datas/first_search_text.yaml"))  # 替换为你的第二个 YAML 文件路径

    # 使用 zip 创建一一对应的参数
    params = list(zip(stock_names, result_text))

    @pytest.mark.parametrize("search_text, result_text", params)
    def test_auto_select(self,search_text,result_text):
        '''
        1、跳转到首页
        2、点击搜索框
        3、跳转到搜索页面
        4、在搜索页面搜索框输入文本信息
        5、点击第一个搜索结果（指的是搜索页面的搜索结果）
        6、跳转到搜索结果页面
        7、获取搜索结果文本信息
        5、断言 搜索文本信息是否为预期结果
        '''
        page_result = self.page_main.\
            go_to_search().input_search(input_text=search_text).click_first().\
            go_to_result_page()
        first_ele = page_result.get_first_text()
        selected_list = page_result.click_first_result(search_text=result_text).\
            get_first_result_page().click_add_select().\
            go_back_result_page().go_back_main_page().click_select().\
            click_all().get_all()

        assert first_ele in selected_list

#  cd frame/tests
#  pytest test_xueqiu_search.py --alluredir=./result --clean-alluredir
#  allure serve ./result