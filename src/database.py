import pandas as pd

from math import ceil
from sklearn.model_selection import train_test_split 

class Database:
    dataframe = pd.DataFrame()
  
    def __init__(self, file_path):
        self.dataframe = pd.read_csv(file_path)
        self.dataframe_size = len(self.dataframe.index)

    def __set_dinamically_train_test_data(self):
        train, test = train_test_split(self.dataframe, test_size=0.3, train_size=0.7, random_state=42)
        
        return [train, test]

    def get_dinamically_train_data(self):
        train, _ = self.__set_dinamically_train_test_data()

        return train
    
    def get_dinamically_test_data(self):
        _, test = self.__set_dinamically_train_test_data()

        return test
    
    def __set_statically_train_test_data(self):
        amout_lines_to_train = ceil(self.dataframe_size * 70 / 100)
        amout_lines_to_test = int(self.dataframe_size * 30 / 100)

        train = self.dataframe.head(amout_lines_to_train)
        test = self.dataframe.tail(amout_lines_to_test)

        return [train, test]
    
    def get_statically_train_data(self):
        train, _ = self.__set_statically_train_test_data()

        return train

    def get_statically_test_data(self):
        _, test = self.__set_statically_train_test_data()

        return test