# coding:utf-8
import xlrd
class Excel():
    '''excelPath= excel 的目录路径，sheetName = 自定义table'''
    def __init__(self, excelPath, tableName='Sheet1'):
        self.data = xlrd.open_workbook(excelPath)
        self.table = self.data.sheet_by_name(tableName)
        self.keys = self.table.row_values(0)    # 获取第一行作为key值
        self.rowNum = self.table.nrows          # 获取总行数
        self.colNum = self.table.ncols          # 获取总列数

    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum-1):
                s = {}
                values = self.table.row_values(j)   # 从第二行取对应values值
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
