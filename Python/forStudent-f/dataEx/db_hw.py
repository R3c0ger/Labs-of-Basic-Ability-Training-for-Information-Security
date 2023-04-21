#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 题目十八：实现数据库的操作
import sqlite3
import os

db_hw_db_path = ""  # 全局变量，在create_db(path)时记录创建的数据库所在路径


def create_db(path):
    global db_hw_db_path
    db_hw_db_path = path
    if os.path.exists(path):
        os.remove(path) # 如果数据库文件已存在，则删除

    # 连接到数据库，并获取游标
    conn = sqlite3.connect(path)
    c = conn.cursor()
    # 创建Person表
    c.execute('''CREATE TABLE Person
                (NAME TEXT(32), GENDER CHAR(2), BIRTH DATE, ID CHAR(18) PRIMARY KEY, POSITIONID CHAR(1));''')
    # 创建Position表
    c.execute('''CREATE TABLE Position
                (POSITIONID CHAR(1) PRIMARY KEY, SALARY INT);''')
    # 向Position表中插入数据
    c.execute("INSERT INTO Position (POSITIONID, SALARY) VALUES ('A', 10000), ('B', 6000), ('C', 3000), ('D', 1000);")

    # 提交事务并关闭连接
    conn.commit()
    conn.close()
    return 0

# 使用Insert语句
def new_employee(person,level):
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor() # 获取游标，用于执行SQL语句

    # 从Position表中获取指定岗位的薪水
    c.execute("SELECT SALARY FROM Position WHERE POSITIONID = ?", (level,))
    result = c.fetchone() # 获取查询结果
    if not result:
        return -1

    # 将新员工信息插入到Person表中
    c.execute("INSERT INTO Person (NAME, GENDER, BIRTH, ID, POSITIONID) VALUES (?, ?, ?, ?, ?);",
              (person[0], person[1], person[2], person[3], level))
    conn.commit() # 提交事务并关闭连接
    conn.close()
    return 0

# 使用Delete语句
def delete_employee(person):
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()

    # 根据员工ID从Person表中删除员工信息
    c.execute("DELETE FROM Person WHERE ID = ?", (person,))
    if c.rowcount == 0: # 如果删除的行数为0，则说明没有找到指定员工
        return -1
    conn.commit()
    conn.close()
    return 0

# 使用Update语句
def set_level_salary(level,salary):
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()

    # 更新Position表中指定岗位的薪水
    c.execute("UPDATE Position SET SALARY = ? WHERE POSITIONID = ?", (salary, level))
    if c.rowcount == 0:
        return -1
    conn.commit()
    conn.close()
    return 0

# 使用Select查询语句
def get_total_salary():
    conn = sqlite3.connect(db_hw_db_path)
    c = conn.cursor()

    # 通过JOIN操作获取Person表和Position表中所有员工的薪水并求和
    c.execute("SELECT SUM(SALARY) FROM Position JOIN Person ON Position.POSITIONID = Person.POSITIONID;")
    result = c.fetchone()
    conn.close()
    if not result:
        return -1
    return result[0] # result[0]即SUM(SALARY)


if __name__ == "__main__":
    create_db('./test.db')
    new_employee(("tom","m","2018-09-01","123456789"),"A")
    new_employee(("too","f","2017-09-01","123456788"),"B")
    print(get_total_salary())
    delete_employee("123456788")
    print(get_total_salary())
    set_level_salary("A",2)
    print(get_total_salary())
