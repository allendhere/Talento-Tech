import csv

# Ruta al archivo CSV
archivo_csv = 'proyecto/heart_attack_dataset.csv'

# Inicializamos contadores
Lifestyle_Changes = 0
Angioplasty = 0
Coronary_Artery_Bypass_Graft_CABG = 0
Medication = 0

with open(archivo_csv, encoding='latin1') as fichero_csv:
    lector = csv.reader(fichero_csv)
    # Saltamos la primera línea (encabezados)
    next(lector)

    # Recorremos las filas del archivo
    for fila in lector:
        # La primera columna está en la posición 0
        valor_genero = fila[7]

        if valor_genero.lower() == 'lifestyle changes':
            Lifestyle_Changes += 1
        elif valor_genero.lower() == 'angioplasty':
            Angioplasty += 1
        elif valor_genero.lower() == 'coronary artery bypass graft (cabg)':
            Coronary_Artery_Bypass_Graft_CABG += 1
        elif valor_genero.lower() == 'medication':
            Medication += 1

print(f"{Lifestyle_Changes} registros 'Lifestyle Changes'.")
print(f"{Angioplasty} registros 'Angioplasty'.")
print(f"{Coronary_Artery_Bypass_Graft_CABG} registros 'Coronary Artery Bypass Graft (CABG)'")
print(f"{Medication} registros 'Medication'.")
