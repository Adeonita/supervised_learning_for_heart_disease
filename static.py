"""test to static values"""
from src.database import Dataset
from src.knn import Knn

data = Dataset('heart.csv')
knn = Knn(data)

static_x_train_data = data.fit_transform_statically_x_train_data()
static_y_train_data = data.get_statically_y_train_data()

static_x_test_data = data.fit_transform_statically_x_test_data()
static_y_test_data = data.get_statically_y_test_data()

knn.classifier(static_x_train_data, static_y_train_data)
y_pred = knn.test_prevision(static_x_test_data)

acuracy = knn.get_acuracy(static_y_test_data, y_pred)
error_rate = knn.get_error_rate(static_y_test_data, y_pred)

print(f"Distance: {knn.distance}")
print(f"n_neighbors: {knn.n_neighbors}")
print(f"Random State: {data.random_state}")
print(f"Acuracia: {acuracy} ≈ {round(acuracy,2)}")
print(f"Taxa de erro: {error_rate} ≈ {round(error_rate,2)}")
