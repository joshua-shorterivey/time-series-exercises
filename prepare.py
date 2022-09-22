import pandas as pd
import numpy as np
import requests
import acquire

def summarize(df):
    """ 
    """

    print(f"""
    Shape: {df.shape}\n
    Nulls:\n{df.isnull().sum()}\n
    Unique Stores: {df.store_id.unique()}\n
    Unique Items: {df.item_id.unique()}\n
    Number of Sales Days: {df.index.nunique()}\n
    Sales Date Range: {df.index.min(), df.index.max()}\n
    """)
    df.hist()
    
    return

def engineer_features(df):
    """ 
    """

    df['month'] = df.index.strftime('%b')
    df['day of week'] = df.index.strftime('%a')
    df['sales_total'] = df.sale_amount * df.item_price
    
    return df 

def prepare (df):
    """ 
    """

    df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
    df.sale_date = df.sale_date.dt.strftime('%Y-%m-%d').astype('datetime64')
    df = df.set_index('sale_date')

    df = engineer_features(df)

    summarize(df)

    return df