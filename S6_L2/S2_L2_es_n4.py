# ESERCIZIO 4
'''
Esercizio In una catena di montaggio abbiamo una struttura metallica di 28.75 cm di lunghezza;
per assicurarne la stabilità, è necessario inserire 15 rivetti, 
dei quali uno all'inizio e uno alla fine, e tutti quanti separati dalla stessa distanza; 
come possiamo calcolare i punti esatti in cui inserire i rivetti tramite NumPy?
'''
import numpy as np 


distanza_tra_i_rivetti = np.linspace(0, 28.75, 15)
print(f"\n Matrice non arrotondata \n{distanza_tra_i_rivetti}")

'''
[ 0.          2.05357143  4.10714286  6.16071429  8.21428571 10.26785714 
12.32142857 14.375      16.42857143 18.48214286 20.53571429 22.58928571 
24.64285714 26.69642857 28.75      ]
'''

matrice = distanza_tra_i_rivetti.reshape(3, 5)
matrice_arrotondata = np.round(matrice, 3)

print(f"\n Matrice arrotondata \n{matrice_arrotondata}")

'''
[[ 0.    2.05  4.11  6.16  8.21]
 [10.27 12.32 14.37 16.43 18.48]
 [20.54 22.59 24.64 26.7  28.75]]
'''