import os

import yaml


class Utils:


    @classmethod
    def get_path(cls):
        """
        获取项目绝对路径
        :return:
        """
        path=os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        return path

    @classmethod
    def get_yaml_data(cls, file_path):
        '''
        封装yaml读取
        :param file_path: 文件路径
        :return: 返回yaml数据体
        '''
        with open(file_path, encoding="utf-8") as f:
            datas = yaml.safe_load(f)
        return datas
if __name__ == "__main__":

    a = Utils()
    print(a.get_path())