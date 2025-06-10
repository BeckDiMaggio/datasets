import pandas as pd

def transform_data(orders, items, products):
    # Normalizar nombres de columnas
    orders.columns = orders.columns.str.strip().str.lower().str.replace(" ", "_")
    items.columns = items.columns.str.strip().str.lower().str.replace(" ", "_")
    products.columns = products.columns.str.strip().str.lower().str.replace(" ", "_")

    # Convertir columnas de fecha en 'orders'
    for col in orders.columns:
        if 'date' in col or 'timestamp' in col:
            orders[col] = pd.to_datetime(orders[col], errors='coerce')

    # Fechas en items
    items['shipping_limit_date'] = pd.to_datetime(items['shipping_limit_date'], errors='coerce')

    #Transformar y agregar columna
    items['total_price'] = items['price'] + items['freight_value']
   
    # Eliminar filas con valores nulos 
    orders = orders.dropna(subset=['order_id'])
    items = items.dropna(subset=['order_id', 'product_id'])
    products = products.dropna(subset=['product_id'])

    # Verificar si quedaron vacíos
    if orders.empty or items.empty or products.empty:
        raise ValueError("Uno o más DataFrames están vacíos después de la limpieza.")

    return orders, items, products
