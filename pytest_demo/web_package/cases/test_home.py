# coding:utf-8
import os, sys
sys.path.append(os.path.dirname(os.getcwd()))                                  # 添加至环境变量
from web_package.pages import page_home


class TestHome:
    def test_add(self, login):
        driver = login
        home = page_home.Home(driver)
        home.add_projects()
        res = home.exp()
        print("检查点---->：%s" % res)
        assert res is False

    def test_del(self, login):
        driver = login
        home = page_home.Home(driver)
        home.del_project()
        res = home.exp()
        print("检查点---->：%s" % res)
        assert res
