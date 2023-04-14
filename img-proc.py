import sys
import json

if sys.argv != 3:
    print("Uso correcto:")
    print("python ./img-proc.py ./archivo-de-entrada ./archivo-de-salida.json")

data = {}

with open("img.temp") as f:
    for line in f:
        if line.startswith("#"):
            key = line.strip("#").strip()
            data[key] = []
        else:
            data[key].append(line.strip())

with open("tunuevoarchivo.json", "w") as f:
    json.dump(data, f)