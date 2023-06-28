"""KNN class"""
import random
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

class Knn:
    """Knn Class"""

    p = None
    dataset = None
    distance = None
    n_neighbors = None
    knn_classifier = None

    def __init__(self, dataset) -> None:
        self.dataset = dataset
        self.p = random.randint(1,2)
        self.distance = self.__get_distance()
        self.n_neighbors = random.randrange(1,100,2)

        self.knn_classifier = KNeighborsClassifier(n_neighbors=self.n_neighbors,
                                                   metric='minkowski',
                                                   p=self.p
                                                )
    def __get_distance(self):
        return "Manhattan Distance" if self.p == 1 else " Euclidean Distance"

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
