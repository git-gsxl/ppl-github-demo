# coding:utf-8
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))                # 添加至环境变量
from api_package.api.api_login import Login_api
from api_package.common.sql import send_sql


class TestLogin:

    def test_register(self):
        sql = "delete from UserInfo where username='gsxl11';"
        send_sql(sql)
        res = Login_api().register()
        assert '恭喜您，账号已成功注册' == res.text

    def test_register1(self):
        res = Login_api().register()
        assert '该用户名已被注册，请更换用户名' == res.text

    def test_login(self):
        res = Login_api().login()
        assert '欢迎您：admin' in res.text

    def test_login1(self):
        res = Login_api().login(user='')
        assert '请输入用户名' in res.text
