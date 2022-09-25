import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import acquire

def summarize(df, data='sales'):
    """ 
    """

    if data == 'sales':
        print(f"""
        Info: {df.info()}\n
        Nulls:\n{df.isnull().sum()}\n
        Unique Stores: {df.store_address.unique()}\n
        Unique Items: {df.item_name.unique()}\n
        Number of Sale Days: {df.index.nunique()}\n
        Sales Date Range: {df.index.min(), df.index.max()}\n
        """)
    elif data == 'ops':
        print(f"""
        {df.info()}
        Nulls:\n{df.isnull().sum()}\n
        """)

    for col in df.columns.to_list():
        df[col].hist()
        plt.title(col)
        plt.show();
        
    return

def engineer_features(df, data='sales'):
    """ 
    """

    df['month'] = df.index.strftime('%b')

    if data == 'sales':
        df['day of week'] = df.index.strftime('%a')
        df['sales_total'] = df.sale_amount * df.item_price   
    elif data == 'ops':
        df['year'] = df.index.strftime('%Y')
        
    return df 

def prepare (df, data='sales'):
    """ 
    """

    if data == 'sales':
        df.sale_date = pd.to_datetime(df.sale_date, format='%a, %d %b %Y %H:%M:%S %Z')
        df.sale_date = df.sale_date.dt.strftime('%Y-%m-%d').astype('datetime64')
        df = df.set_index('sale_date')
        df = df.drop(columns=['sale_id', 'store_id', 'item_id'])
    elif data == 'ops':
        df.Date = pd.to_datetime(df.Date)
        df = df.set_index('Date')
        df[df.index.year < 2011] = df[df.index.year < 2011].fillna(0)
        df['Solar'] = np.where(df.index.year == 2011, 0, df['Solar'])
        df['Wind+Solar'] = np.where(df.index.year == 2011, 0, df['Wind+Solar'])
        df = df.fillna(method='ffill')

    df = engineer_features(df, data)

    summarize(df, data)

    return df