# Libraries to import
import os
import pandas as pd
import numpy as np
import rampwf as rw

# Assuming you have the configuration parameter 'workflow'
# set to 'regressor' in your problem.yml

from sklearn.model_selection import GroupShuffleSplit

# Problem title
problem_title = "Coral Bleaching Prediction"

# Type of prediction: regression
Predictions = rw.prediction_types.make_regression()

# Workflow: regressor
workflow = rw.workflows.Regressor()

# Scoring: rmse and normalized rmse
score_types = [
    rw.score_types.RMSE(name="rmse", precision=3),
    rw.score_types.NormalizedRMSE(name="Nrmse", precision=3)
]



_target_column_name = 'Percent_Bleached'
_ignore_column_names = ["Sample_ID","Site_ID"]

# I/O method for data

groups = None

def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name),sep=";")
    data = data.iloc[:, 2:]
    y_array = data[_target_column_name].values
    X_df = data.drop([_target_column_name] + _ignore_column_names, axis=1)
    X_df=X_df.to_numpy()
    return X_df, y_array


def get_train_data(path='.'):
    data = pd.read_csv(os.path.join(path, "data", "train.csv"),sep=";")
    data_df = data.copy()
    data_df["Sample_ID"] = data_df["Sample_ID"].astype("category")
    Site_ID = np.array(data_df["Sample_ID"].cat.codes)
    global groups
    groups = Site_ID
    f_name = 'train.csv'
    return _read_data(path, f_name)


def get_test_data(path='.'):
    f_name = 'test.csv'
    return _read_data(path, f_name)


def get_cv(X, y):
    cv = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=1234)
    return cv.split(X, y,groups)
