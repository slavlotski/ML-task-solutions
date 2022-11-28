import pandas as pd


def limit_gmv(dataframe: pd.DataFrame) -> pd.DataFrame:
    """Function to postprocessing gmv value"""

    limit_gmv_df = dataframe.copy()
    count_product = (limit_gmv_df.gmv / limit_gmv_df.price).astype(int)
    limit_gmv_df['gmv'] = limit_gmv_df.price * count_product.clip(upper = limit_gmv_df.stock)

    return limit_gmv_df
