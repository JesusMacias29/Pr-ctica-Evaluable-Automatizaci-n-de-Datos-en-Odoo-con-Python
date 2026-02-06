# Automatización de Datos en Odoo con Python 📊

---

## Autor 👤
JESÚS MACÍAS OJUELOS  DAM2

---

## Descripción del proyecto
En esta práctica se desarrolla un script en Python que implementa un proceso ETL (Extracción, Transformación y Carga) para importar un archivo CSV con datos de centros educativos a una base de datos PostgreSQL utilizada por Odoo. Todo el entorno se encuentra desplegado mediante Docker, garantizando una ejecución controlada y reproducible.

El script se encarga de leer el archivo CSV, crear automáticamente la tabla de destino si no existe e insertar los datos en la base de datos, asegurando que la transacción solo se confirme cuando el proceso se completa sin errores.

---

## Tecnologías utilizadas ⚙️
- Python 3.10 o superior  
- Docker Desktop  
- PostgreSQL  
- Odoo  
- pgAdmin 4  
- Librerías Python:
  - pandas  
  - psycopg2-binary  

---

## Estructura del repositorio 📁
El repositorio contiene los siguientes archivos:

├── importar.py

├── centros_educativos.csv

├── README.md

└── captura.png


---

## Preparación del entorno 🧪
Antes de ejecutar el script, se debe disponer de Python 3.10 o superior y tener Docker Desktop instalado y en funcionamiento.

Para instalar las dependencias necesarias, ejecutar el siguiente comando:

pip install pandas psycopg2-binary

---
## Configuración y ejecución ▶️
Verificar que los contenedores de Odoo y PostgreSQL están activos.

Comprobar que PostgreSQL expone el puerto 5432 al sistema anfitrión.

Desde la carpeta raíz del proyecto, ejecutar el script:

python importar.py
Si la ejecución es correcta, el script mostrará un mensaje indicando que la conexión con la base de datos se ha establecido correctamente y que los datos han sido cargados con éxito.

---

## Verificación de resultados en pgAdmin 🗄️
Para comprobar que el proceso ETL se ha realizado correctamente:

Abrir pgAdmin y conectarse al servidor PostgreSQL.

Acceder a la base de datos configurada en el script.

Ejecutar la siguiente consulta SQL:

SELECT * FROM import_centros;
La consulta mostrará los registros importados desde el archivo CSV, confirmando que los datos han sido insertados correctamente.

---

## Evidencia 📸
El repositorio incluye una captura de pantalla (captura.png) en la que se puede observar:

La ejecución correcta del script desde la terminal de VS Code.

El resultado de la consulta SELECT en pgAdmin mostrando los datos cargados.

La barra de tareas del sistema con la hora visible, como verificación de la autoría del trabajo.

---

## Conclusión
Con esta práctica se ha conseguido automatizar la carga de datos externos en Odoo mediante un proceso ETL desarrollado en Python, 
integrando correctamente Docker, PostgreSQL y herramientas de administración como pgAdmin. El proyecto demuestra la correcta conexión 
entre servicios, el tratamiento de archivos CSV y la persistencia segura de los datos en la base de datos, cumpliendo con los requisitos 
técnicos planteados en la actividad.


