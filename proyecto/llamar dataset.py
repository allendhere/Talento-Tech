import csv

# Ruta al archivo CSV
archivo_csv = 'proyecto/heart_attack_dataset.csv'

# Inicializamos contadores
contador_male = 0
contador_female = 0

with open(archivo_csv, encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    # Saltamos la primera línea (encabezados)
    next(lector)

    # Recorremos las filas del archivo
    for fila in lector:
        # La primera columna está en la posición 0
        valor_genero = fila[0]

        if valor_genero.lower() == 'male':
            contador_male += 1
        elif valor_genero.lower() == 'female':
            contador_female += 1

print(f"Hay {contador_male} registros 'Male' y {contador_female} registros 'Female'.")
