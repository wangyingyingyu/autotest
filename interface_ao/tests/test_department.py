import allure
import pytest

from interface_ao.apis.contacts.departments import Departments
from interface_ao.utils.utils import Utils


@allure.epic("企业微信接口测试")
@allure.feature("通讯录管理")
class TestDepartment:

    def setup_class(self):
        self.depart=Departments()
    @allure.story("部门管理")
    @allure.title("添加部门")
    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("create"),
                             ids=["id:2-添加广州研发中心，父id为1", "必填参数name为空", "必填参数父id为空",
                                  "id:3-添加北京研发中心，父id为1", "id:4-添加上海研发中心，父id为1"])
    def test_create(self,data,expect):
        with allure.step("调用创建部门信息接口"):
            r=self.depart.create(data)
        with allure.step("断言创建部门是否符合预期"):
            assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("update"),
                             ids=["更新广州研发中心的英文简称", "更新北京研发中心的英文简称",
                                  "更新上海研发中心的英文简称，父id为2"])
    def test_update(self,data,expect):
        with allure.step("调用更新部门信息接口"):
            r=self.depart.update(data)
        with allure.step("断言更新部门是否符合预期"):
            assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("get_list"),
                             ids=["部门ID为1的列表", "不存在部门ID为9的列表", "部门ID为2的列表", "部门ID为4的列表"])
    def test_check(self,data,expect):
        with allure.step("调用查看部门信息接口"):
            r=self.depart.check(data)
        with allure.step("断言查看部门是否符合预期"):
            assert r.json()['errcode'] == expect

    @pytest.mark.parametrize("data,expect", Utils.get_yaml_data("../data/department.yaml").get("delete"),
                             ids=["删除ID为1的根部门", "删除部门ID为2含有子部门的部门", "删除部门ID为3的部门",
                                  "删除部门ID为4的部门","再次删除部门ID为2的部门"])
    def test_delete(self,data,expect):
        with allure.step("调用删除部门信息接口"):
            r=self.depart.delete(data)
        with allure.step("断言删除部门是否符合预期"):
            assert r.json()['errcode'] == expect

