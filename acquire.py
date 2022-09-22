import numpy as np
import pandas as pd
import requests

from os import path

def acquire_items_data():

    #pull information/payload from the url
    response = requests.get('https://python.zgulde.net/api/v1/items')

    #use .json to turn into dictionary if underlying infomration is in RESTful format
    data = response.json()

    #create variables that will hold the payload sub dictionary information
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']

    base_url = 'https://python.zgulde.net'

    #create items dataframe to hold data from payload['items'] dictionary
    items = pd.DataFrame(data['payload']['items'])

    for page in range(current_page, max_page):
        response = requests.get(base_url + next_page)   
        data = response.json()
        items = pd.concat([items, pd.DataFrame(data['payload']['items'])], ignore_index=True)
        next_page = data['payload']['next_page']
        if type(next_page) is None:
            break


    return items

def acquire_store_data():

    #pull information/payload from the url
    response = requests.get('https://python.zgulde.net/api/v1/stores')

    #use .json to turn into dictionary if underlying infomration is in RESTful format
    data = response.json()

    #create variables that will hold the payload sub dictionary information
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']

    base_url = 'https://python.zgulde.net'

    #create items dataframe to hold data from payload['items'] dictionary
    stores = pd.DataFrame(data['payload']['stores'])

    for page in range(current_page, max_page):
        response = requests.get(base_url + next_page)   
        data = response.json()
        stores = pd.concat([stores, pd.DataFrame(data['payload']['stores'])], ignore_index=True)
        next_page = data['payload']['next_page']
        if next_page is None:
            break


    return stores

def acquire_sales_data():


    if path.exists('sales.csv'):
        sales = pd.read_csv('sales.csv')
        return sales

    #pull information/payload from the url
    response = requests.get('https://python.zgulde.net/api/v1/sales')

    #use .json to turn into dictionary if underlying infomration is in RESTful format
    data = response.json()

    #create variables that will hold the payload sub dictionary information
    current_page = data['payload']['page']
    next_page = data['payload']['next_page']
    max_page = data['payload']['max_page']

    base_url = 'https://python.zgulde.net'

    #create items dataframe to hold data from payload['items'] dictionary
    sales = pd.DataFrame(data_sales['payload']['sales'])    
    sales_list = []

    for page in range(current_page_sales, max_page_sales):
        response = requests.get(base_url + next_page_sales)   
        data = response.json()
        #sales = pd.concat([sales, pd.DataFrame(data_sales['payload']['sales'])])
        sales_list.extend(data['payload']['sales'])
        next_page_sales = data['payload']['next_page']
        if next_page_sales is None:
            break

    sales = pd.concat([sales, pd.DataFrame(sales_list)])
    sales = sales.rename(columns={'item':'item_id', 'store': 'store_id'})

    return sales

def acquire_all_data():

    items = acquire_items_data()
    stores = acquire_store_data()
    sales = acquire_sales_data()

    df = pd.merge(sales, items, how='left', on='item_id')

    df = pd.merge(df, stores, how='left', on='store_id')

    return df

def acquire_energy():
    
    url = 'https://raw.githubusercontent.com/jenfly/opsd/master/opsd_germany_daily.csv'

    df = pd.read_csv(url)

    return df