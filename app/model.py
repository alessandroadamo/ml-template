# Script for the classifier class
from sklearn.base import BaseEstimator, ClassifierMixin


class MyClassifier(BaseEstimator, ClassifierMixin):
    """An example of classifier"""

    def __init__(self, intValue=0, stringParam="defaultValue"):
        """
        Called when initializing the classifier
        """
        self.intValue = intValue
        self.stringParam = stringParam

    def fit(self, X, y=None):
        """
        This should fit classifier. All the "work" should be done here.

        Note: assert is not a good choice here and you should rather
        use try/except blog with exceptions. This is just for short syntax.
        """
        assert (type(self.intValue) == int), "intValue parameter must be integer"
        assert (type(self.stringParam) == str), "stringValue parameter must be string"

        self.treshold_ = (sum(sum(X)) / len(X)) + self.intValue  # mean + intValue

        return self

    def _meaning(self, x):
        # returns True/False according to fitted classifier
        # notice underscore on the beginning
        return (True if sum(x) >= self.treshold_ else False)

    def predict(self, X, y=None):
        try:
            getattr(self, "treshold_")
        except AttributeError:
            raise RuntimeError("You must train classifer before predicting data!")

        return ([self._meaning(x) for x in X])

    def score(self, X, y=None):
        # counts number of values bigger than mean
        return (sum(self.predict(X)))