'''
data:excel配置文件；
num：环境选择，如外网/测试环境等；
dic_body：请求参数转为字典格式；
get_token：获取登录token
'''
import os, requests, json, sys

cur_path = os.path.dirname(os.getcwd())
sys.path.append(cur_path)

from unittest_demo.api_package.common.excel import Excel

data = Excel(os.path.join(os.path.dirname(os.getcwd()
                                          ), 'cases', 'api_excel.xls'), '配置文件').dict_data()
num = int(data[0]['type'])
url = data[num]['host'] + data[num]['url']
dic_body = json.loads(data[num]['body'])
s = requests.session()


def token():
    ''' 获取登录token '''
    try:
        res = s.post(url, json=dic_body)
        dic = json.loads(res.content.decode("utf-8"))
        return dic['data']['token']

    except:
        return ''

