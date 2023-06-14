"""entrypoint"""
from src.database import Dataset

data = Dataset('heart.csv')
dinamic_train_data = data.get_dinamically_train_data()
dinamic_test_data = data.get_dinamically_test_data()

static_train_data = data.get_statically_train_data()
static_test_data = data.get_statically_test_data()
