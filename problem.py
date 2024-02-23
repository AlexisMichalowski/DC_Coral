# library to import
import os
import pandas as pd
import rampwf as rw

# Assuming you have the configuration parameter 'workflow'
# set to 'regressor' in your problem.yml

# a modifier si on change de cv
from sklearn.model_selection import GroupShuffleSplit

# Problem title
problem_title = "Coral Bleaching Prediction"

# Type of prediction: regression
Predictions = rw.prediction_types.make_regression()

# workflow: regressor
workflow = rw.workflows.Regressor()

# scoring: We'll have to choose, for now: rmse and normalized rmse
score_types = [
    rw.score_types.RMSE(name="rmse", precision=3),
    rw.score_types.NormalizedRMSE(name="Nrmse", precision=3)
]

# define cross validation??


def get_cv(X, y):
    # a verifier? faut il specifier les groupes
    cv = GroupShuffleSplit(n_splits=5, test_size=0.2, random_state=1234)
    return cv.split(X, y)


_target_column_name = 'Percent_Bleached'
_ignore_column_names = []  # a rajouter, voir code rémi

# I/O method for data


def _read_data(path, f_name):
    data = pd.read_csv(os.path.join(path, 'data', f_name))
    y_array = data[_target_column_name].values
    X_df = data.drop([_target_column_name] + _ignore_column_names, axis=1)
    return X_df, y_array


def get_train_data(path='.'):
    f_name = 'train.csv'
    return _read_data(path, f_name)


def get_test_data(path='.'):
    f_name = 'test.csv'
    return _read_data(path, f_name)
