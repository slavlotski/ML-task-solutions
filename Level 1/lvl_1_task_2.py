import numpy as np

def smape (y_true: np.array, y_pred: np.array) -> float:
    
    numerator = 2 * np.abs(y_true - y_pred)
    denominator = (np.abs(y_true) + np.abs(y_pred))
    denominator[denominator == 0.0] = 1.0  # Деление на 0 приведет к ошибке или nan значению
    
    return np.mean(numerator / denominator)