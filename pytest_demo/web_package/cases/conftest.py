import sys, pytest, time
from selenium import webdriver
from unittest_demo.web_package.pages.page_login import Login

@pytest.fixture(scope="session")
def driver(request, no_ui=False):
    '''只打开浏览器和关闭浏览器'''
    if 'linux' in sys.platform:
        option = webdriver.ChromeOptions()
        option.add_argument('headless')                 # 浏览器不提供可视化页面
        option.add_argument('no-sandbox')               # 以最高权限运行
        option.add_argument('--start-maximized')        # 最大化运行（全屏窗口）设置元素定位比较准确
        option.add_argument('--disable-gpu')            # 谷歌文档提到需要加上这个属性来规避bug
        # option.add_argument('--window-size=1920,1080')  # 设置浏览器分辨率（窗口大小）
        driver = webdriver.Chrome(options=option)
    else:
        if no_ui:
            ''' win系统下无界面模式 '''
            option = webdriver.ChromeOptions()
            option.add_argument('headless')             # 浏览器不提供可视化页面
            option.add_argument('--start-maximized')    # 最大化运行（全屏窗口）设置元素定位比较准确
            driver = webdriver.Chrome(chrome_options=option)
        else:
            driver = webdriver.Chrome()
            driver.maximize_window()                    # 将浏览器最大化

    def end():
        print("全部用例执行完后 teardown quit dirver")
        time.sleep(2)
        driver.quit()

    request.addfinalizer(end)
    return driver

@pytest.fixture(scope="session")
def login(driver):
    Login(driver).login()
    return driver


