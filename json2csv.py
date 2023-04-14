import json
import pandas as pd

# Leer archivo json
with open('test.json', 'r') as file:
    data = json.load(file)

# Convertir datos en DataFrame de pandas
df = pd.DataFrame(columns=['nombre', 'imagen'])
for key in data:
    df = df.append(pd.DataFrame({'nombre': [key], 'imagen': data[key]}), ignore_index=True)

# Exportar DataFrame a csv
df.to_csv('archivo.csv', index=False)