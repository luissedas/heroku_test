"""Script to train machine learning model."""

from sklearn.model_selection import train_test_split
import pandas as pd
import joblib
from starter.data import process_data
from starter.model import train_model
import starter.utils as utils

# Add code to load in the data.
data = pd.read_csv('data_cleaned/census_cleaned.csv')

data = data[utils.predict_cols + utils.target_col]

# Optional enhancement, use K-fold cross validation instead of a train-test split.
train, test = train_test_split(data, test_size=0.20)

X_train, y_train, encoder, lb = process_data(
    train, categorical_features=utils.cat_features, label="salary", training=True
)

# Proces the test data with the process_data function.
X_test, y_test, _, _ = process_data(
    test, categorical_features=utils.cat_features, label="salary", training=False,
    encoder=encoder, lb=lb
)

# Train and save a model.
model = train_model(X_train, y_train)
joblib.dump(model, 'model/model.joblib')
joblib.dump(encoder, 'model/encoder.joblib')
joblib.dump(lb, 'model/lb.joblib')
