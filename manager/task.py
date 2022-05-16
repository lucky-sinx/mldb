import datetime
import json

from db import Task, Task_log


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

    def run(self):
        """
            运行task
        :return:
        """
        query = {
            "task_id": self.id,
            "start_time": datetime.datetime.now()
        }
        # 首先向task_log表插入一条日志
        Task_log.create(**query)
        a = 0
