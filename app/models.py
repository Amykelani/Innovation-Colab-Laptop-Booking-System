import mysql.connector
from .config import Config

def get_connection():
    config = {
        'host': Config.MYSQL_HOST,
        'user': Config.MYSQL_USER,
        'password': Config.MYSQL_PASSWORD,
        'database': Config.MYSQL_DATABASE,
    }
    return mysql.connector.connect(**config)

def init_db():
    connection = mysql.connector.connect(
        host=Config.MYSQL_HOST,
        user=Config.MYSQL_USER,
        password=Config.MYSQL_PASSWORD
    )
    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {Config.MYSQL_DATABASE}")
    cursor.close()
    connection.close()

    connection = get_connection()
    cursor = connection.cursor()
    create_table_query = """
    CREATE TABLE IF NOT EXISTS laptop_log (
        id INT AUTO_INCREMENT PRIMARY KEY,
        laptop VARCHAR(255) NOT NULL,
        serial_number VARCHAR(255) NOT NULL,
        code VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
    )
    """
    cursor.execute(create_table_query)
    connection.commit()
    cursor.close()
    connection.close()

def insert_record(laptop, serial_number, code, password_value):
    connection = get_connection()
    cursor = connection.cursor()
    insert_query = """
    INSERT INTO laptop_log (laptop, , serial_number, code, password)
    VALUES (%s, %s, %s, %s)
    """
    cursor.execute(insert_query, (laptop, serial_number, code, password_value))
    connection.commit()
    cursor.close()
    connection.close() 
