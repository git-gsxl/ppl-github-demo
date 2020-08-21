import pymysql


def send_sql(sql=''):
    ''' sql操作 '''
    try:
        db = pymysql.connect(
            host='xxx.xxx.84',
            port=3306,
            user='root',
            passwd='123456',
            db='hrun')

        cur = db.cursor()               # 使用 cursor() 方法创建一个游标对象cur
        cur.execute(sql)                # 使用 execute()  方法执行 SQL 查询
        data = cur.fetchall()           # 使用fetchall()方法获取查询结果 (接收全部的返回结果)
        db.commit()                     # 提交执行
        db.close()                      # 关闭连接
        return '已为您执行sql语句：%s\n返回结果：%s' % (sql, data)

    except:
        return 'sql连接或sql语句错误！！！'


if __name__ == '__main__':
    sql = "delete from UserInfo where username is null;"
    # sql = 'select * from1 UserInfo where username="gsxl";'
    print(send_sql(sql))
