# J'importe la librairie pandas pour en utiliser ses fonctions
import pandas as pd
# Import du fichier csv dans un dataframe
df = pd.read_csv('data/cinema.csv', sep=";", encoding="utf-8")
# On vérifie son import en lisant les 5 premières lignes
print(df.head())
# On ne garde que les colonnes nécessaires aux consignes
columns = ['commune', 'population de la commune', 'écrans', 'fauteuils', 'entrées 2022', 'entrées 2021']
df = df[columns]
# On se débarrasse des rangées ayant des données manquantes, afin de ne pas fausser les résultats 
df_cleaned = df.dropna()
# On vérifie le résultant en affichant les 5 premières lignes
print(df_cleaned.head())