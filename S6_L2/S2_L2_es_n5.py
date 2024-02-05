# ESERCIZIO 5
'''
Esercizio Abbiamo la seguente matrice: Creiamo un ndarray con gli stessi valori. 
Ci sono due modalità: inizializzare un array e poi inserire i valori nelle posizioni adatte,
oppure creare una lista di liste e poi effettuare un casting.
'''

import numpy as np

# Metodo 1

dimensioni = (3, 4)
matrice_ndarray = np.empty(dimensioni)
matrice_ndarray[0, 0] = 1
matrice_ndarray[0, 1] = 1
matrice_ndarray[0, 2] = 1
matrice_ndarray[0, 3] = 1
matrice_ndarray[1, 0] = 5
matrice_ndarray[1, 1] = 1
matrice_ndarray[1, 2] = 1
matrice_ndarray[1, 3] = 1
matrice_ndarray[2, 0] = 20
matrice_ndarray[2, 1] = -4
matrice_ndarray[2, 2] = 0
matrice_ndarray[2, 3] = 42

matrice_arrotondata = np.round(matrice_ndarray)
print(f"\n Metodo 1 \n{matrice_arrotondata}")

# Metodo 2
lista = [[1, 1, 1, 1], [5, 1, 1, 1], [20, -4, 0, 42]]
ndarray = np.array(lista)
print(f"\n Metodo 2 \n{ndarray}")