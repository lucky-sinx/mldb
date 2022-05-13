import unittest

from sklearn import datasets


class MyTestCase(unittest.TestCase):

    def test_logistic(self):
        from manager import models
        iris = datasets.load_iris()
        X = iris.data[:, :]
        Y = iris.target
        param = {
            "max_iter": 1,
            "penalty": "none",
        }
        models.run_logistic_regression(X, Y, param)


if __name__ == '__main__':
    unittest.main()
