"""KNN class"""
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class Knn:
    """Knn Class"""

    dataset = None
    knn_classifier = None

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.knn_classifier = KNeighborsClassifier(n_neighbors=2, metric='minkowski', p=1)

    def classifier(self, x_train, y_train):
        """Method to classifier"""

        self.knn_classifier.fit(x_train, y_train)

    def test_prevision(self, x_test):
        """Method to make prevision test data"""

        return self.knn_classifier.predict(x_test)

    def get_acuracy(self, y_test, y_pred):
        """Method to get acurracy"""

        return accuracy_score(y_test, y_pred)


    def get_error_rate(self, y_test, y_pred):
        """Method to get error tax"""

        return 1 - self.get_acuracy(y_test, y_pred)
