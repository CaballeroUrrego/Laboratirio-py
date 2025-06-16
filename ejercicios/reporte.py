import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

# 1. Cargar variables de entorno desde el archivo .env
load_dotenv()

usuario = os.getenv("DB_USER")
contraseña = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
base_de_datos = os.getenv("DB_NAME")
puerto = os.getenv("DB_PORT")

# 2. Crear el engine de SQLAlchemy para conectar pandas con MySQL
engine = create_engine(f"mysql+mysqlconnector://{usuario}:{contraseña}@{host}:{puerto}/{base_de_datos}")

# 3. Leer la tabla 'diccionario_campos' en un DataFrame de pandas
diccionario = pd.read_sql("SELECT * FROM diccionario_campos", engine)

# 4. Mostrar las primeras filas para verificar la estructura
print("Primeras filas del diccionario de datos:")
print(diccionario.head())

# 5. Ejercicio: Análisis del diccionario de datos

# a) ¿Cuántos campos tiene cada tabla?
campos_por_tabla = diccionario.groupby('tabla')['campo'].count()
print("\nCantidad de campos por tabla:")
print(campos_por_tabla)

# b) ¿Cuáles son los campos tipo DECIMAL en todas las tablas?
campos_decimal = diccionario[diccionario['tipo_dato'].str.contains('DECIMAL', case=False)]
print("\nCampos tipo DECIMAL:")
print(campos_decimal[['tabla', 'campo', 'tipo_dato']])

# c) ¿Cuáles campos tienen la palabra 'correo' en la descripción?
campos_correo = diccionario[diccionario['descripcion'].str.contains('correo', case=False, na=False)]
print("\nCampos relacionados con correo:")
print(campos_correo[['tabla', 'campo', 'descripcion']])

# d) ¿Cuáles son los campos de la tabla 'Pagador'?
campos_pagador = diccionario[diccionario['tabla'] == 'Pagador']
print("\nCampos de la tabla Pagador:")
print(campos_pagador[['campo', 'tipo_dato', 'descripcion']])

# e) Guardar un resumen en Excel
resumen = {
    "campos_por_tabla": campos_por_tabla,
    "campos_decimal": campos_decimal,
    "campos_correo": campos_correo,
    "campos_pagador": campos_pagador
}

# Guardar cada análisis en una hoja diferente de un archivo Excel
with pd.ExcelWriter("resumen_diccionario.xlsx") as writer:
    campos_por_tabla.to_frame().to_excel(writer, sheet_name="Campos por tabla")
    campos_decimal.to_excel(writer, sheet_name="Campos DECIMAL", index=False)
    campos_correo.to_excel(writer, sheet_name="Campos correo", index=False)
    campos_pagador.to_excel(writer, sheet_name="Pagador", index=False)

print("\nResumen guardado en 'resumen_diccionario.xlsx'")