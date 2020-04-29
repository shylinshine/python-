# -*- coding:utf-8 -*-

import pymysql

# 打开本地数据库用于存储用户信息

# 创建一个 Connection 对象，代表了一个数据库连接
connection = pymysql.connect(
    host='localhost',  # 数据库IP地址
    user="root",  # mysql用户名
    passwd="w5220699..",  # mysql用户登录密码
    db="scott",  # 数据库名
    # 如果数据库里面的文本是utf8编码的，
    # charset指定是utf8
    charset="utf8")

# 返回一个 Cursor对象
cx = connection.cursor()


# #在该数据库下创建学生信息表
# cx.execute (f'''CREATE TABLE if not exists StudentTable(ID    int(10)  PRIMARY KEY   AUTO_INCREMENT,
#                                                         StuId  int(10)   ,
#                                                         SNAME   varchar(20) ,
#                                                         CLASS    varchar(10) );''')
# print ('Table created successfully')

# #在该数据库下创建课程信息表
# cx.execute ('''CREATE TABLE CourseTable(
#    ID int (10) PRIMARY KEY   AUTO_INCREMENT,
#    CourseId       INT(10)       NOT NULL,
#    SName           varchar(20)      NOT NULL,
#    Teacher           varchar(20)      NOT NULL,
#    Classroom            varchar(20)      NOT NULL,1
#    StartTime             varchar(20)    NOT NULL,
#    EndTime                varchar(20)    NOT NULL);''')
# print ('Table created successfully')


# #在该数据库下创建选课情况信息表
# cx.execute ('''CREATE TABLE XuankeTable(
#    ID int(10) PRIMARY KEY   AUTO_INCREMENT,
#    StuId       int(10)        NOT NULL,
#    CourseId     int(10)         NOT NULL);''')
# print ('Table created successfully')

# 以上三个表创建完后，再次运行程序时，需要把三个建表代码注释掉，否则会提示:该表已存在。即建表只需建一次。


def insert_stu():  # 录入学生信息
    cu = connection.cursor()
    stu_id = int(input("请输入学生学号:"))
    cu.execute(f"SELECT StuId from StudentTable where StuId = {stu_id};")
    row = cu.fetchone()
    if row:
        print('sorry,该学号已存在,请重新输入')
    else:
        stu_name = input("请输入学生姓名:")
        stu_class = int(input("请输入学生班级:"))
        sql1 = "INSERT INTO StudentTable(StuId,SNAME,CLASS)"
        sql1 += " VALUES(%d,'%s',%d);" % (stu_id, stu_name, stu_class)
        cu.execute(sql1)
        connection.commit()
        print("恭喜你,学生录入成功!")
    connection.close()


def xuanke():  # 学生选课
    cu = connection.cursor()
    stu_id = int(input('请输入要选课的学生学号:'))
    sql2 = "select StuId from StudentTable where StuId = %d;" % (stu_id)
    cu.execute(sql2)
    row = cu.fetchone()
    if row:
        sql3 = "select CourseId,SName,Teacher,Classroom, StartTime,EndTime from CourseTable"
        cu.execute(sql3)
        rows = cu.fetchall()
        for row in rows:
            print("CourseId = ", row[0])
            print("SName = ", row[1])
            print("Teacher = ", row[2])
            print("Classroom = ", row[3])
            print("StartTime = ", row[4])
            print("EndTime = ", row[5], "\n")
        cou_id = int(input("请输入要选的课程号:"))
        sql0 = "select CourseId from CourseTable where CourseId =%d;" % (cou_id)
        cu.execute(sql0)
        row = cu.fetchone()
        if row:
            sql = "select StuId CourseId from XuankeTable "
            sql += "where CourseId = %d and StuId=%d;" % (cou_id, stu_id)
            cu.execute(sql)
            rows = cu.fetchone()
            if row:
                print("该课程已选,不能重复选课!")
                # break
            else:
                sql3 = "insert into XuankeTable (StuId,CourseId) values (%d,%d)" % (stu_id, cou_id)
                cu.execute(sql3)
                cx.commit()
                print("恭喜你，选课成功!")
        else:
            print("sorry,该课程不存在!")
    else:
        print("sorry,没有该学生号")
    cu.close()


def stu_id_search():  # 按照学生学号查询学生信息
    cu = connection.cursor()
    search_stu_id =int(input("请输入要查询的学号:"))
    sql4 = "SELECT ID,StuId,SNAME, CLASS from StudentTable "
    sql4 += "where StuId= %d;" % (search_stu_id)
    cu.execute(sql4)
    row = cu.fetchone()
    if row:
        print
        print("您要查询的学生信息为:")
        print("ID = ", row[0])
        print("StuId = ", row[1])
        print("SNAME = ", row[2])
        print("CLASS = ", row[3], "\n")
    else:
        print("sorry,没有该学生信息！")
    cu.close()


