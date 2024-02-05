# Esercizio 1 
# Abbiamo 25 studenti; memorizzare questo dato in una variabile.

studenti = 25

# Esercizio 2
# Abbiamo 25 studenti; memorizzare questo dato in una variabile e stamparla a video.

studenti = 25
print(studenti)

# Esercizio 3 
# Abbiamo 25 studenti; memorizzare questo dato in una variabile. 
# Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile.

studenti = 25
studenti_extra = 3

# Esercizio 4
# Abbiamo 25 studenti; memorizzare questo dato in una variabile. Arrivano altri 3 studenti; memorizzare questo dato in un'altra variabile. 
# Creare un'altra variabile ancora che conterrà la somma delle prime due, poi stamparla a video.

studenti = 25
studenti_extra = 3
tot_studenti = studenti + studenti_extra
print(tot_studenti)

# Esercizio 5
# Creare una variabile che contiene la stringa "Epicode", quindi stamparla a video.

stringa = "Epicode"
print(stringa)

# Esercizio 6
# Creare, a mano, una lista che contenga i numeri da 0 a 5, 
# memorizzarla in una variabile e infine stamparla a video.

lista = [0, 1, 2, 3, 4, 5]
print(lista)

# Esercizio 7
# Stampare l'iniziale

nome_scuola = "Epicode"
print(stringa[0])

# Esercizio 8
# Stampare le prime tre lettere.

nome_scuola = "Epicode"
print(stringa[0:3])

# Esercizio 9
# Incrementarla di 2 e poi moltiplicarla per 3 Usare due metodi diversi (ad esempio,
# uno utilizzando gli operatori di assegnazione, e uno senza)

x = 10
x += 2
x *= 3
print(x)

x = (10 + 2) * 3
print(x)

# Esercizio 10
# Scriviamo un programma che chiede in input all'utente una stringa e visualizza 
# i primi 3 caratteri, seguiti da 3 punti di sospensione e quindi gli ultimi 3 caratteri.

parola = input("Inserisci la parola --> ")
concatenazione = parola[0:3] + "..." + parola[-3:]
print(concatenazione)

# Esercizio 11
# Verificare, per ognuna delle seguenti stringhe, 
# se il numero di caratteri è compreso tra 5 e 8:

lista_caratteri = ["Windows", "Excel", "Powerpoint", "Word"]

for i in lista_caratteri:
    if len(i) >= 5 and len(i) <= 8:
        print(f"{i} è compreso tra i 5 e 8 caratteri")
    elif len(i) < 5:
        print(f"{i} è minore di 5 caratteri")
    else:
        print(f"{i} è maggiore di 8 caratteri")
    
# Esercizio 12
# Calcolatrice semplice

while True:
    calcolatrice = input("Inserire +, -, *, /, ** in base all'operazione desiderata, digita Q oppure q per uscire dal programma --> ")
    simbolo_validi = ["+", "-", "*", "/", "**", "Q", "q" ]
    if calcolatrice not in simbolo_validi:
        print("Inserire un'operazione valida")
        continue
    elif calcolatrice == "Q" or "q":
        break
    numero_1 = float(input("Inserisci il primo numero --> "))
    numero_2 = float(input("Inserisci il secondo numero --> "))
    if calcolatrice == "+":
        print(numero_1 + numero_2)
    elif calcolatrice == "-":
        print(numero_1 - numero_2)
    elif calcolatrice == "*":
        print(numero_1 * numero_2)
    elif calcolatrice == "/":
        print(numero_1 / numero_2)
    else:
        print(numero_1 ** numero_2)

# Esercizio 13
        
'''
Un utente inserisce tre parole e il programma produce in output la prima in maiuscolo,
la seconda in minuscolo e la terza con 
l'iniziale maiuscola. Poi prende i primi tre caratteri di ognuna e li stampa a video

'''
parole = input("Inserisci 3 nomi: ").split()

if len(parole) == 3:
    print(parole[0].upper())
    print(parole[1].lower())
    print(parole[2].capitalize())
else:
    print("Inserisci 3 nomi.")

# Esercizio 14
# Un utente inserisce tre parole e il programma stampa il prodotto delle lunghezze delle parole.

# Metodo 1
parola1 = input("Inserisci la prima parola: ")
parola2 = input("Inserisci la seconda parola: ")
parola3 = input("Inserisci la terza parola: ")

lunghezza_prodotto = len(parola1) * len(parola2) * len(parola3)

print("Il prodotto delle lunghezze delle parole è:", lunghezza_prodotto)

# Metodo 2
parole = input("Inserisci 3 nomi: ").split()
totale_lettere = 1

for i in parole:
    totale_lettere = len(i) * totale_lettere

print(totale_lettere)

