import pandas as pd

df = pd.read_csv('C:/Users/boliv/OneDrive/Escritorio/github/Talento-Tech/proyecto/heart_attack_dataset.csv', encoding='latin1')

tratamiento_lifestyle_hombres = df[(df['Treatment'] == 'Medication') & (df['Gender'] == 'Male')]
cantidad_hombres_lifestyle = len(tratamiento_lifestyle_hombres)

print(f"La cantidad de hombres que han recibido el tratamiento 'Medicacion' es: {cantidad_hombres_lifestyle}")