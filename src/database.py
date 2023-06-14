"""Class representing a Dataset"""
from math import ceil
import pandas as pd
from sklearn.model_selection import train_test_split

class Dataset:
    """Class representing a Dataset"""

    dataframe = pd.DataFrame()

    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)
        self.dataframe_size = len(self.dataframe.index)

    def __set_dinamically_train_test_data(self):
        train, test = train_test_split(self.dataframe,
                                       test_size=0.3,
                                       train_size=0.7,
                                       random_state=42
                                    )

        return [train, test]

    def get_dinamically_train_data(self):
        """Method to get dinamically train data"""

        train, _ = self.__set_dinamically_train_test_data()

        return train

    def get_dinamically_test_data(self):
        """Method to get dinamically test data"""

        _, test = self.__set_dinamically_train_test_data()

        return test

    def __get_total_lines_by_percentage(self, value, percentage, use_ceil=False):
        if use_ceil is True:
            return ceil((value * percentage) / 100)

        return int((value * percentage) / 100)

    def __set_statically_train_test_data(self):
        amout_lines_to_train = self.__get_total_lines_by_percentage(self.dataframe_size,70)
        amout_lines_to_test = self.__get_total_lines_by_percentage(self.dataframe_size,30, True)

        train = self.dataframe.head(amout_lines_to_train)
        test = self.dataframe.tail(amout_lines_to_test)

        return [train, test]

    def get_statically_train_data(self):
        """Method to get statically train data"""

        train, _ = self.__set_statically_train_test_data()

        return train

    def get_statically_test_data(self):
        """Method to get statically test data"""
        _, test = self.__set_statically_train_test_data()

        return test
