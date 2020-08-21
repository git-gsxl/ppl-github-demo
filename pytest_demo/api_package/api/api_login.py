from api_package.common.base import Base_api
from api_package.common.config import host


class Login_api(Base_api):

    def register(self, user="gsxl11", email="gsxl11@qq.com", pwd="gsxl11", re_pwd="gsxl11"):
        ''' 注册 '''
        url = host()+'/api/register/'
        body = {"account": user,
                "email": email,
                "password": pwd,
               "repassword": re_pwd}
        res = self.post(url, body)
        return res

    def login(self, user='admin', pwd='123456'):
        ''' 登录 '''
        url = host()+'/api/login/'
        body = 'account=%s&password=%s' % (user, pwd)
        res = self.post(url, body)
        return res
