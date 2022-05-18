import datetime
import json

from db import Task, Task_log, DataSet, Model
from .data_preprocessing import feature_filter
from .model import ClassifyModelBase
from .node import NodeStrategyFactory


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
        result_dict = {}
        for node_info in task:
            node_cls = NodeStrategyFactory.get_strategy_by_type(node_info["type"])
            node = node_cls(node_info, result_dict)
            node.execute()

        task_log.end_time = datetime.datetime.now()
        task_log.generate_model_id = result_dict["model_id"]
        task_log.result = str(result_dict["model"].score)
        task_log.save()
