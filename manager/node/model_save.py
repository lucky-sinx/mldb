from db import Model
from manager.node._base import NodeSuper, NodeStrategyFactory


class NodeModelSave(NodeSuper):
    def __init__(self, node_info, result_dict):
        super(NodeModelSave, self).__init__(node_info, result_dict)

    def execute(self):
        model = self.result_dict["model"]
        model.save()
        model_id = Model.add_model(model.model_name, model.model_type, model.model_path, model.param).id
        self.result_dict["model_id"] = model_id

    @classmethod
    def register_node(cls):
        NodeStrategyFactory.register("model save", cls)
