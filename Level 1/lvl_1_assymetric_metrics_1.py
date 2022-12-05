import numpy as np

def turnover_error(y_true: np.array, y_pred: np.array) -> float:
    """Custom RMSLE metric"""
    if len(y_true) == len(y_pred):
        y_true = np.array([np.log1p(value) + 1 for value in y_true])
        y_pred = np.array([np.log1p(value) + 1 for value in y_pred])
        if not np.isnan(y_true).any() and not np.isnan(y_pred).any():
            error = np.sqrt(np.mean((y_pred - y_true)**2))

    return error
