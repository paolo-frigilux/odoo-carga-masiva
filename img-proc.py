import sys
import json

if len(sys.argv) != 3:
    print("Uso correcto:")
    print("python ./img-proc.py ./archivo-de-entrada ./archivo-de-salida.json")
    exit()

data = {}
inputFile = sys.argv[1]
outputFile = sys.argv[2]

with open(inputFile, "r") as f:
    for line in f:
        if line.startswith("#"):
            key = line.strip("#").strip()
            data[key] = []
        else:
            data[key].append(line.strip())

with open(outputFile, "w") as f:
    json.dump(data, f)