from api_package.common.base import Base_api
from api_package.common.config import host
import re


class HomeApi(Base_api):

    def add_project(self, name='hrun1', _name='广深小龙', **kwargs):
        url = host()+'/api/add_project/'
        body = {"project_name": name,
                "responsible_name": _name,
                "test_user": "K、J、L",
                "dev_user": "D",
                "publish_app": "hrun_web",
                "simple_desc": "hrun_web",
                "other_desc": "hrun_web"}

        res = self.post(url, body, **kwargs)
        return res

    def select_list(self, **kwargs):
        url = host()+'/api/project_list/1/'
        res = self.get(url, **kwargs).text
        try:
            r = re.findall("invalid\('(.+?)'\)", res)
            idName = int(r[0])
        except:
            idName=''
        return idName

    def del_project(self, id, **kwargs):
        url = host()+'/api/project_list/1/'
        body = {"id": id, "mode": "del"}
        res = self.post(url, body, **kwargs)
        return res
