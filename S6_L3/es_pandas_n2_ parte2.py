# Esercizio " (2/2)
'''
Dal dataset di prima: 
• Leggiamo il file e carichiamolo in un DataFrame, 
aggiungendo i nomi di colonna — che si trovano nel file .names — come parametro di pd.read_csv() 
• Stampiamo le prime cinque righe e le ultime dieci 
• Stampiamo un riepilogo dei descrittori statistici del dataset
'''

import pandas as pd
import numpy as np

iris = pd.read_csv("Dataset/iris/iris.data", header=None)

nuovi_nomi_colonna = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'class']
iris = iris.set_axis(nuovi_nomi_colonna, axis=1) # Cambia l'indice delle colonne nel DataFrame axis = 1 (colonna) axis = 0 (riga)

colonne_numeriche = iris.select_dtypes(include='number')
moda_colonne_numeriche = colonne_numeriche.mode().iloc[0]

print("\nModa:")
print(f"{np.round(moda_colonne_numeriche, 2)}\n")

print(f"Esempio di loc \n {iris.loc[2:4]} ")
print(f"Esempio di iloc \n {iris.iloc[:6]} ")

print(iris)
print(iris.head())
print(iris.tail(10))
print(round(iris.describe(), 3))

