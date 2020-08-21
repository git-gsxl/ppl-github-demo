'''
--类：
    selenium 二次封装
    1.driver:传浏览器driver，如Chrome浏览器运行 webdriver.Chrome()
    2.timeout:元素定位超时时间，默认 8s
    3.poll:获取间隔时间

--方法：
    0.find：单个元素定位：locator = ("id", "id值")
    1.finds：复数元素定位：locator = ("id", "id值")[x]，取第几个？
    2.send：文本输入
    3.click：点击操作
    4.clear：清空文本
    5.text_in_enement：判断 _text 文本值是否 in 定位元素中，返回 bool 值
    6.text_in_enement：
    7.get_enement：判断元素是否存在，返回 bool 值
    8.get_text：获取元素的文本值
    9.now_title：获取当前页面的 title
    10.move_element：鼠标悬停操作，传locator
    11.select_index：index是索引定位第x个，从0开始，默认第1个
    12.select_value：select中的value方法，如html中：value="50"，则value传：50
    13.select_text：select中的text方法全匹配文本，如html中显示：每页显示50条，则文本需全部匹配
    14.switch_iframe：切换iframe：传下标 或 locator
    15.is_alert：
                alert弹窗处理_text：
            --1.默认点击：确定
            --2.取消操作传：取消
            --3.获取弹窗文本传：text
            --4.弹出输入文本传：输入 + 文本值
    16.switch_handle：句柄切换，传int类型，从0开始，-1既是最新打开的一个
    17.js_top：页面滚动条滑动至顶部
    18.js_element：聚焦元素位置,传locator
    19.js_tail：页面滚动条滑动至底部

'''
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():
    '''
    selenium 二次封装
    1.driver:传浏览器driver，如Chrome浏览器运行 webdriver.Chrome()
    2.timeout:元素定位超时时间，默认 8s
    3.poll:获取间隔时间
    '''

    def __init__(self, driver:webdriver.Chrome, timeout=20, poll=1):
        self.driver = driver
        self.timeout = timeout
        self.poll = poll

    def find(self, locator):
        ''' 单个元素定位：locator = ("id", "id值") '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element = WebDriverWait(self.driver, self.timeout, self.poll).until(
                    lambda x: x.find_element(*locator))
                return element
            except:print('元素定位超时，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def finds(self, locator):
        ''' 复数元素定位：locator = ("id", "id值")[x]，取第几个？ '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        try:
            elements = WebDriverWait(self.driver, self.timeout, self.poll).until(
                lambda x: x.find_elements(*locator))
            return elements
        except:
            print('复数定位：元素定位超时，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def send(self, locator, _text):
        ''' 文本输入 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                self.find(locator).send_keys(_text)
            except:print('元素定位超时，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def click(self, locator):
        ''' 点击操作 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                self.find(locator).click()
            except:print('元素定位超时，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def clear(self, locator):
        ''' 清空文本 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                self.find(locator).clear()
            except:print('清空文本发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def text_in_enement(self, locator, _text):
        ''' 判断 _text 文本值是否 in 定位元素中，返回 bool 值'''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                res = WebDriverWait(self.driver, self.timeout, self.poll
                                    ).until(EC.text_to_be_present_in_element(locator, _text))
                return res
            except:
                return False

    def get_enement(self, locator):
        ''' 判断元素是否存在，返回 bool 值 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                self.find(locator)
                return True
            except:
                return False

    def get_text(self, locator):
        ''' 获取元素的文本值 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element_text = WebDriverWait(self.driver, self.timeout, self.poll).until(
                    lambda x: x.find_element(*locator).text)
            except:
                element_text = ''
            return element_text

    def exp_title(self, title=''):
        ''' 断言获取当前页面的 title，完全匹配 返回bool值 '''
        try:
            t = WebDriverWait(self.driver, self.timeout, self.poll).until(EC.title_is(title))
            return t
        except:
            return False

    def move_element(self, locator):
        ''' 鼠标悬停操作 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
              element = self.find(locator)
              ActionChains(self.driver).move_to_element(element).perform()
            except:print('鼠标悬停操作发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def select_index(self, locator, index=0):
        ''' index是索引定位第x个，从0开始，默认第1个 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element = self.find(locator)
                Select(element).select_by_index(index)
            except:print('select中的index方法发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def select_value(self, locator, value):
        ''' select中的value方法，如html中：value="50"，则value传：50 '''

        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element = self.find(locator)
                Select(element).select_by_value(value)
            except:print('select中的value方法-发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def select_text(self, locator, text):
        ''' select中的text方法全匹配文本，如html中显示：每页显示50条，则文本需全部匹配 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element = self.find(locator)
                Select(element).select_by_visible_text(text)
            except:print('select中的text方法-发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def switch_iframe(self, index_locator):
        ''' 切换iframe：传下标 或 locator '''
        try:
            if isinstance(index_locator, int):
                self.driver.switch_to.frame(index_locator)
            elif isinstance(index_locator, tuple):
                element = self.find(index_locator)
                self.driver.switch_to.frame(element)
        except:
            print("iframe切换发生异常：%s" % index_locator)

    def is_alert(self, _text='确定', send_alert=None):
        '''
        alert弹窗处理：
            --1.默认点击：确定
            --2.取消操作传：取消
            --3.获取弹窗文本传：text
            --4.弹出输入文本传：输入 + 文本值
       '''
        try:
            WebDriverWait(self.driver, self.timeout, self.poll).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            if _text == 'text':
                return 'alert获取的文本为：%s' % alert.text
            elif _text == '输入':
                alert.send_keys(send_alert)
                return 'alert弹窗已为您输入文本：%s' % send_alert
            elif _text == '取消':
                alert.dismiss()
                return 'alert弹窗已为您处理：取消'
            else:
                alert.accept()
                return 'alert弹窗已为您处理：确定'
        except:
            return False

    def switch_handle(self, window_name):
        ''' 句柄切换，传int类型，从0开始，-1既是最新打开的一个 '''
        try:
            if not isinstance(window_name, int):
                print('参数类型错误，window_name必须传 int 类型！！！')
            else:
                handlels = driver.window_handles
                self.driver.switch_to.window(handlels[window_name])
        except:print('句柄切换发生错误：%s' % window_name)

    def js_top(self):
        ''' 页面滚动条滑动至顶部 '''
        self.driver.execute_script('window.scrollTo(0,0)')

    def js_element(self, locator):
        ''' 聚焦元素位置 '''
        if not isinstance(locator, tuple):
            print('参数类型错误，locator必须是元祖类型：loc = ("id","value1")')
        else:
            try:
                element = self.find(locator)
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
            except:print('聚焦元素位置-发生异常，定位方式->%s,value值->%s' % (locator[0], locator[1]))

    def js_tail(self):
        ''' 页面滚动条滑动至底部 '''
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

if __name__ == '__main__':
    import time
    driver = webdriver.Chrome()
    b = Base(driver)
    driver.get('https://www.cnblogs.com/gsxl/')
    driver.maximize_window()
    loc_1 = ('xpath', '//*[@id="sidebar_toptags"]/div/ul/li[2]/a')
    b.click(loc_1)
    time.sleep(1)
    b.js_tail()

