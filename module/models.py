import numpy as np
from sklearn.metrics import mean_squared_error

class IdealFunctionFitter:
    """
    A class to fit and predict ideal functions for given data.
    
    Attributes:
        training_data (ndarray): An array of shape (n_samples, 2) containing the training data.
        ideal_functions (list): A list of fifty ideal functions to choose from.
        chosen_functions (list): A list of four chosen ideal functions that are the best fit for the training data.
    """
    
    def __init__(self, training_data, ideal_functions):
        """
        Initializes the IdealFunctionFitter object with the given training data and ideal functions.
        
        Args:
            training_data (ndarray): An array of shape (n_samples, 2) containing the training data.
            ideal_functions (list): A list of fifty ideal functions to choose from.
        """
        self.training_data = training_data
        self.ideal_functions = ideal_functions
        self.chosen_functions = []
        
    def fit(self):
        """
        Chooses the four ideal functions which are the best fit out of the fifty provided.
        """
        # Choose the four ideal functions which are the best fit out of the fifty provided
        errors = []
        for f in self.ideal_functions:
            y_pred = f(self.training_data[:, 0])
            error = mean_squared_error(self.training_data[:, 1], y_pred)
            errors.append(error)
        best_functions_idx = np.argsort(errors)[:4]
        self.chosen_functions = [self.ideal_functions[i] for i in best_functions_idx]
        
    def predict(self, test_data):
        """
        Determines for each and every x-y pair of values in the test data whether or not they can be assigned to the four chosen ideal functions.
        
        Args:
            test_data (ndarray): An array of shape (n_samples, 2) containing the test data.
            
        Returns:
            results (list): A list of tuples containing the x-y pair, the chosen function, and the deviation for each test sample.
        """
        # Determine for each and every x-y pair of values whether or not they can be assigned to the four chosen ideal functions
        results = []
        for x, y in test_data:
            deviations = []
            for f in self.chosen_functions:
                y_pred = f(x)
                deviation = abs(y - y_pred)
                deviations.append(deviation)
            min_deviation_idx = np.argmin(deviations)
            min_deviation = deviations[min_deviation_idx]
            chosen_function = self.chosen_functions[min_deviation_idx]
            results.append((x, y, chosen_function, min_deviation))
        return results
    
    def visualize(self, results):
        """
        Visualizes all data logically.
        
        Args:
            results (list): A list of tuples containing the x-y pair, the chosen function, and the deviation for each test sample.
        """
        # Visualize all data logically
        import matplotlib.pyplot as plt
        x_train = self.training_data[:, 0]
        y_train = self.training_data[:, 1]
        plt.scatter(x_train, y_train, label='Training data')
        x_test = [r[0] for r in results]
        y_test = [r[1] for r in results]
        plt.scatter(x_test, y_test, label='Test data')
        for i, f in enumerate(self.chosen_functions):
            x = np.linspace(min(x_train), max(x_train), 100)
            y = f(x)
            plt.plot(x, y, label=f'Chosen function {i+1}')
        plt.legend()
        plt.show()

import pandas as np
