import db


def show_tables():
    cur = db.conn.cursor()
    cur.execute("show tables")
    result = cur.fetchall()
    for i in result:
        print(i)
