from week5_day4.src.student_manage_system import Student
import pytest
import yaml
def setup_module():
    print('学生信息管理打开')
def teardown():
    print('学生管理系统关闭')
#
data = [('01','Tom',18,'male','学生Tom信息已修改'),
        ('02','Eve',19,'female','学生Eve信息已修改'),
        ('03','David',20,'male','学生David信息已修改')]
def write_yaml():
    with open('../data/stu_data.yaml','w',encoding='utf-8') as file:
        yaml.safe_dump(data,file,allow_unicode=True)
write_yaml()
def get_yaml():
    with open('../data/stu_data.yaml', 'r',encoding='utf-8') as file:
        return yaml.safe_load(file)


"""测试需求
第一步 - 完成学生管理系统代码的编写。 
      - 使用 pytest 编写增加、修改、查询（id和name）、删除（id和name）学生的测试用例 
      - 使用标签为测试用例制定合适的优先级。 
      - 实现增加学生用例的参数化 - 生成 allure 报告。
第二步
针对增加学生的测试用例使用yaml实现数据驱动。
第三步
使用fixtrue 完善学生修改的测试用例 前置步骤为添加学生，后置步骤为删除学生。"""

class TestStudent:
    def setup_class(self):
        print("类测试开始")
    def tear_down(self):
        print('类测试结束')
    def setup_method(self):
        self.student = Student()
        print("方法测试开始")
    def teardown_method(self):
        print("方法测试结束")

    @pytest.mark.P0
    @pytest.mark.parametrize("id,name,age,sex,result",[('01','Tom',18,'male','学生Tom已添加'),
                                                       ('02','Eve',19,'female','学生Eve已添加'),
                                                       ('03','David',20,'male','学生David已添加')],
                             ids=['01','02','03'])
    def test_add(self,id,name,age,sex,result):
        assert self.student.add(id,name,age,sex) == result
    # @pytest.mark.parametrize("id,name,age,sex,result",[('01','Tom',19,'male','学生Tom信息已修改'),
    #                                                    ('02','Eve',20,'female','学生Eve信息已修改'),
    #                                                    ('03','David',21,'male','学生David信息已修改')],
    #                          ids=['01-Tom','02-Eve','03-David'])
    @pytest.mark.parametrize("id,name,age,sex,result",get_yaml(),ids=['01-Tom','02-Eve','03-David'])
    def test_update(self,add_stu,id,name,age,sex,result):

        assert add_stu.update(id, name, age, sex) == result

    @pytest.mark.P0
    @pytest.mark.parametrize("id,result",[('01','学生Tom信息已删除'),('02','学生Eve信息已删除')],
                              ids=['Tom','Eve'])
    def test_delete_id(self,add_stu,id,result):
        assert add_stu.delete_id(id) == result

    @pytest.mark.parametrize("name,result", [('Tom', '学生Tom信息已删除'), ('Eve', '学生Eve信息已删除')],
                             ids=['Tom', 'Eve'])
    def test_delete_name(self,add_stu, name, result):

        assert add_stu.delete_name(name) == result
    @pytest.mark.P1
    @pytest.mark.parametrize("id,result", [('01','01:Tom age:18,sex:male'), ('02', '02:Eve age:19,sex:female')],
                             ids=['Tom', 'Eve'])
    def test_query_id(self,add_stu, id,result):

        assert add_stu.query_id(id) == result
    @pytest.mark.parametrize("name,result", [('Tom','01:Tom age:18,sex:male'), ('Eve', '02:Eve age:19,sex:female')],
                             ids=['Tom', 'Eve'])
    def test_query_name(self,add_stu, name,result):

        assert add_stu.query_name(name) == result

    def test_stu_info(self):
        self.student.add('01', 'Tom', 18, 'male')
        assert self.student.stu_info() == 'ID: 01, Name: Tom, Age: 18, Sex: male'


