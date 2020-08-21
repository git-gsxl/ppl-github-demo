# coding:utf-8
import os, sys, unittest
sys.path.append(os.path.dirname(os.getcwd()))                                  # 添加至环境变量
from web_package.pages import page_home, page_login
from web_package.common.config import url, is_driver
url = url()


class Test_home(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = is_driver()
        cls.driver.get(url['host']+url['login_url'])
        cls.login = page_login.Login(cls.driver).login()
        cls.home = page_home.Home(cls.driver)

    @ classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_add(self):
        self.home.add_projects()
        res = self.home.exp()
        print("检查点---->：%s" % res)
        self.assertFalse(res)

    def test_del(self):
        self.home.del_project()
        res = self.home.exp()
        print("检查点---->：%s" % res)
        self.assertTrue(res)


if __name__ == '__main__':
    unittest.main()
