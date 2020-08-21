# coding:utf-8
import os, sys, unittest, ddt
sys.path.append(os.path.dirname(os.getcwd()))                                  # 添加至环境变量
from web_package.pages.page_login import Login
from web_package.common.config import url, is_driver
from web_package.common.sql import send_sql

login_url = url()['host']+url()['login_url']
# login：参数化数据，断言：1==True  0==False
data_login = [
    {'user': 'gsxl111111', 'pwd': 'gsxl12', 'exp': 0},
    {'user': 'admin', 'pwd': '123456', 'exp': 1},
    {'user': 'and 1=1', 'pwd': 'and 1=2', 'exp': 0}, ]


@ddt.ddt
class TestLogin(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        ''' 前置只执行一次 '''
        cls.driver = is_driver()
        cls.driver.get(login_url)
        cls.b = Login(cls.driver)
        ''' 后置只执行一次，清理注册的账号，确保每次数据正常测试 '''
        sql = "delete from UserInfo where username='gsxl11';"
        send_sql(sql)

    def tearDown(self):
        ''' 后置每个用例后执行一次,回到登录页 '''
        self.driver.get(login_url)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

    def test_register(self):
        res = self.b.register()
        print("检查点---->：%s" % res)
        self.assertTrue(res)

    def test_register1(self):
        res = self.b.register(user='gsxl')
        print("检查点---->：%s" % res)
        self.assertFalse(res)

    @ddt.data(*data_login)
    def test_login(self, data):
        print('login测试数据为：%s' % data)
        user = data['user']
        pwd = data['pwd']
        exp = bool(data['exp'])
        res = self.b.login(user, pwd)
        print("检查点---->：%s" % res)
        self.assertEqual(exp, res)


if __name__ == '__main__':
    unittest.main()
