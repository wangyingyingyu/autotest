import requests

from interface_ao.apis.weworks import WeWork


class Departments(WeWork):

    def create(self,data):
        """

        :return:返回创建部门信息请求对象
        """
        seq = {
            "url": f"{self.base_url}/department/create",
            "params": {"access_token": self.token},
             "method": "POST",
            "json": data
        }

        r = self.send(seq)

        return r

    def update(self,data):
        """

        :return:
        """
        seq = {
            "url": f"{self.base_url}/department/update",
            "params": {"access_token": self.token},
            "method": "POST",
            "json": data
        }
        r = self.send(seq)

        return r
    def check(self,data):
        """

        :return:
        """
        seq = {
            "url": f"{self.base_url}/department/simplelist",
            "params": {"access_token": self.token,"id": data['id']},
            "method": "POST"
        }

        r = self.send(seq)
        return r
    def delete(self,data):
        """

        :return:
        """
        seq = {
            "url": f"{self.base_url}/department/delete",
            "params": {"access_token": self.token, "id": data['id']},
            "method": "POST"
        }
        r = self.send(seq)
        return r


