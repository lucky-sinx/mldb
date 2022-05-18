from db import DataSet
from manager.load_data import load_csv_data
from manager.node._base import NodeSuper, NodeStrategyFactory


class NodeDataLoad(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeDataLoad, self).__init__(node_info, result_dict)

    def execute(self):
        # 根据id获取dataset path
        dataset_info = DataSet.get_by_id(self.node_info["data_id"])
        self.result_dict["data_set"] = list(load_csv_data(dataset_info.path))

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("data_load", cls)