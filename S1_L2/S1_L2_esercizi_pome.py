# Esercizio 1
# Abbiamo la stringa  nome_scuola = "Epicode"
# Stampare ogni carattere della stringa, uno su ogni riga, utilizzando un costrutto while.

nome_scuola = "Epicode"
lunghezza = 0

while lunghezza < len(nome_scuola):
    print(nome_scuola[lunghezza])
    lunghezza += 1

# Esercizio 2 
# Stampare a video tutti i numeri da 0 a 20 utilizzando il costrutto while.

numero = 0

while numero < 21:
    print(numero)
    numero += 1

# Esercizio 3
# Calcolare e stampare tutte le prime 10 potenze di 2 (e.g., 2⁰, 2¹, 2², …) utilizzando un ciclo while.

numero_contatore = 0

while numero_contatore < 11:
    print(2 ** numero_contatore)
    numero_contatore += 1

# Esercizio 4
# Calcolare e stampare tutte le prime N potenze di 2 utilizzando un ciclo while,
# domandando all'utente di inserire N.

n = int(input("Inserisci un numero intero che sarà l'esponente di 2 --> "))

while n >= 0:
    print(2**n)
    n -= 1

# Esercizio 5
# Calcolare e stampare tutte le potenze di 2 minori di 25000.

inizio = 0
potenza = 0

while potenza < 25000:
    potenza = (2**inizio)
    if potenza < 25000:
        print(potenza)
    else:
        break
    inizio += 1

# Esercizio 6  
# Abbiamo due liste, una di studenti e una di corsi: 

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend"]

corsi.append("Frontend")
corsi.append("Cybersecurity")

if len(studenti) == len(corsi):
    print("Le liste hanno la stessa lunghezza")
    print(corsi)
else:
    print("Le liste hanno lunghezze differenti")

# Esercizio 7
'''
Scriviamo un programma che chiede in input all'utente una stringa 
e visualizza i primi 3 caratteri, seguiti da 3 punti di sospensione 
e quindi gli ultimi 3 caratteri (Stavolta facciamo attenzione a tutti i casi particolari, 
ovvero implementare soluzioni ad hoc per stringhe di lunghezza inferiore a 6 caratteri)
'''
while True:

    parola_utente = input("Inserisci una parola oppure Q o q per chiudere (consigliati almeno 3 caratteri --> ")
    
    if parola_utente == "Q" or parola_utente == "q":
        print("Chiusura attivata il programma cesserà le sue funzionalità")
        break
    elif len(parola_utente) >= 7:
        concatenazione = parola_utente[0:3] + "..." + parola_utente[-3:]
        print(concatenazione)
    elif len(parola_utente) >= 5:
        concatenazione = parola_utente[0:2] + "..." + parola_utente[-2:]
        print(concatenazione)
    elif len(parola_utente) >= 3:
        concatenazione = parola_utente[0:1] + "..." + parola_utente[-1:]
        print(concatenazione)
    else:
        print("La parola è composta da meno di 3 caratteri")


# Esercizio 8
# Memorizza e stampa tutti i divisori di un numero dato in input. 
# Esempio: • input: 150 • output: [2, 3, 5, 5]

numero = int(input("Inserisci un numero per trovare i suoi divisori --> "))
contatore = 1
lista_divisori = []

while contatore <= numero:
    if numero % contatore == 0:
        lista_divisori.append(contatore)
        contatore += 1
    else:
        contatore += 1
        continue
    

print(lista_divisori)

# Esercizio 9

'''
Calcolare (ma non stampare) le prime N potenze di K; 
ognuna di esse andrà memorizzata in coda a una lista. 
Alla fine, stampare la lista risultante. 
Proviamo con diversi valori di K, oppure facciamola inserire all'utente.
'''

k = float(input("Inserisci la base della potenza --> "))
n = float(input("Inserisci l'esponente della potenza --> "))

lista_pot_k =[]


