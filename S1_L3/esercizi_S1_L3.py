# Esercizio 1 (1/3)
# Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while.

for i in range(0, 21, 1):
    print(i)

# Esercizio 1 (2/3)
# Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.

for i in range(0, 11, 1):
    print(2 ** i)

# Esercizio 1 (3/3)
# Memorizza e stampa tutti i divisori di un numero dato in input. 
# Esempio: • input: 150 • output: [2, 3, 5, 5]

numero = int(input("Inserisci un numero per trovare i suoi divisori --> "))
lista_divisori = []

for i in range(1, numero+1, 1):
    if numero % i == 0:
        lista_divisori.append(i)

print(lista_divisori)

# Esercizio 2

'''
Creiamo un dizionario che assegni ad ogni proprietario la sua auto, 
sapendo che: 
• Ada guida una Punto 
• Ben guida una Multipla 
• Charlie guida una Golf 
• Debbie guida una 107 
Stampiamo il dizionario per intero, e poi l'auto associata a Debbie.
'''

dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

print(dizionario_auto)
print(dizionario_auto["Debbie"])

# Esercizio 3
'''
Abbiamo un dizionario che assegna ad ogni proprietario la sua 
auto: dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"} 
Con un ciclo, e usando il metodo .values(), 
stampiamo a video tutte le auto che non sono una Multipla.
'''
dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107"}

for i in dizionario_auto.values():
    if i == "Multipla":
        continue
    else:
        print(i)

# Esercizio 4

'''
Abbiamo due dizionari che assegnano ad ogni proprietario la propria 
auto: dizionario_auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"} 
Aggiornare il dizionario dizionario_auto con i dati contenuti in nuovi_proprietari e stamparlo. 
Cosa è successo a Ben?
'''

auto = {"Ada": "Punto", "Ben": "Multipla", "Charlie": "Golf", "Debbie": "107", "Emily": "A1"} 
nuovi_proprietari = {"Ben": "Polo", "Fred": "Octavia", "Grace": "Yaris", "Hugh": "Clio"} 

auto["Ben"] = "Polo"
auto["Fred"] = "Octavia"
auto["Grace"] = "Yaris"
auto["Hugh"] = "Clio"

print(auto)

# Il valore di Ben è stato aggiornato cambiando da Multipla a Polo

# Esercizio 5
# Scrivere una funzione che, data una lista di numeri, 
# fornisca in output il minimo e il massimo (possiamo usare o meno le funzioni min() e max() nel corpo).
from random import randint

lista_numeri = []

for i in range(10):
    n = randint(1, 100)
    lista_numeri.append(n)

def max_min(lista_numeri):
    massimo = max(lista_numeri)
    minimo = min(lista_numeri)
    return massimo, minimo

print(f"Il numero massimo e il numero minimo sono {max_min(lista_numeri)}")

# ESERCIZIO 5 SENZA MAX() E MIN()

from random import randint

lista_numeri = []

for i in range(10):
    n = randint(1, 100)
    lista_numeri.append(n)

def minimo(parametro):
    n = None
    for i in parametro:
        if n == None:
            n = i
        elif i < n:
            n = i
    return n

def massimo(parametro):
    n = None
    for i in parametro:
        if n == None:
            n = i
        elif i > n:
            n = i
    return n

print("Il massimo ed il minimo è", minimo(lista_numeri))
print("Il massimo ed il massimo è", massimo(lista_numeri))

# Esercizio 6
''' 
Scrivere una funzione che, data una lista di numeri, 
fornisca in output i tre numeri più grandi;
gestire il caso in cui la lista sia più corta di tre, 
e quando uno o più dei numeri selezionati sono uguali.
'''

lista_numeri = [1, 5, 8, 15, 6, 9, 10]

def max_tre(lista):
    if len(lista) > 3:
        lista_ordinata = sorted(lista, reverse=True)
        lista_pulita = set(lista_ordinata[:3])
    else:
        print("Inserire una lista di almeno 3 numeri")
    return lista_pulita

print(f"I tre numeri più grandi nella lista sono: {max_tre(lista_numeri)}")

# Esercizio 7

'''
Scrivere una funzione che in input acquisisce una lista di numeri e un numero K; 
in output, dovrà restituire la media di tutti i numeri nella lista maggiori o uguali a K; 
se non ce ne dovesse essere nessuno, dovrà stampare a schermo un messaggio adeguato.
'''
from random import randint, choice

lista_di_numeri = []
possibili_k = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
k = choice(possibili_k)

for i in range(10):
    n = randint(1, 100)
    lista_di_numeri.append(n)

def media_k(lista_di_numeri, k):
    valori_sopra_k = []
    for i in lista_di_numeri:
        if i >= k:
            valori_sopra_k.append(i)
        
    if len(valori_sopra_k) > 1:
        media_valori = sum(valori_sopra_k) / len(valori_sopra_k)
        return f"La media di valori è {media_valori}"
    else:
        return "Ci sono meno di 2 valori superiore a k, impossibile fare la media"

print(media_k(lista_di_numeri, k))

# Esercizio 8

'''
Scrivere una funzione che, data una lista di numeri, 
come output stamperà lo stesso numero di asterischi su righe diverse, 
ottenendo una semplice visualizzazione grafica Esempio, 
supponendo di chiamare la funzione 
"aster()": numeri = [5, 2, 3, 4] aster(numeri) 

Output:
***** 
** 
*** 
****

'''

from random import randint

lista_numeri = []

for i in range(10):
    n = randint(1, 25)
    lista_numeri.append(n)

def aster(lista_numeri):
    for i in lista_numeri:
        print("*"*i)

print(lista_numeri)
aster(lista_numeri)

