import pandas as pd


def fillna_with_mean(df: pd.DataFrame, target: str, group: str) -> pd.DataFrame:
    """Fillna values in the target grouping by category feature."""
    dataframe_copy = df.copy()
    mean_target_transform = dataframe_copy.groupby(group)[target].transform("mean")
    dataframe_copy[target] = dataframe_copy[target].fillna(mean_target_transform)
    # Используем transform, чтобы на выходе получался датафрейм того же размера что и на входе
    return dataframe_copy
