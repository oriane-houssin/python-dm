import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

# Reprise du code de l'exercice 1
df = pd.read_csv('data/cinema.csv', sep=";", encoding="utf-8")
columns = ['commune', 'population de la commune', 'écrans', 'fauteuils', 'entrées 2022', 'entrées 2021']
df = df[columns]
df_cleaned = df.dropna()

# Division en deux sous-ensembles
columns_exp = ['écrans', 'fauteuils', 'population de la commune']
X = df_cleaned[columns_exp]

columns_cible = ['entrées 2022', 'entrées 2021']
Y = df_cleaned[columns_cible]

# Je traine les données
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=42)

# Je fais un modèle de régression linéaire
model = LinearRegression()
model.fit(X_train, Y_train)

Y_pred = model.predict(X_test)

r2 = r2_score(Y_test, Y_pred)
mae = mean_absolute_error(Y_test, Y_pred)

print(f"R²: {r2}")
print(f"MAE: {mae}")

# Prédictions
Y_pred_2022, Y_pred_2021 = model.predict(X).T

df_cleaned['entrées prédites 2022'] = Y_pred_2022
df_cleaned['entrées prédites 2021'] = Y_pred_2021

# J'enregistre dans un fichier csv
df_cleaned.to_csv('cinemas_predictions.csv', index=False, sep=';')

# Je vérifie
print(df_cleaned)
