#Prueba

Brazilian E-Commerce Public Dataset by Olist ETL con Python
Este repositorio utiliza el dataset público de comercio electrónico brasileño de Olist para demostrar un flujo completo de trabajo: modelado de datos, automatización del proceso ETL, y visualización en Power BI.

Dataset: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce

Datasets utilizados en carpeta data:
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`

Requisitos:
Tener instalado SQL Server, SQL Manger Configuration, Python 3.X (up to date) y Power BI.

🐍 Python 3.x con las siguientes librerias
-Pandas:  para poder hacer uso
de lectura de los archivos .csv 
-squlalchemy: para hacer la conexión con Python y la base de datos SQL Server.
-pyobc: Conector obc para SQL Server
pip install pandas sqlalchemy pyodbc

🛢️ SQL Server:
-Crear base de datos con el nombre orders_db.
-Instancia local
-Sever name: localhost
-TCP/IP habilitado (enable)







