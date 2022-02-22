"""
Tests of model.py
"""
import pandas as pd
import numpy as np
from pandas.core.frame import DataFrame
import pytest
from joblib import load
from ml.data import process_data
from ml.model import inference
import ml.utils as utils


@pytest.fixture
def data():
    """
    Read the dataset used for training
    """
    df = pd.read_csv("data_cleaned/census_cleaned.csv")
    return df


def test_colnames(data):
    """
    Check that the column names do not have whitespaces
    """
    assert set(data.columns) == set(data.columns.str.replace(' ', ''))


def test_used_cols(data):
    """
    Check that the columns in the training df are the same es the specified
    """
    assert set(data.columns) == set([*utils.predict_cols, *utils.target_col])


def test_nona(data):
    """
    Check that there are no na in data
    """
    assert data.shape[0] == data.dropna().shape[0]


def test_size_split(data):
    """
    Check that X and y have same number of rows when splitting
    """
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")

    X_test, y_test, _, _ = process_data(
        data,
        categorical_features=utils.cat_features,
        label="salary", encoder=encoder, lb=lb, training=False)

    assert len(X_test) == len(y_test)


def test_process_encoder(data):
    """
    Check that the saved encoder is the same as when trained
    """
    encoder_test = load("model/encoder.joblib")
    lb_test = load("model/lb.joblib")

    _, _, encoder, lb = process_data(
        data,
        categorical_features=utils.cat_features,
        label="salary", training=True)

    assert encoder.get_params() == encoder_test.get_params()
    assert lb.get_params() == lb_test.get_params()


def test_inference_above():
    """
    Check that inference is done correctly for >50K class
    """
    model = load("model/model.joblib")
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")

    # these tend to be features of >50k
    array = np.array([[
        38,
        "Private",
        "Doctorate",
        "Married-civ-spouse",
        "Exec-managerial",
        "Husband",
        "White",
        "Male",
        60,
        "United-States"]])
    df_temp = DataFrame(data=array, columns=utils.predict_cols)

    X, _, _, _ = process_data(
        df_temp,
        categorical_features=utils.cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(model, X)
    y = lb.inverse_transform(pred)[0]
    assert y == ">50K"


def test_inference_below():
    """
    Check that inference is done correctly for <=50K class
    """
    model = load("model/model.joblib")
    encoder = load("model/encoder.joblib")
    lb = load("model/lb.joblib")

    array = np.array([[
        19,
        "Private",
        "HS-grad",
        "Never-married",
        "Own-child",
        "Husband",
        "Black",
        "Male",
        0,
        "United-States"
    ]])

    df_temp = DataFrame(data=array, columns=utils.predict_cols)

    X, _, _, _ = process_data(
        df_temp,
        categorical_features=utils.cat_features,
        encoder=encoder, lb=lb, training=False)

    pred = inference(model, X)
    y = lb.inverse_transform(pred)[0]
    assert y == "<=50K"
