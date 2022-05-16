import datetime
import json
import os
import unittest

from peewee import AutoField


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_peewee(self):
        from peewee import MySQLDatabase, Model, CharField, DateField, BooleanField, IntegerField

        # py_peewee连接的数据库名
        db = MySQLDatabase('mltest', host='127.0.0.1', user='root', passwd='root', charset='utf8', port=3306)

        class BaseModel(Model):
            class Meta:
                database = db  # 将实体与数据库进行绑定

        class Person(BaseModel):  # 继承自BaseModel，直接关联db，并且也继承了Model。Model有提供增删查改的函数
            id1 = AutoField()
            name = CharField(verbose_name='姓名', max_length=10, null=False, index=True)
            passwd = CharField(verbose_name='密码', max_length=20, null=False, default='111111')
            gender = IntegerField(verbose_name='姓别', null=False, default=1)
            is_admin = BooleanField(verbose_name='是否是管理员', default=False)

        # 查询数据库是连接
        print(db.is_closed())  # 返回false未连接
        # 连接数据库
        db.connect()
        print(db.is_closed())  # 返回true表示已连接
        # 创建table
        Person.create_table(safe=False)

    def test_dataset(self):
        from db import DataSet
        # DataSet1.create_table(safe=True)
        DataSet.create(dataset_name="dataset1", dataset_description="test", path="./dataset",
                       create_time=datetime.datetime.now())
        DataSet.add_dataset("dataset2", "./dataset")
        DataSet.delete().execute()

    def test_model(self):
        from db import Model
        Model.add_model("model1", "classification", "./model", json.dumps({"test": 1}))

    def test_task(self):
        from db import Task
        query = {
            "task_name": "task1",
            "task_description": "test",
            "path": "F:\code\python\mldb\\temp\\task\\1.json",
            "create_time": datetime.datetime.now()
        }
        # Task.delete().execute()
        Task.create(**query)

    def test_load_dataset(self):
        from db import DataSet
        data_path = "F:\code\python\mldb\\temp\dataset"
        for file_name in os.listdir(data_path):
            DataSet.add_dataset(file_name.split('.')[0], os.path.join(data_path, file_name),
                                "test dataset:" + file_name)


if __name__ == '__main__':
    unittest.main()
