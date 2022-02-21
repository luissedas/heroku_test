"""
Module Docstring
"""

from sklearn.metrics import fbeta_score, precision_score, recall_score
from sklearn.ensemble import RandomForestClassifier
import pandas as pd
from .data import process_data

# Optional: implement hyperparameter tuning.
def train_model(X_train, y_train):
    """
    Trains a machine learning model and returns it.

    Inputs
    ------
    X_train : np.array
        Training data.
    y_train : np.array
        Labels.
    Returns
    -------
    model
        Trained machine learning model.
    """
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    return model


def compute_model_metrics(y, preds):
    """
    Validates the trained machine learning model using precision, recall, and F1.

    Inputs
    ------
    y : np.array
        Known labels, binarized.
    preds : np.array
        Predicted labels, binarized.
    Returns
    -------
    precision : float
    recall : float
    fbeta : float
    """
    fbeta = fbeta_score(y, preds, beta=1, zero_division=1)
    precision = precision_score(y, preds, zero_division=1)
    recall = recall_score(y, preds, zero_division=1)
    return precision, recall, fbeta


def inference(model, X):
    """ Run model inferences and return the predictions.

    Inputs
    ------
    model : ???
        Trained machine learning model.
    X : np.array
        Data used for prediction.
    Returns
    -------
    preds : np.array
        Predictions from the model.
    """
    pred = model.predict(X)
    return pred

def slice_metrics(data, model, encoder, lb, cat_features):
    """Calculates metrics while slicing on categorical features

    Args:
        data (DataFrame): a dataframe to calculate metrics on
        model (RF): a machine learning model
        encoder (Encoder): an encoder of categorical features
        lb (LB): a label binarizer
        cat_features (list): a list of categorical features

    Returns:
        metrics_df (DataFrame): a dataframe containing all metrics
    """
    X, y, _, _ = process_data(
        data,
        categorical_features=cat_features,
        encoder=encoder,
        lb=lb,
        label="salary",
        training=False
    )
    metrics_data = []
    for col in cat_features:
        cat_vals = list(data[col].unique())
        for cat_val in cat_vals:
            value_index = data[data[col] == cat_val].index.values
            y_pred = inference(model, X[value_index])
            precision, recall, fbeta = compute_model_metrics(y[value_index], y_pred)
            metrics_data.append([col, cat_val, precision, recall, fbeta])
    metrics_df = pd.DataFrame(
        data=metrics_data,
        columns=['column', 'value', 'precision', 'recall', 'fbeta'])
    return metrics_df
