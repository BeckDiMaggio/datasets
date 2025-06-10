from sqlalchemy import create_engine

def load_to_sqlserver(orders, items, products):
    server = 'localhost' 
    database = 'orders_db'
    driver = 'ODBC Driver 17 for SQL Server'

    connection_string = f"mssql+pyodbc://@{server}/{database}?driver={driver}&trusted_connection=yes"
    engine = create_engine(connection_string)

    orders.to_sql('orders', con=engine, if_exists='replace', index=False)
    items.to_sql('order_items', con=engine, if_exists='replace', index=False)
    products.to_sql('products', con=engine, if_exists='replace', index=False)
    print("✅ Datos cargados exitosamente en SQL Server.")