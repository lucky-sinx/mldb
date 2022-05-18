import unittest

from sklearn import datasets


class MyTestCase(unittest.TestCase):

    def test_logistic(self):
        from manager import model
        iris = datasets.load_iris()
        X = iris.data[:, :]
        Y = iris.target
        param = {
            "max_iter": 1,
            "penalty": "none",
        }
        # models.run_logistic_regression(X, Y, param)

    def test_taskflow(self):
        from manager.task import TaskFlow
        task_flow = TaskFlow(10)
        task_flow.run_task()

    def test_load_iris(self):
        from manager.load_data import load_csv_data
        data, target, _ = load_csv_data("F:\code\python\mldb\\temp\dataset\iris.csv")
        t = 0

    def test_filter(self):
        from manager.load_data import load_csv_data
        from manager.data_preprocessing import feature_filter
        data, target, _ = load_csv_data("F:\code\python\mldb\\temp\dataset\iris.csv")
        filter_str = "[0,2,3]"
        data = feature_filter(data, filter_str)
        print(data)


if __name__ == '__main__':
    unittest.main()
