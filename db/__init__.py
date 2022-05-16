import datetime
from peewee import *

db = MySQLDatabase('mltest', host='127.0.0.1', user='root', passwd='root', charset='utf8', port=3306)


class BaseModel(Model):
    class Meta:
        database = db  # 将实体与数据库进行绑定


class DataSet(BaseModel):
    id = AutoField()
    dataset_name = CharField(100)
    dataset_description = CharField(100)
    path = CharField(100)
    create_time = DateTimeField()

    @staticmethod
    def add_dataset(name, path, description=""):
        DataSet.create(dataset_name=name, path=path, dataset_description=description,
                       create_time=datetime.datetime.now())


class Model(BaseModel):
    id = AutoField()
    model_name = CharField(100)
    model_type = CharField(100)
    model_path = CharField(200)
    create_time = DateTimeField()
    algorithm_param = CharField(200)

    @staticmethod
    def add_model(model_name, model_type, model_path, algorithm_param):
        Model.create(model_name=model_name, model_path=model_path, model_type=model_type,
                     create_time=datetime.datetime.now(), algorithm_param=algorithm_param)


class Task(BaseModel):
    id = AutoField()
    task_name = CharField(100)
    task_description = CharField(100)
    path = CharField(100)
    create_time = DateTimeField()


class Task_log(BaseModel):
    id = AutoField()
    task_id = BigIntegerField()
    generate_model_id = BigIntegerField()
    result = CharField(100)
    start_time = DateTimeField()
    end_time = DateTimeField()
