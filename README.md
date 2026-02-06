# Automatización de Datos en Odoo con Python 📊

En esta práctica se desarrolla un script en Python que implementa un proceso ETL (Extracción, Transformación y Carga) para importar un archivo CSV 
con datos de centros educativos a una base de datos PostgreSQL utilizada por Odoo. El entorno de ejecución se encuentra desplegado mediante Docker.

El script automatiza la lectura del CSV, la creación de la tabla de destino `import_centros` y la inserción de los datos, asegurando que la transacción 
se confirme únicamente si el proceso se completa sin errores.

## Tecnologías utilizadas ⚙️
- Python 3.10+
- Docker Desktop
- PostgreSQL
- Odoo
- pgAdmin 4
- Librerías: pandas y psycopg2-binary

## Contenido del repositorio 📁
- `importar.py`: script ETL en Python  
- `centros_educativos.csv`: archivo de datos de entrada  
- `README.md`: documentación del proyecto  
- `captura.png`: evidencia de ejecución y verificación  

## Ejecución del proyecto ▶️
1. Comprobar que los contenedores de Odoo y PostgreSQL están activos y que PostgreSQL expone el puerto 5432.
2. Instalar las dependencias necesarias:
```bash
pip install pandas psycopg2-binary
Ejecutar el script desde la carpeta del proyecto:

python importar.py
Al finalizar, el script muestra un mensaje indicando que la conexión y la carga de datos se han realizado correctamente.

Verificación en pgAdmin 🗄️
Para comprobar que los datos se han importado correctamente, se accede a pgAdmin y se ejecuta la siguiente consulta SQL sobre la base de datos configurada:

SELECT * FROM import_centros;
La consulta muestra los registros cargados desde el archivo CSV.

Evidencia 📸
La captura incluida en el repositorio muestra la ejecución correcta del script desde la terminal de VS Code, la consulta SELECT en pgAdmin con los
datos cargados y la barra de tareas del sistema con la hora visible para verificar la autoría.

Autor 👤
Práctica realizada como actividad evaluable de automatización de datos en Odoo con Python.
