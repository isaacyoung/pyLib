import sys

import datetime
import pymysql


def connect():
    return pymysql.connect('127.0.0.1', 'root', '123456',
                           'diary', 3306, charset='utf8')


def get_data():
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `diary_log` ORDER BY ID DESC LIMIT 10"
            cursor.execute(sql)
            for i in range(cursor.rowcount):
                row = cursor.fetchone()
                print(row)

    finally:
        connection.close()


def insert_data(content, date=datetime.date.today()):
    connection = connect()
    try:
        with connection.cursor() as cursor:
            sql = "INSERT INTO `diary_log` (`diary_date`, `content`) VALUES (%s, %s)"
            cursor.execute(sql, (date, content))

        connection.commit()

    finally:
        connection.close()

args = sys.argv
if len(args) != 3 and len(args) != 2 and len(args) != 1:
    raise Exception('参数有误')


if len(args) == 1:
    get_data()
elif len(args) == 2:
    insert_data(args[1])
else:
    insert_data(args[2], args[1])
