# Crivello di Eratostene 
'''
Elencare i primi n numeri primi, 
chiedendo n all'utente e implementando l'algoritmo del "Crivello di Eratostene"
'''

n = int(input("Inserisci un numero e ti restituirò una lista di numeri primi --> "))
lista_numeri_primi = [2]

for i in range(3, n + 1, 2):
    for y in lista_numeri_primi:
        if i % y == 0:
            break
    else:
        lista_numeri_primi.append(i)
        

print(f"I numeri primi fino a {n} sono: {lista_numeri_primi}")















