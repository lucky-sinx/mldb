from db import DataSet
from manager.data_preprocessing import feature_filter

"""
策略模式+工厂模式实现工作节点
"""


class NodeSuper:
    """
    工作流节点基类
    """

    def __init__(self, node_info, result_dict):
        self.node_info = node_info
        self.result_dict = result_dict

    def execute(self):
        pass


class NodeStrategyFactory(object):
    strategy = {}

    @classmethod
    def get_strategy_by_type(cls, node_name):
        """
        类方法，通过name获取具体的策略类
        :param node_name:
        :return:
        """
        return cls.strategy.get(node_name)

    @classmethod
    def register(cls, node_name, strategy):
        """
        类方法，注册策略类型
        :param node_name:
        :param strategy:
        :return:
        """
        if strategy == "":
            raise Exception("node_name can't be null")
        cls.strategy[node_name] = strategy
