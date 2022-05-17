import datetime
import json

from db import Task, Task_log, DataSet, Model
from .load_data import load_csv_data
from .data_preprocessing import feature_filter
from .model import ModelBase


class TaskFlow:
    def __init__(self, task_id):
        self.id = task_id
        self.task_info = None
        self.task = None
        self.read_task_info()

    def read_task_info(self):
        """
            读取数据库，获取task存取的路径
        :return:
        """
        self.task_info = Task.get_by_id(self.id)
        task_filepath = self.task_info.path
        with open(task_filepath, "r") as f:
            self.task = json.load(f)

    def run_task(self):
        """
            运行task
        :return:
        """
        query = {
            "task_id": self.id,
            "start_time": datetime.datetime.now()
        }
        # 读取数据库，获取task文件路径
        with open(self.task_info.path, "r") as f:
            task = json.load(f)

        # 首先向task_log表插入一条日志
        task_log = Task_log.create(**query)
        data_set, model = None, None
        for node in task:
            if node["type"] == "data_load":
                # 根据id获取dataset path
                dataset_info = DataSet.get_by_id(node["data_id"])
                x, y, _ = load_csv_data(dataset_info.path)
                data_set = [x, y]
            if node["type"] == "data_preprocessing":
                for process in node["process"]:
                    if process["type"] == "feature select":
                        data_set[0] = feature_filter(data_set[0], process["features"])
            if node["type"] == "model train":
                model_info = node["model"]
                model = ModelBase(model_info["name"], model_info["param"])
                model.train(*data_set)
            if node["type"] == "model save":
                model.save()
                model_id = Model.add_model(model.model_name, model.model_type, model.model_path, model.param).id
        task_log.end_time = datetime.datetime.now()
        task_log.generate_model_id = model_id
        task_log.result = str(model.score)
        task_log.save()
