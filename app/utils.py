import pandas as pd
from .models import get_connection

def export_to_excel():
    connection = get_connection()
    query = "SELECT * FROM laptop_log"
    df = pd.read_sql(query, connection)
    connection.close()
    file_path = "Laptop_Log.xlsx"
    df.to_excel(file_path, index=False)
    return file_path 
