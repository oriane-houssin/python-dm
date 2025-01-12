import pandas as pd
import matplotlib.pyplot as plt
# J'importe seaborn
import seaborn as sn

# Reprise du code de l'exercice 1
df = pd.read_csv('data/cinema.csv', sep=";", encoding="utf-8")
columns = ['commune', 'population de la commune', 'écrans', 'fauteuils', 'entrées 2022', 'entrées 2021']
df = df[columns]
df_cleaned = df.dropna()

# On ne garde que l'année 2022
columns_2022 = ['commune', 'population de la commune', 'écrans', 'fauteuils', 'entrées 2022']
df_2022 = df_cleaned[columns_2022]
# Je vérifie
print(df_2022.head())

# Corrélation entrées écrans
entrees_ecrans = df_2022['écrans'].corr(df_2022['entrées 2022'])
print('Corrélation entre le nombre d écrans et le nombre d entrées annuelles 2022:')
print(entrees_ecrans)
# Corrélation fauteuils écrans
entrees_fauteuils = df_2022['fauteuils'].corr(df_2022['entrées 2022'])
print('Corrélation entre le nombre de fauteuils et le nombre d entrées annuelles 2022:')
print(entrees_fauteuils)

sn.regplot(data=df_2022, x='écrans', y='entrées 2022')
plt.title = 'Corrélation entre le nombre d écrans et le nombre d entrées annuelle 2022'
plt.xlabel = 'Ecrans'
plt.ylabel = 'Entrées 2022'
plt.savefig('exercice_3_corr_1.png')
plt.close()

sn.regplot(data=df_2022, x='fauteuils', y='entrées 2022')
plt.title = 'Corrélation entre le nombre de fauteuils et le nombre d entrées annuelle 2022'
plt.xlabel = 'Fauteuils'
plt.ylabel = 'Entrées 2022'
plt.savefig('exercice_3_corr_2.png')
plt.close()
