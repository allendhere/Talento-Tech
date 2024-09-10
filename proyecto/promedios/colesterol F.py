

'C:/Users/boliv/OneDrive/Escritorio/github/Talento-Tech/proyecto/heart_attack_dataset.csv'
import pandas as pd

df = pd.read_csv('C:/Users/boliv/OneDrive/Escritorio/github/Talento-Tech/proyecto/heart_attack_dataset.csv',encoding='latin1')

# Hago un DataFrame llamado 'df'
# Se filtran pacientes masculinos
df_masculinos = df[df['Gender'] == 'Female']

# Calcular el promedio del colesterol para pacientes masculinos
promedio_colesterol_masculinos = df_masculinos['Cholesterol (mg/dL)'].mean()

print(f"El promedio del colesterol para pacientes masculinos es: {promedio_colesterol_masculinos:.2f} mg/dL")