def stu_id_cou():  # 按照学生学号查询该学生所选课程
    cu = connection.cursor()
    stu_id = int(input("请输入要查询学生号:"))
    sql5 = "select StuId from StudentTable where StuId = %d;" % (stu_id)
    cu.execute(sql5)
    row = cu.fetchone()
    if row:
        sql6 = "select A.*,B.*,C.* from XuankeTable A, CourseTable B, StudentTable C \
        where A.StuId = %d and A.CourseId=B.CourseId and A.StuId=C.StuId" % (stu_id)  # 连表查询
        cu.execute(sql6)
        rows = cu.fetchall()
        for row in rows:
            print("该学生所选课程为:")
            print("StuId=", row[1])
            print("CourseId=", row[2])
            print("SName = ", row[7])
            print("Teacher = ", row[8])
            print("Classroom = ", row[9])
            print("StartTime = ", row[10])
            print("EndTime = ", row[11], "\n")

    else:
        print("sorry,没有该学生选课信息!")
    cu.close()


def cou_id_search():  # 按照课程号查询课程信息
    cu = connection.cursor()
    cou_id = int(input("请输入要查询的课程号:"))
    sql7 = "select CourseId ,SName,Teacher,Classroom,StartTime,EndTime from CourseTable "
    sql7 += "where CourseId = %d;" % (cou_id)
    cu.execute(sql7)
    row = cu.fetchone()
    if row:
        print("您要查询的课程信息为:")
        print("CourseId = ", row[0])
        print("SName = ", row[1])
        print("Teacher = ", row[2])
        print("Classroom = ", row[3])
        print("StartTime = ", row[4])
        print("EndTime = ", row[5], "\n")
    else:
        print("sorry,没有该课程信息!")
    cu.close()


def cou_id_stu():  # 按照课程号查询选择该课程的学生列表
    cu = connection.cursor()
    cou_id = int(input('请输入课程号:'))
    sql8 = "select CourseId from XuankeTable where CourseId =%d;" % (cou_id)
    cu.execute(sql8)
    row = cu.fetchone()
    if row:
        sql9 = "select A.*,B.*,C.* from XuankeTable A, CourseTable B, StudentTable C \
        where A.CourseId = %d and A.CourseId=B.CourseId and A.StuId=C.StuId" % (cou_id)
        cu.execute(sql9)
        rows = cu.fetchall()
        for row in rows:
            print("选择该课程的学生为:")
            print("StuId = ", row[1])
            print("CourseId = ", row[2])
            print("SNAME = ", row[14])
            print("CLASS = ", row[15], "\n")
    else:
        print("sorry,没有该课程信息!")
    cu.close()


def menu():
    print('1.进入学生信息系统(学生信息录入)')
    print('2.进入学生选课系统(学生选课操作)')
    print('3.进入学生选课信息系统(学生信息查询和选课情况查询)')
    print('4.退出程序')


def student():
    print('1.录入学生信息')
    print('2.返回主菜单')


def Course():
    print('1.开始选课')
    print('2.返回主菜单')


def information():
    print('1.按学号查询学生信息')
    print('2.按学号查看学生选课课程列表')
    print('3.按课程号查看课程信息')
    print('4.按课程号查看选课学生列表')
    print('5.返回主菜单')


while True:
    menu()
    print
    x = input('请输入您的选择菜单号:')
    if x == '1':
        # 进入学生信息系统
        student()
        stu = input('您已进入学生录入系统,请再次输入选择菜单:')
        print
        if stu == '1':
            insert_stu()
            continue
        if stu == '2':
            continue
        else:
            print("输入的选项不存在，请重新输入！")
            continue

    if x == '2':
        # 进入选课信息系统
        Course()
        cou = input('您已进入学生选课系统,请再次输入选择菜单:')
        print
        if cou == '1':
            xuanke()
            continue
        if cou == '2':
            continue
        else:
            print("输入的选项不存在，请重新输入！")
            continue

    if x == '3':
        # 进入学生选课信息表
        information()
        inf = input('您已进入学生选课信息系统,请再次输入选择菜单:')
        print
        if inf == '1':
            stu_id_search()
            continue
        if inf == '2':
            stu_id_cou()
            continue
        if inf == '3':
            cou_id_search()
            continue
        if inf == '4':
            cou_id_stu()
            continue
        if inf == '5':
            continue
        else:
            print("输入的选项不存在，请重新输入！")
            continue

    if x == '4':
        print("谢谢使用！")
        exit()
    else:
        print("输入的选项不存在，请重新输入！")
        continue

