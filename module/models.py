from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier

class Models:
    """
    A machine learning class that can create regression, logistic regression, and decision tree models using scikit-learn.
    
    Parameters
    ----------
    model_type : str
        The type of model to create. Can be one of 'regression', 'logistic_regression', 'decision_tree_regression', or 'decision_tree_classification'.
    **kwargs : dict
        Additional keyword arguments to pass to the model constructor.
    """
    def __init__(self, model_type: str, **kwargs):
        self.model_type = model_type
        self.kwargs = kwargs
        self.model = None

    def create_model(self):
        """
        Creates an instance of the specified model type using scikit-learn.
        """
        if self.model_type == 'regression':
            self.model = LinearRegression(**self.kwargs)
        elif self.model_type == 'logistic_regression':
            self.model = LogisticRegression(**self.kwargs)
        elif self.model_type == 'decision_tree_regression':
            self.model = DecisionTreeRegressor(**self.kwargs)
        elif self.model_type == 'decision_tree_classification':
            self.model = DecisionTreeClassifier(**self.kwargs)
        else:
            raise ValueError(f"Invalid model type: {self.model_type}")

    def fit(self, X, y):
        """
        Fits the model to the training data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The training data.
        y : array-like of shape (n_samples,)
            The target values.
        """
        if not self.model:
            raise ValueError("Model not created. Call create_model() first.")
        self.model.fit(X, y)

    def predict(self, X):
        """
        Makes predictions on new data.
        
        Parameters
        ----------
        X : array-like of shape (n_samples, n_features)
            The data to make predictions on.
        
        Returns
        -------
        y_pred : array-like of shape (n_samples,)
            The predicted values.
        """
        if not self.model:
            raise ValueError("Model not created. Call create_model() first.")
        return self.model.predict(X)
