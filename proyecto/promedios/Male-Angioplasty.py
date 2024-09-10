import pandas as pd

df = pd.read_csv('C:/Users/boliv/OneDrive/Escritorio/github/Talento-Tech/proyecto/heart_attack_dataset.csv',encoding='latin1')

#  NO SIRVE:    df = pd.read_csv('../heart_attack_dataset.csv',encoding='latin1')


# Filtramos las filas correspondientes al tratamiento "Lifestyle Changes" y género masculino
tratamiento_lifestyle_hombres = df[(df['Treatment'] == 'Angioplasty') & (df['Gender'] == 'Male')]

# Contamos cuántos pacientes masculinos han recibido este tratamiento
cantidad_hombres_lifestyle = len(tratamiento_lifestyle_hombres)

print(f"La cantidad de hombres que han recibido el tratamiento 'Angioplasty' es: {cantidad_hombres_lifestyle}")

