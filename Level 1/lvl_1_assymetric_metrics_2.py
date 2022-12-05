import numpy as np

def ltv_error(y_true: np.array, y_pred: np.array) -> float:
    """Custom LTV metric"""

    return np.mean(np.abs((y_true**2) - ((y_pred)**2)))
