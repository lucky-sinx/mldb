from db import DataSet
from manager.data_preprocessing import feature_filter
from .load_data import load_csv_data

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


class NodeDataLoad(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeDataLoad, self).__init__(node_info, result_dict)

    def execute(self):
        # 根据id获取dataset path
        dataset_info = DataSet.get_by_id(self.node_info["data_id"])
        self.result_dict["data_set"] = [load_csv_data(dataset_info.path)]

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("data_load", cls)


class NodeDataPreProcessing(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeDataPreProcessing, self).__init__(node_info, result_dict)

    def execute(self):
        for process in self.node_info["process"]:
            if process["type"] == "feature select":
                self.result_dict["data_set"][0] = feature_filter(self.result_dict["data_set"][0], process["features"])
        dataset_info = DataSet.get_by_id(self.node_info["data_id"])
        self.result_dict["data_set"] = [load_csv_data(dataset_info.path)]

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("data_preprocessing", cls)


class NodeModelTrain(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeModelTrain, self).__init__(node_info, result_dict)

    def execute(self):
        pass

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("model train", cls)


# class Node?(NodeSuper):
#     def __init__(self, node_info, result_dict):
#         super(, self).__init__(node_info, result_dict)
#
#     def execute(self):
#         pass
#
#     @classmethod
#     def register_node(cls):
#         NodeStrategyFactory.register("", cls)


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


def init_register():
    NodeDataLoad.register_node()


if __name__ == '__main__':
    init_register()
    node_cls = NodeStrategyFactory.get_strategy_by_type("data_load")
    node = node_cls()
    _ = 0
