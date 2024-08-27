import csv


# Ruta al archivo CSV
archivo_csv = 'proyecto/heart_attack_dataset.csv'


with open(archivo_csv, encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    primera_columna = next(lector)  # Obtenemos la primera línea


    # Buscamos el índice de la columna de género (asumiendo que es la primera columna)
    genero = 0


    # Inicializamos contadores
    contador_male = 0
    contador_female = 0


    # Recorremos la primera línea
    for valor in primera_columna:
        if valor.lower() == 'Male':
            contador_male += 1
        elif valor.lower() == 'Female':
            contador_female += 1
           


    print(f"hay {contador_male} registros 'Male' y {contador_female} registros 'Female'.")
