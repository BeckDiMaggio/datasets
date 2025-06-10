import pandas as pd

def extract_data():
    orders = pd.read_csv('./data/olist_orders_dataset.csv')
    items = pd.read_csv('./data/olist_order_items_dataset.csv')
    products = pd.read_csv('./data/olist_products_dataset.csv')
    return orders, items, products