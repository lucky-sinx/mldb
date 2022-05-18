from manager.model import ClassifyModelBase
from manager.node._base import NodeSuper, NodeStrategyFactory


class NodeModelTrain(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeModelTrain, self).__init__(node_info, result_dict)

    def execute(self):
        model_info = self.node_info["model"]
        model = ClassifyModelBase(model_info["name"], model_info["param"])
        model.train(self.result_dict["data_set"][0], self.result_dict["data_set"][1])
        self.result_dict["model"] = model

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("model train", cls)
