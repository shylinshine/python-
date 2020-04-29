import pymysql

#打开本地数据库用于存储用户信息

# 创建一个 Connection 对象，代表了一个数据库连接
connection = pymysql.connect(
                host='localhost',# 数据库IP地址  
                user="root",     #  mysql用户名
                passwd="w5220699..",      # mysql用户登录密码
                db="scott" ,        # 数据库名
                # 如果数据库里面的文本是utf8编码的，
                #charset指定是utf8
                charset = "utf8")   

# 返回一个 Cursor对象
cx = connection.cursor()
cx.execute("""SELECT * FROM student """)







# 在该数据库下创建学生信息表
cx.execute ('''CREATE TABLE if not exists StudentTable(ID    int(10)      PRIMARY KEY   AUTO_INCREMENT,
                                                        StuId  varchar(10),
                                                        SNAME    varchar(10),
                                                        CLASS     varchar(10));''')
# print ('Table created successfully')