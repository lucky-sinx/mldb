import datetime
import json

import db
from pymysql.converters import escape_string


def show_tables():
    cur = db.conn.cursor()
    cur.execute("show tables")
    result = cur.fetchall()
    for i in result:
        print(i)


def save_model(model, model_path, model_type, model_name, param, score):
    model_path, model_type, model_name, param = escape_string(model_path), escape_string(model_type), escape_string(
        model_name), escape_string(str(json.dumps(param)))

    cur = db.conn.cursor()
    sql = "INSERT INTO mltest.model" \
          "(model_name, model_type, model_path, create_time, alhorithm_param)" \
          "VALUES('%s', '%s', '%s', '%s', '%s')" % (model_name, model_path, model_type, datetime.datetime.now(), param)

    try:
        cur.execute(sql)
        db.conn.commit()
    except Exception as e:
        db.conn.rollback()
        raise e
