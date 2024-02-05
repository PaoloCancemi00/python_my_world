# ESERCIZIO 2
'''
Trasformiamo la lista dell'esercizio precedente 
mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9] [10, 11, 12, 13, 14]] in un array 
NumPy: mat = np.array(mat) 
Come facciamo per accedere ai singoli elementi?
'''
import numpy as np

mat = [[0, 1, 2, 3, 4], [5, 6, 7, 8, 9], [10, 11, 12, 13, 14]]
mat = np.array(mat)

elem_1 = mat[0, 4]
print(elem_1) # restituisce 4

elem_2 = mat[1, :]
print(elem_2) # restituisce tutti gli elementi della amtrice interna con indice 1

elem_2 = mat[2, 2:4]
print(elem_2) # Restituisce 12 e 13