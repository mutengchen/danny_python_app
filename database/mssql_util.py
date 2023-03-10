#sql server
# mysql
# 封装了创建数据库连接，查询，释放的简单操作
# 具体的配置写在config/config.ini [mssql]
# 因为sql server有两种方式去登录，一种是window认证不需要密码，只能访问本机数据库或者局域网数据库，其他的是远程访问
import pymssql
from config.config_util import getValue
class MSSQL_DB(object):
    def __init__(self):
        #读取数据库host,port，建立连接
        self.host = getValue("mssql","host")
        self.port = getValue("mssql","port")
        self.account = getValue("mssql","account")
        self.pwd = getValue("mssql","password")
        self.db_name = getValue("mssql","db")
        pass
    def connect(self):
        self.conn = pymssql.connect(host=self.host,
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


