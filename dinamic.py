"""test to dinamic values"""
from src.database import Dataset
from src.knn import Knn

data = Dataset('heart.csv')
knn = Knn(data)

dinamic_x_train_data = data.fit_transform_dinamically_x_train_data()
dinamic_y_train_data = data.get_dinamically_y_train_data()

dinamic_y_test_data = data.get_dinamically_y_test_data()
dinamic_x_test_data = data.fit_transform_dinamically_x_test_data()

knn.classifier(dinamic_x_train_data, dinamic_y_train_data)
y_pred = knn.test_prevision(dinamic_x_test_data)

acuracy = knn.get_acuracy(dinamic_y_test_data, y_pred)
error_rate = knn.get_error_rate(dinamic_y_test_data, y_pred)

print(f"Distance: {knn.distance}")
print(f"n_neighbors: {knn.n_neighbors}")
print(f"Random State: {data.random_state}")
print(f"Acuracia: {acuracy} ≈ {round(acuracy,2)}")
print(f"Taxa de erro: {error_rate} ≈ {round(error_rate,2)}")
