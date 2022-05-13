import unittest


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)  # add assertion here

    def test_logistic(self):
        import numpy as np
        import matplotlib.pyplot as plt
        from sklearn import linear_model, datasets
        from sklearn.model_selection import train_test_split

        # 加载鸢尾花数据
        iris = datasets.load_iris()
        # 只采用样本数据的前两个feature，生成X和Y
        X = iris.data[:, :]
        Y = iris.target

        h = .02  # 网格中的步长
        X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=42)
        # 新建模型，设置C参数为1e5，并进行训练
        logreg = linear_model.LogisticRegression(C=1e5)
        # logreg.fit(data, Y)
        logreg.fit(X_train, y_train)

        result = logreg.predict(X_test)
        print(logreg.score(X_test, y_test))

        # # 绘制决策边界。为此我们将为网格 [x_min, x_max]x[y_min, y_max] 中的每个点分配一个颜色。
        # x_min, x_max = X_test[:, 0].min() - .5, X_test[:, 0].max() + .5
        # y_min, y_max = X_test[:, 1].min() - .5, X_test[:, 1].max() + .5
        # xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
        # Z = logreg.predict(np.c_[xx.ravel(), yy.ravel()])
        #
        # # 将结果放入彩色图中
        # Z = Z.reshape(xx.shape)
        # plt.figure(1, figsize=(4, 3))
        # plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)
        #
        # # 将训练点也同样放入彩色图中
        # plt.scatter(data[:, 0], data[:, 1], c=Y, edgecolors='k', cmap=plt.cm.Paired)
        # plt.xlabel('Sepal length')
        # plt.ylabel('Sepal width')
        #
        # plt.xlim(xx.min(), xx.max())
        # plt.ylim(yy.min(), yy.max())
        # plt.xticks(())
        # plt.yticks(())
        #
        # plt.show()


if __name__ == '__main__':
    unittest.main()
