from db import DataSet
from manager.data_preprocessing import feature_filter
from manager.load_data import load_csv_data
from manager.node._base import NodeSuper, NodeStrategyFactory


class NodeDataPreProcessing(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeDataPreProcessing, self).__init__(node_info, result_dict)

    def execute(self):
        for process in self.node_info["process"]:
            if process["type"] == "feature select":
                self.result_dict["data_set"][0] = feature_filter(self.result_dict["data_set"][0], process["features"])

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("data_preprocessing", cls)