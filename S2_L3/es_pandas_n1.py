# Esercizio 1
'''
Esercizio Andiamo a questo link e scarichiamo una serie di dataset: 
https://www.kaggle.com/datasets/ahmettezcantekin/beginner-datasets 
Tra i vari dataset presenti, ce n'è uno che contiene diverse qualità di vini 
e le misure di diverse proprietà organolettiche: wine.csv; 
Effettuiamo calcoliamo le informazioni statistiche base 
(numerosità, modie, mode, mediane, quartili, ecc) 
sulle colonne numeriche usando python 
'''
import pandas as pd
import numpy as np

vini = pd.read_csv("Dataset/wine.csv")
print(vini)

pd.set_option('display.max_columns', None) #SERVE PER VISUALIZZARE TUTTE LE COLONNE SENZA CHE VENGANO TRONCATE
print(np.round(vini.describe(), 3))




