# ESERCIZIO 3
'''
Esercizio Abbiamo il seguente array NumPy: 
linear_data = np.array([x for x in range(27)]) 
Lo ridimensioniamo mediante il metodo .reshape(): 
reshaped_data = linear_data.reshape((3, 3, 3)) 
Quante dimensioni ha il nuovo array? 
Come facciamo per accedere ai singoli elementi?
'''
import numpy as np

linear_data = np.array([x for x in range(27)]) 

reshaped_data = linear_data.reshape((3, 3, 3))  # CREA UNA MATRICE 3 X 3 X 3 OVVERO 3 MATRICI CON OGIUNA 3 RIGHE E 3 COLONNE
print(reshaped_data)

# Quante dimensioni ha il nuovo array? 

'''
Ci sono 3 dimensioni in totale

Dimensione 1: 3 (i "livelli" o "strati" dell'array).
Dimensione 2: 3 (le righe di ciascuna matrice).
Dimensione 3: 3 (le colonne di ciascuna matrice).

'''

# Come facciamo per accedere ai singoli elementi?

print(f"\n Valore singolo estratto dall' array: {reshaped_data[0, 1, 2]} in posizione [0, 1, 2] nella matrice di riferimento") # Il risultato è 5

'''

Questo comando indica:
0) Prendi la matrice a indice 0 (ovvero la prima dell' array)
1) Prendi la riga ad indice 1 
2) Prendi l' elemento ad indice 2 dentro la prima riga

[[[ 0  1  2]
    [ 3  4  5]
    [ 6  7  8]]

    [[ 9 10 11]
    [12 13 14]
    [15 16 17]]

    [[18 19 20]
    [21 22 23]
    [24 25 26]]]

'''