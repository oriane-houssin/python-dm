import pandas as pd
# J'importe la librairie matplotlib.pyplot
import matplotlib.pyplot as plt

# Reprise du code de l'exercice 1
df = pd.read_csv('data/cinema.csv', sep=";", encoding="utf-8")
columns = ['commune', 'population de la commune', 'écrans', 'fauteuils', 'entrées 2022', 'entrées 2021']
df = df[columns]
df_cleaned = df.dropna()

# Création de la colonne 'entrées moyennes/fauteuil 2022' avec pour données le nombre d'entrées 2022 divisé par le nombre de fauteuil pour chaque cinéma
df_cleaned['entrées moyennes/fauteuil 2022'] = df_cleaned['entrées 2022']/df_cleaned['fauteuils']
# Je vérifie le bon fonctionnement de mon code en affichant les 5 premières lignes du dataframe
#print(df_cleaned.head())
# Je choisis les colonnes qui me seront nécessaires pour cet exercice
columns_commune = ['commune', 'fauteuils', 'entrées 2022', 'entrées moyennes/fauteuil 2022']
# Je crée un dataframe avec les colonnes qui m'intéressent
df_communes = df_cleaned[columns_commune]
# Je vérifie
#print(df_communes.head())
# J'utilise la fonction d'aggrégation pour regrouper les données par commune, en faisant la somme des données de chaque commune
df_communes = df_communes.groupby('commune').sum().reset_index()
# Je vérifie
#print(df_communes.head())

# Je trie le dataframe par le nombre d'entrées moyennes/fauteuil 2022 grâce de manière décroissante
df_best = df_communes.sort_values(by=['entrées moyennes/fauteuil 2022'], ascending=False)
# Les trois meilleures
print('Les trois communes ayant les meilleurs résultats en termes d entrées moyennes par fauteuil')
print(df_best.head(3))

# Je trie le dataframe par le nombre d'entrées moyennes/fauteuil 2022 grâce de manière croissante
df_worst = df_communes.sort_values(by=['entrées moyennes/fauteuil 2022'])
# Les trois pires
print('Les trois communes ayant les pires résultats en termes d entrées moyennes par fauteuil')
print(df_worst.head(3))

df_10_best = df_best.head(10)
# Afficher sous forme de graphique en barres
best_bar = plt.bar(df_10_best['commune'], df_10_best['entrées moyennes/fauteuil 2022'])
plt.title('Top 10 des communes ayant le meilleur résultat entrées moyennes/fauteuil 2022')
plt.xlabel('Communes')
plt.ylabel('Moyenne entrées/fauteuil 2022')
plt.savefig('exercice_2_bar.png')
plt.close()



