# coding:utf-8
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))                                  # 添加至环境变量
from web_package.pages.page_login import Login
from web_package.common.sql import send_sql


class TestLogin:
    def test_register(self, driver):
        sql = "delete from UserInfo where username='gsxl11';"
        send_sql(sql)
        res = Login(driver).register()
        print("检查点---->：%s" % res)
        assert res

    def test_register1(self, driver):
        res = Login(driver).register(user='gsxl')
        print("检查点---->：%s" % res)
        assert res is False

    def test_login(self, driver):
        res = Login(driver).login()
        print("检查点---->：%s" % res)
        assert res

    def test_login1(self, driver):
        res = Login(driver).login(user='asdasdasd')
        print("检查点---->：%s" % res)
        assert res is False
