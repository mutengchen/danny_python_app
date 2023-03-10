# mysql
# 封装了创建数据库连接，查询，释放的简单操作
# 具体的配置写在config/config.ini [mysql]

import pymysql
from config.config_util import getValue
class MySQL_DB(object):
    def __init__(self):
        #读取数据库host,port，建立连接
        self.host = getValue("mysql","host")
        self.port = getValue("mysql","port")
        self.account = getValue("mysql","account")
        self.pwd = getValue("mysql","password")
        self.db_name = getValue("mysql","db")
        pass
    def connect(self):
        self.conn = pymysql.connect(host=self.host,
                             user=self.account,
                             password=self.pwd,
                             database=self.db_name,
                             charset='utf8')
        self.cursor = self.conn.cursor()

    def release(self):
        self.cursor.close()
        self.conn.close()

    def search(self,sql,**kwargs):
        # self.cursor.execute(sql)
        # data = self.cursor.fetchone()
        # data = self.cursor.fetchall()
        # return data
        pass

    def pitch_insert(self,sql,data):
        # self.cursor.execute(sql)
        # self.conn.commit()

        pass


#创建数据库表
# sql="""CREATE TABLE test (
#           FIRST_  CHAR(20) NOT NULL,
#           SECOND_  CHAR(20),
#           THIRD_ INT,
#           FOURTH_ CHAR(1),
#           FIFTH_ FLOAT )"""

#插入操作
# sql = "insert into test(FIRST_,SECOND_,THIRD_,FOURTH_,FIFTH_) values ('MAC','MOTH','20','M','2000')"
#删除操作
# sql = "DELETE FROM student WHERE Sno='20111107'"

#批量插入

# list_1 = [('a',1),('b',2),('c',3)]  # 元素是不是元组都可以
# sql_1 = 'insert into 表明(字段1,字段2) values(%s,%s)'
# cursor.executemany(sql_1,list_1)

