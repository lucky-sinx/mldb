import json
import os.path
import uuid

import joblib
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

ModelTypeToModel = {
    "LogisticRegression": LogisticRegression
}


class ModelBase:
    def __init__(self, model_type, param=None, model_path=None, model_name=None):
        self.model_type = model_type
        self.param = param
        self.model_path = model_path
        self.model_name = model_name
        self.model = None
        self.score = -1

        if model_type in ModelTypeToModel:
            if param is None:
                self.model = ModelTypeToModel[model_type]()
            else:
                self.model = ModelTypeToModel[model_type](**param)

    def train(self, data, label):
        x_train, x_test, y_train, y_test = train_test_split(data, label, test_size=0.3, random_state=42)
        self.model.fit(x_train, y_train)
        self.score = self.model.score(x_test, y_test)

        if self.model_path is None:
            # 存储到默认的文件夹
            self.model_path = os.path.join("F:\code\python\mldb\\temp\model",
                                           self.model_type + "_" + str(uuid.uuid4())[:8] + ".pickle")

        if self.model_name is None:
            self.model_name = self.model_type

        # dbUtils.save_model(self.model, self.model_name, self.model_path, self.model_type, self.param, score)

    def save(self):
        joblib.dump(self.model, self.model_path)


def run_logistic_regression(X, y, param: dict, model_name=None, model_path=None):
    model = ModelBase("LogisticRegression", param, model_name, model_path)
    model.train(X, y)
