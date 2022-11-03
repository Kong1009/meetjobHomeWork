# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 20:56:11 2022

@author: DCT
"""

from flask import Flask, render_template, request, redirect
import db
import os

app = Flask(__name__)


# 主頁
@app.route("/")
def index():
    sql = "select * from servic_items"
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    items = cursor.fetchall()
    
    sql = "select name, info, profession from customer_comment"
    
    cursor.execute(sql)
    db.conn.commit()
    
    comment = cursor.fetchall()
    
    msg = 'Hello'
    
    
        
    
    return render_template("index.html", **locals())

@app.route("/addComment", methods=['post'])
def addComment():
    if request.method == "POST":
        name = request.form.get('username')
        profession = request.form.get('profession')
        comment = request.form.get('comment')
        
        if comment != '':
            sql = "insert into customer_comment(name, info, profession) values('{}', '{}', '{}')".format(name, comment, profession)
            cursor = db.conn.cursor()
            cursor.execute(sql)
            db.conn.commit()
            
            msg = "評論新增完成"
        else:
            msg = '評論不可空白'
    return redirect('/', msg)

@app.route("/HotNews")
def HotNews():
    sql = "select * from servic_items"
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    items = cursor.fetchall()
    
    sql = "select title, info from hotnews"    
    cursor.execute(sql)
    db.conn.commit()
    
    hotnews = cursor.fetchall()
    return render_template("hot_news.html", **locals())

@app.route("/about")
def about():
    img_list= []


    img_path = 'images/team/'
    img = os.listdir(os.path.join('./static/images/team'))
    # img = os.listdir('./static/images/team')
    for r in img:
        img_list.append(img_path + r)
    
    return render_template("about.html", **locals())


# 服務項目template
@app.route("/service")
def service():
    sql = "select * from servic_items"
    
    cursor = db.conn.cursor()
    cursor.execute(sql)
    db.conn.commit()
    
    items = cursor.fetchall()
    
    
    return render_template("service.html", **locals())


@app.route("/reserve-item", methods=['post'])
def reserve_item():
    if request.method == 'POST':
        item = request.form.get('item')
        customername = request.form.get('customername')
        email = request.form.get('email')
        date = request.form.get('reserve-date')
        time = request.form.get('reserve-time')
        
        sql = "select item from servic_items where id = '{}'".format(item)
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        data = cursor.fetchall()
        for row in data:
            if item == "1":
                item = row[0]
            elif item == "2":
                item = row[0]
            elif item == "3":
                item = row[0]
            else:
                item = row[0]
            
        sql = "insert into reserve_list(customername, item, email, reserve_date, reserve_time) values('{}', '{}', '{}', '{}', '{}')".format(customername, item, email, date, time)
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        

    return redirect("/service")




# 連絡我們template
@app.route('/contact')
def contact():
    return render_template("contact.html")


# 新增用戶問題到資料庫
@app.route("/addMessage", methods=['post'])
def addMessage():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        title = request.form.get('title')
        content = request.form.get('content')
        
        sql = "insert into contact(username, email, title, content) values('{}', '{}', '{}', '{}')".format(username, email, title, content)
        
        cursor = db.conn.cursor()
        cursor.execute(sql)
        db.conn.commit()
        
    return redirect("/contact")
# app.run(debug=True, host='0.0.0.0', port = 5555)
app.run(debug=True)