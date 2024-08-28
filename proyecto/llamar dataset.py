import csv

# Ruta al archivo CSV
archivo_csv = 'proyecto/heart_attack_dataset.csv'

# Inicializamos contadores
LifestyleChanges = 0
Angioplasty = 0

with open(archivo_csv, encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    # Saltamos la primera línea (encabezados)
    next(lector)

    # Recorremos las filas del archivo
    for column in lector:
        # La primera columna está en la posición 0
        valor_genero = column[7]

        if valor_genero.lower() == 'lifestyle changes':
            LifestyleChanges += 1
        elif valor_genero.lower() == 'angioplasty':
            Angioplasty += 1

        

print(f"Hay {LifestyleChanges} registros 'lifestyle changes' y {Angioplasty} registros 'angioplasty'.")
