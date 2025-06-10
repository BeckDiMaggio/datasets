from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_to_sqlserver

def run_etl():
    print("🟢 Iniciando ETL...")
    orders, items, products = extract_data()
    print("📥 Datos extraídos.")

    orders, items, products = transform_data(orders, items, products)
    print("🔧 Datos transformados.")

    load_to_sqlserver(orders, items, products)
    print("✅ ETL finalizado con éxito.")

if __name__ == "__main__":
    run_etl()