while n >= 0:
    lista_pot_k.append(k**n)
    n -= 1

print(lista_pot_k)

# Esercizio 10

'''
Abbiamo una lista con i guadagni degli ultimi 12 mesi: 
guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
usando un costrutto while, calcolare la media dei guadagni e stamparla a video.
'''

guadagni = [100, 90, 70, 40, 50, 80, 90, 120, 80, 20, 50, 50] 
somma = 0
i = 0

while i < len(guadagni):
    somma += guadagni[i]
    i += 1



media = somma/len(guadagni)
print(media)

# Esercizio 11

'''
Abbiamo una lista di codici fiscali: lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", 
"MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"] • 
trovare i codici fiscali che contengono "95", metterli in una lista, e alla fine stamparla; 
• inoltre, per ognuno di essi, stampare a video i caratteri relativi al nome e quelli relativi al cognome.
'''

lista_cf = ["ABCDEF95G01A123B", "GHIJKL91M02A321C", "MNOPQR89S03A456D", "STUVWX95Z04A654E", "XYZABC01D05A789F", "DEFGHI95J06A987G"]

lista_95 = []
contatore = 1

for i in lista_cf:
    if "95" in i:
        lista_95.append(i)

print(lista_95)

for i in lista_cf:
    cognome = i[0:3]
    nome = i[3:6]
    print(f"L' utente {contatore} ha come lettere nel nome : {nome} e nel cognome {cognome}")
    contatore += 1

# Esercizio 12
'''
Abbiamo tre liste della stessa lunghezza, 
dove ogni elemento nella medesima posizione si riferisce ai dati dello stesso 
studente: studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"] 
edizioni = [1, 2, 3, 2, 2, 1, 3, 3] 
• Stampare a video tutti e soli gli studenti che frequentano una prima edizione; 
non tutti i dati potrebbero essere necessari. 
• Riuscite a vedere una similarità con la logica che si usa in SQL e le tabelle relazionali?
'''

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry"] 
corsi = ["Cybersecurity", "Data Analyst", "Backend", "Frontend", "Data Analyst", "Backend", "Frontend", "Cybersecurity"] 
edizioni = [1, 2, 3, 2, 2, 1, 3, 3] 

contatore = 0

for i in edizioni:
    if i == 1:
        print(studenti[contatore])
    contatore  += 1

# La similitudine sta nel fatto che le liste funzionano in questo caso come le tabelle in SQL 
# permettendoci di analizzare specularmente gli elementi che si troverebbero allo stesso indice di riga"

# Esercizio 13
'''
Abbiamo una lista di stringhe di prezzi in dollari, 
che erroneamente sono stati scritti con il simbolo dell'euro: 
prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] 
cambiare il simbolo dell'euro (€) in quello del dollaro ($) 
per ogni stringa nella lista; il risultato sarà memorizzato in un'altra lista.
''' 

prezzi = ["100 €", "200 €", "500 €", "10 €", "50 €", "70 €"] 
lista_corretta = []

for i in prezzi:
    dollaro = i.replace("€", "$")
    lista_corretta.append(dollaro)

print(lista_corretta)

# Esercizio 14

'''
Abbiamo una lista di studenti: 
studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"] 
vogliamo dividere gli studenti in due squadre per un campionato di Uno nel seguente modo: 
selezioneremo i nomi in posizione pari per un squadra, 
e i nomi in posizione dispari per l'altra. 
Creiamo due liste per ogni squadra, e alla fine visualizziamole.
'''

studenti = ["Alex", "Bob", "Cindy", "Dan", "Emma", "Faith", "Grace", "Henry", "Isabelle", "John"]
contatore = 1
squadra_dispari = []
squadra_pari = []

for i in studenti:
    if contatore % 2 == 0:
        squadra_pari.append(i)
        contatore += 1
    elif contatore % 2 == 1:
        squadra_dispari.append(i)
        contatore += 1

print(squadra_dispari)
print(squadra_pari)


