import unittest
from app.model import MyClassifier
from sklearn.datasets import load_iris

class MyClassifierTest(unittest.TestCase):

    def test_fit(self):

        iris = load_iris()

        model = MyClassifier()
        r = model.fit(iris.data, iris.target)

        self.assertEqual(r, model,  "Models should be equlals")

    def test_predict(self):
        iris = load_iris()

        model = MyClassifier()
        model.fit(iris.data, iris.target)

        pred = model.predict([[5, 1, 2, 3]])

        self.assertEqual(pred, [False],  "Prediction should be equlals")

    def test_score(self):

        iris = load_iris()

        model = MyClassifier()
        model.fit(iris.data, iris.target)

        sc = model.score([[5, 1, 2, 3]])

        self.assertEqual(sc, 0,  "TODO")


if __name__ == '__main__':

    unittest.main()
