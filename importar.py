import pandas as pd
import psycopg2

# Credenciales de PostgreSQL
db_config = {
    "host": "localhost",
    "database": "postgres",
    "user": "odoo",
    "password": "odoo",
    "port": 5432
}

archivo_csv = "listado.csv"

try:
    # Leer CSV con latin1
    df = pd.read_csv(archivo_csv, encoding="latin1")
    print("CSV leído correctamente")

    # Conectar con PostgreSQL
    conexion = psycopg2.connect(**db_config)
    cursor = conexion.cursor()

    # Crear tabla si no existe
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS import_centros (
        id SERIAL PRIMARY KEY,
        col1 TEXT,
        col2 TEXT,
        col3 TEXT,
        col4 TEXT,
        col5 TEXT
    );
    """)

    # Insertar datos usando iloc
    for i in range(len(df)):
        cursor.execute("""
        INSERT INTO import_centros (col1, col2, col3, col4, col5)
        VALUES (%s,%s,%s,%s,%s)
        """, (
            str(df.iloc[i,0]),
            str(df.iloc[i,1]),
            str(df.iloc[i,2]),
            str(df.iloc[i,3]),
            str(df.iloc[i,4])
        ))

    conexion.commit()
    print("Datos insertados correctamente")

except Exception as e:
    print("Error:", e)

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()