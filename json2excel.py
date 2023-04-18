import pandas as pd
import json

# Leer la tabla de Excel
df = pd.read_excel('plantilla-swarovski.xlsx', sheet_name='Sheet1')

# Cargar el archivo JSON
with open('test.json') as f:
    data = json.load(f)

# Crear una tabla vacia para almacenar los DataFrames
dfs_list = pd.DataFrame(columns = df.columns)

# Iterar sobre las llaves del objeto y crear un DataFrame para cada una de ellas
for key in data:
    # Buscar una coincidencia en la columna Ref del DataFrame
    mask = df['Referencia interna'].apply(str) == key
    if mask.any():
        for index, row in df[mask].iterrows():
            new_df = pd.DataFrame(index=range(len(data[key])), columns=df.columns)
            new_df.iloc[0] = row
            new_df['Imagen del Open Graph del sitio'] = pd.Series(data[key])
            dfs_list = dfs_list.append(new_df)

# Exportar el DataFrame resultante a un archivo de Excel
dfs_list.to_excel('resultado.xlsx', index=False)