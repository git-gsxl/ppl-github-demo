from web_package.common.base import Base
from web_package.common.config import url
import time
url = url()

class Login(Base):
    ''' 注册/登录模块 '''

    # 1.注册：
    loc_注册账号 = ('xpath', '//*[@id="account"]')
    loc_注册邮箱 = ('id', 'email')
    loc_注册密码 = ('id', 'password')
    loc_注册密码2 = ('id', 'repassword')
    loc_注册 = ('xpath', '//*[@id="register_form"]/div[5]/input')

    # 2.登录
    loc_账号 = ('id', 'account')
    loc_密码 = ('id', 'password')
    loc_登录 = ('xpath', '//*[@id="login_submit"]')
    loc_res用户名 = ('xpath', '/html/body/div[2]/div[1]/div[1]')
    loc_注销 = ('xpath', '/html/body/div[2]/div[1]/div[1]/a')

    def register(self, user='gsxl11', email='gsxl11@gmail.com', pwd='gsxl12'):
        ''' 注册账号 '''
        self.driver.get(url['host']+url['register_url'])
        self.send(self.loc_注册账号, user)
        self.send(self.loc_注册邮箱, email)
        self.send(self.loc_注册密码, pwd)
        self.send(self.loc_注册密码2, pwd)
        time.sleep(0.2)                     # 操作太快，缓一缓
        self.click(self.loc_注册)
        if self.is_alert():
            print('弹窗处理：确定')
        else:pass
        time.sleep(0.2)                     # 操作太快，缓一缓
        # 注册成功后会回到登录页，所以断言title是否是登录即可
        if self.driver.title == '登录':
            return True
        else:return False

    def login(self, user='gsxl', pwd='gsxl12', q=1):
        ''' t: 默认登录成功后不退出登录，如需登录后退出登录设为：0 '''
        self.driver.get(url['host']+url['login_url'])
        self.send(self.loc_账号, user)
        self.send(self.loc_密码, pwd)
        self.click(self.loc_登录)

        # 断言是否登录成功，首页 get_text 用户名
        res = self.get_text(self.loc_res用户名)
        if user in res:
            if q == 0:
                self.click(self.loc_注销)
            return True
        else:
            return False



