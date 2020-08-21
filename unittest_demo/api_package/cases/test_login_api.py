# coding:utf-8
import unittest,ddt, os, sys
sys.path.append(os.path.dirname(os.getcwd()))                                  # 添加至环境变量
from api_package.common import base
from api_package.common.excel import Excel
from xlrd import open_workbook
from xlutils.copy import copy

tablename = '登录模块'
dir_path = os.path.dirname(os.getcwd())                                        # 获取模块路径
report_path = os.path.join(dir_path, "report", "api_excel测试报告.xls")         # 报告生成路径
filename = os.path.join(dir_path, "cases", "api_excel.xls")                    # 获取excel路径
testdata = Excel(filename, tablename).dict_data()                              # tablename
excel1 = copy(open_workbook(filename, formatting_info=True))                   # 将xlrd的对象转化为xlwt的对象
excel1.save(report_path)                                                       # 每次执行前复制用例

@ddt.ddt
class Test_api(unittest.TestCase):
    @ddt.data(*testdata)
    def test_login_api(self, data):
        res = base.send_requests(data)
        base.wirte_result(res, report_path, tablename)   # res写入保存
        check = data["checkpoint"]
        print("检查点---->：%s" % check)                  # 检查点 checkpoint
        res_text = res["text"]                           # 返回结果
        self.assertIn(check, res_text)


if __name__ == "__main__":
    unittest.main()
