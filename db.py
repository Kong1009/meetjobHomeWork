# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 23:01:33 2022

@author: DCT
"""

import pymysql

dbsetting = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "root",
    "password": "123456789",
    "db": "flaskweb",
    "charset": "utf8"
    }

conn = pymysql.connect(**dbsetting)