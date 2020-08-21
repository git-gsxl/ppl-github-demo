# coding:utf-8
import json
import requests


class Base_api():
    '''
    1.默认只需要传url和参数
    2.微信的accesss_token可在headers加入
    3.request 的参数可以直接用**kwargs传入
    '''
    s = requests.session()

    def post(self, url, body=None, headers={}, method='post', token='', **kwargs):
        if type(body) == str:
            headers['Content-Type'] = 'application/x-www-form-urlencoded'
            my_type = 'params'
        else:
            headers['Content-Type'] = 'application/json'
            headers['X-Requested-With'] = 'XMLHttpRequest'
            body = json.dumps(body)
            my_type = 'json'

        if len(token) > 1:
            body = body.replace('$token', token)  # 替换token

        res = self.s.request(method=method,
                             url=url,
                             params=body,
                             headers=headers,
                             data=body,
                             **kwargs
                             )
        print("请求方式：%s, 请求url:%s" % (method, url))
        print("请求头参数为：%s" % headers)
        print("请求类型为：%s ,body参数为：%s" % (my_type, body))
        print('decode响应信息为：', res.content.decode("utf-8"))
        return res

    def get(self, url, body=None, headers={}, method='get', **kwargs):
        res = self.s.request(method=method,
                             url=url,
                             params=body,
                             headers=headers,
                             data=body,
                             **kwargs
                             )
        print("请求方式：%s, 请求url:%s" % (method, url))
        print('decode响应信息为：', res.content.decode('utf-8'))
        return res
