import pandas as pd

df = pd.read_csv('C:/Users/boliv/OneDrive/Escritorio/github/Talento-Tech/proyecto/heart_attack_dataset.csv', encoding='latin1')

tratamiento_lifestyle_hombres = df[(df['Treatment'] == 'Angioplasty') & (df['Gender'] == 'Female')]
cantidad_hombres_lifestyle = len(tratamiento_lifestyle_hombres)

print(f"La cantidad de mujeres que han recibido el tratamiento 'Angioplasty' es: {cantidad_hombres_lifestyle}")
