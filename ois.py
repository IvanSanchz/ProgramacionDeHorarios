import csv
diccionario = {}
with open ("C:Direccion del archivo/Libro1.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        diccionario[row[0]] = row[1]

print(diccionario['Quimica'])