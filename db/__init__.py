import pymysql

conn = pymysql.connect(
    host='127.0.0.1',  # 连接名称，默认127.0.0.1
    user='root',  # 用户名
    passwd='root',  # 密码
    port=3306,  # 端口，默认为3306
    db='mltest',  # 数据库名称
    charset='utf8',  # 字符编码
)
conn.connect()
