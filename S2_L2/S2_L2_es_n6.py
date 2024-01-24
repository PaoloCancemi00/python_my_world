# ESERCIZIO 6
'''
# Creiamo il seguente ndarray 5x5: 
Per ogni valore, sottraiamo il minimo (2) e poi dividiamo il risultato 
per il massimo (42) meno il minimo. 
'''

# METODO STEP BY STEP

import numpy as np

lista = [[10, 22, 21, 8, 9], [9, 42, 3, 18, 11], [5, 4, 30, 12, 29], [37, 31, 7, 2, 26], [8, 6, 4, 33, 15]]
ndarray = np.array(lista)

massimo = np.max(ndarray)
minimo = np.min(ndarray)
massimo_meno_minimo = massimo - minimo


ndarray_meno_minimo = np.subtract(ndarray, minimo)
ndarray_finale = ndarray_meno_minimo / massimo_meno_minimo

print(f" \n Metodo 1 \n{ndarray_finale} \n")

# OTTIMIZZAZIONE

lista = [[10, 22, 21, 8, 9], [9, 42, 3, 18, 11], [5, 4, 30, 12, 29], [37, 31, 7, 2, 26], [8, 6, 4, 33, 15]]
ndarray = np.array(lista)

ndarray_ottimizzato = (np.subtract(ndarray, minimo))/(np.max(ndarray) - np.min(ndarray))
print(f" Metodo 2 \n{ndarray_ottimizzato} \n")
