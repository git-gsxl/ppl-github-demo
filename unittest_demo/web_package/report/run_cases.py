'''
这个是优化版执行所有用例发送测试报告，四个步骤
第一步加载用例
第二步执行用例
第三步获取最新测试报告
第四步发送邮箱 （这一步不想执行的话，可以注释掉最后面那个函数就行）
'''
# coding=utf-8
import unittest, time, os, re, sys
# 声明路径
cur_path = os.path.dirname(os.getcwd())
sys.path.append(cur_path)                             # 添加至环境变量
from api_package.common import HTMLTestRunner
import smtplib                                        # 负责发送邮件
from email.mime.text import MIMEText                  # 负责构造邮件的正文
from email.mime.multipart import MIMEMultipart

report_name = u'web自动化测试报告.html'                 # 报告名称
report_title = u'web自动化测试'                        # 报告title名称
report_ename = 'web_report.html'                      # 附件名称
report_path = os.path.join(cur_path, report_name)     # 测试报告目录

def add_case(caseName='cases', rule='test*.py'):
    '''第一步：加载所有的测试用例'''
    case_path = os.path.join(cur_path, caseName)
    if not os.path.exists(case_path):os.mkdir(caseName)     # 如果不存在这个cases文件夹，就自动创建一个
    # 定义 discover 方法的参数，返回测试用例列表文件名
    discover = unittest.defaultTestLoader.discover(case_path,
    pattern=rule,
    top_level_dir=None)
    return discover

def run_case(all_case):
    '''第二步：执行所有的用例, 把结果写入测试报告'''
    report_path = os.path.join(cur_path, report_name)   # 测试报告名称
    print('生成报告目录在:%s' % report_path)
    fp = open(report_path, 'wb')                        # 加载所有用例，写入测试报告，生成
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title=report_title, retry=0)
    runner.run(all_case)                                # 执行
    fp.close()

def get_report_html(report_path):
    '''第三步：获取最新的测试报告'''
    lists = os.listdir(report_path)                     # 获取report目录下的最新测试报告
    lists.sort(key=lambda fn: os.path.getmtime(os.path.join(report_path, fn)))
    print(u'\n最新测试生成的报告： '+cur_path+lists[-1])
    report_file = os.path.join(report_path, lists[-1])  # 找到最新生成的报告文件
    return report_file

def send_mail(sender, pwd, receiver, smtpserver, report_file, port):
    '''发送最新的测试报告内容'''
    with open(report_file, "rb") as f:
        mail_body = f.read()

    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = report_title+u'报告'
    msg["from"] = sender
    if isinstance(receiver, str):
        msg["to"] = receiver
    if isinstance(receiver, list):
        msg["to"] = ','.join(receiver)

    # 加上时间戳，显示报告的内容
    time.strftime('%a, %d %b %Y %H_%M_%S %z')
    msg.attach(body)

    # 邮箱添加附件
    att = MIMEText(open(report_file, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= %s' % report_ename
    msg.attach(att)

    try:
        smtp = smtplib.SMTP()       # 登录邮箱
        smtp.connect(smtpserver)    # 连接邮箱服务器
        smtp.login(sender, pwd)     # 用户名密码

    except:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, pwd)                         # 登录
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('测试报告电子邮件已发送！')

def read_report():
    ''' 判断是否发送邮件，读取报告判断是否存在：Failure、error、还有可能整个文件是空 '''
    ret = []
    with open(report_path, 'rb')as f:
        f = f.read()
        res_Failure = re.findall(b'class="tj failCase">(.+?)<', f)
        res_error = (re.findall(b'errorCase">(.+?)</span>', f))
        res_null = (re.findall(b'tj passCase">Pass</span>(.+?)</p>', f))
        for i in res_error:
            ret.append(i)
        for i in res_Failure:
            ret.append(i)
        for i in res_null:
            try:
                if int(i):
                    return True
            except:pass
    return False

if __name__ == "__main__":
    all = add_case()   # 加载用例
    run_case(all)      # 执行用例

    report_file = get_report_html(os.path.join(cur_path))      # 获取最新测试报告路径

    # 邮箱配置
    sender = 'xxx@qq.com'
    pwd = 'xxxxxxxxxxxxxxxx'         # SSL授权码登录
    smtp_server = 'smtp.qq.com'
    port = 465
    receiver = ['772262624@qq.com']  # 可多个邮箱传list对象

    # 判断报告是否有错误，有错误就发送邮件
    ret = read_report()
    if ret == False:
        send_mail(sender, pwd, receiver, smtp_server, report_file, port)
    elif not ret:
        send_mail(sender, pwd, receiver, smtp_server, report_file, port)
    else:print('用例全部通过，不需要发送邮件')
