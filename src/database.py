"""Class representing a Dataset"""
from math import ceil
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

class Dataset:
    """Class representing a Dataset"""

    dataframe = pd.DataFrame()

    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)
        self.dataframe_size = len(self.dataframe.index)

    def __set_dinamically_train_test_data(self):
        x = self.dataframe.drop(columns=['target'])
        y = self.dataframe['target']

        x_train, x_test, y_train, y_test = train_test_split(
                                       x, y,
                                       test_size=0.3,
                                       train_size=0.7,
                                       random_state=42
                                    )

        return [x_train, x_test, y_train, y_test]

    def __get_total_lines_by_percentage(self, value, percentage, use_ceil=False):
        if use_ceil is True:
            return ceil((value * percentage) / 100)

        return int((value * percentage) / 100)

    def __set_statically_x_train_test_data(self):
        amout_lines_to_train = self.__get_total_lines_by_percentage(self.dataframe_size,70)
        amout_lines_to_test = self.__get_total_lines_by_percentage(self.dataframe_size,30, True)

        train = self.dataframe.drop(columns=['target']).head(amout_lines_to_train)
        test = self.dataframe.drop(columns=['target']).tail(amout_lines_to_test)

        return [train, test]

    def __set_statically_y_train_test_data(self):
        amout_lines_to_train = self.__get_total_lines_by_percentage(self.dataframe_size,70)
        amout_lines_to_test = self.__get_total_lines_by_percentage(self.dataframe_size,30, True)

        train = self.dataframe['target'].head(amout_lines_to_train)
        test = self.dataframe['target'].tail(amout_lines_to_test)

        return [train, test]

    def get_dinamically_x_train_data(self):
        """Method to get dinamically train data"""

        x_train, _, _, _ = self.__set_dinamically_train_test_data()

        return x_train

    def get_dinamically_y_train_data(self):
        """Method to get dinamically y train data"""

        _, _, y_train, _ = self.__set_dinamically_train_test_data()

        return y_train

    def get_dinamically_x_test_data(self):
        """Method to get dinamically x test data"""

        _, x_test, _, _ = self.__set_dinamically_train_test_data()

        return x_test

    def get_dinamically_y_test_data(self):
        """Method to get dinamically y test data"""

        _, _, _, y_test = self.__set_dinamically_train_test_data()

        return y_test

    def get_statically_x_train_data(self):
        """Method to get statically train data"""

        train, _ = self.__set_statically_x_train_test_data()

        return train

    def get_statically_y_train_data(self):
        """Method to get statically  y train data"""

        train, _ = self.__set_statically_y_train_test_data()

        return train

    def get_statically_x_test_data(self):
        """Method to get statically test data"""
        _, test = self.__set_statically_x_train_test_data()

        return test

    def get_statically_y_test_data(self):
        """Method to get statically test data"""
        _, test = self.__set_statically_y_train_test_data()

        return test

    def __fit_transform_statically_x_train_test(self):
        standard_scaler = StandardScaler()

        x_train = standard_scaler.fit_transform(self.get_statically_x_train_data())
        x_test =  standard_scaler.transform(self.get_statically_x_test_data())

        return [x_train, x_test]

    def __fit_transform_dinamically_x_train_test(self):
        standard_scaler = StandardScaler()

        x_train = standard_scaler.fit_transform(self.get_dinamically_x_train_data())
        x_test =  standard_scaler.transform(self.get_dinamically_x_test_data())

        return [x_train, x_test]

    def fit_transform_dinamically_x_train_data(self):
        """Method to reduce train values"""

        x_train, _ = self.__fit_transform_dinamically_x_train_test()

        return x_train

    def fit_transform_dinamically_x_test_data(self):
        """Method to reduce train values"""  

        _, x_test = self.__fit_transform_dinamically_x_train_test()

        return x_test

    def fit_transform_statically_x_train_data(self):
        """Method to reduce train values"""

        x_train, _ = self.__fit_transform_statically_x_train_test()

        return x_train

    def fit_transform_statically_x_test_data(self):
        """Method to reduce train values"""

        _, x_test = self.__fit_transform_statically_x_train_test()

        return x_test
