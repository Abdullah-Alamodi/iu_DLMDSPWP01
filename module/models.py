import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

class IdealFunctionSelector:
    """
    A class to select the best ideal functions from a set of provided ideal functions.
    """
    def __init__(self, train_data, ideal_data, test_data):
        """
        Initializes the IdealFunctionSelector with the provided train, ideal and test data.
        
        :param train_data: The train data as a DataFrame, csv file or numpy array.
        :param ideal_data: The ideal data as a DataFrame, csv file or numpy array.
        :param test_data: The test data as a DataFrame, csv file or numpy array.
        """
        if isinstance(train_data, pd.DataFrame):
            self.train_data = train_data
        elif isinstance(train_data, str):
            self.train_data = pd.read_csv(train_data)
        elif isinstance(train_data, np.ndarray):
            self.train_data = pd.DataFrame(train_data)
            
        if isinstance(ideal_data, pd.DataFrame):
            self.ideal_data = ideal_data
        elif isinstance(ideal_data, str):
            self.ideal_data = pd.read_csv(ideal_data)
        elif isinstance(ideal_data, np.ndarray):
            self.ideal_data = pd.DataFrame(ideal_data)
            
        if isinstance(test_data, pd.DataFrame):
            self.test_data = test_data
        elif isinstance(test_data, str):
            self.test_data = pd.read_csv(test_data)
        elif isinstance(test_data, np.ndarray):
            self.test_data = pd.DataFrame(test_data)

        
    def select_ideal_functions(self):
        """
        Selects the best ideal functions from the provided ideal functions.
        
        :return: A list of the indices of the selected ideal functions.
        """
        # Calculate the mean squared error for each ideal function
        mse = []
        for i in range(1, 51):
            y_pred = self.ideal_data[f'y{i}']
            mse_i = 0
            for j in range(1, 5):
                y_true = self.train_data[f'y{j}']
                mse_i += mean_squared_error(y_true, y_pred)
            mse.append(mse_i)
            
        # Select the four ideal functions with the lowest mean squared error
        selected_functions = np.argsort(mse)[:4]

        print(selected_functions)
        return selected_functions
    
    def map_test_data(self, selected_functions):
        """
        Maps the test data to the selected ideal functions and calculates the deviation.
        
        :param selected_functions: A list of the indices of the selected ideal functions.
        :return: A DataFrame containing the mapped test data and deviation.
        """
        # Map the test data to the selected ideal functions
        mapped_test_data = self.test_data.copy()
        for i in selected_functions:
            y_pred = self.ideal_data[f'y{i}']
            deviation = np.abs(mapped_test_data['y'] - y_pred)
            mapped_test_data[f'deviation_{i}'] = deviation

        print(mapped_test_data)    
        return mapped_test_data
    
    def visualize(self, selected_functions, mapped_test_data):
        """
        Visualizes the train, test and ideal data.
        
        :param selected_functions: A list of the indices of the selected ideal functions.
        :param mapped_test_data: A DataFrame containing the mapped test data and deviation.
        """
        # Plot the train data
        plt.figure(figsize=(12, 8))
        plt.plot(self.train_data['x'], self.train_data['y1'], label='Train y1')
        plt.plot(self.train_data['x'], self.train_data['y2'], label='Train y2')
        plt.plot(self.train_data['x'], self.train_data['y3'], label='Train y3')
        plt.plot(self.train_data['x'], self.train_data['y4'], label='Train y4')
        
        # Plot the test data
        plt.scatter(self.test_data['x'], self.test_data['y'], label='Test', color='k')
        
        # Plot the selected ideal functions
        for i in selected_functions:
            plt.plot(self.ideal_data['x'], self.ideal_data[f'y{i}'], label=f'Ideal {i}')
            
        # Plot the deviation
        for i in selected_functions:
            plt.fill_between(mapped_test_data['x'], mapped_test_data[f'y'] - mapped_test_data[f'deviation_{i}'], mapped_test_data[f'y'] + mapped_test_data[f'deviation_{i}'], alpha=0.2)
            
        plt.legend()

    
