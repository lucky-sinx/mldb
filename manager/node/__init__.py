from .model_save import NodeModelSave
from .node_data_load import NodeDataLoad
from .node_data_preprocessing import NodeDataPreProcessing
from .node_model_train import NodeModelTrain
from ._base import NodeStrategyFactory


def init_register():
    NodeDataLoad.register_node()
    NodeDataPreProcessing.register_node()
    NodeModelTrain.register_node()
    NodeModelSave.register_node()


init_register()

__all__ = [
    "NodeStrategyFactory"
]
