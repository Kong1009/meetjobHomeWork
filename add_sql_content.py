# -*- coding: utf-8 -*-
"""
Created on Thu Nov  3 12:00:20 2022

@author: DCT
"""
import db


# 新增最新消息
def add_HotNews():

    title = input("輸入最新消息標題：")
    info = input("輸入最新消息內容：")
    
    sql = "select title from hotnews where title = '{}'".format(title)
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    if cursor.rowcount != 1:
        sql = "insert into hotnews(title, info) values('{}', '{}')".format(title, info)
        cursor.execute(sql)
        db.conn.commit()
    
        print("'{}' 新增完成".format(title))
    else:
        print("'{}' 已存在".format(title))
    
    db.conn.close()
    
    
    
# 新增顧客評論
def add_customer_comment():
    name = input("顧客：")
    info = input("輸入評論：")
    
    sql = "insert into customer_comment(name, info) values('{}', '{}')".format(name, info)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    db.conn.close()
    
    print("評論完成")

add_customer_comment()
    
# 新增服務項目
def add_item():
    item = input("輸入服務項目：")
    info = input("輸入項目描述：")
    profession = input('輸入職業：')
    
    sql = "select item from servic_items where item = '{}'".format(item)
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    if cursor.rowcount == 0:
        sql = "insert into servic_items(item, info, profession) values('{}', '{}', '{}')".format(item, info, profession)
        cursor.execute(sql)
        db.conn.commit()
        
    else:
        print("{}已存在".format(item))