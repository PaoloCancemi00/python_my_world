# ESERCIZIO 1

class Persona:
    def __init__(self, nome, cognome, eta):
        self.nome = nome
        self.cognome = cognome
        self.eta = eta

    def informazioni(self):
        return self.nome + " " + self.cognome + " " + self.eta


persona = Persona("Marco", "Bianchi", "34")
print(persona.informazioni())

# ESERCIZIO 2

class Libro:

    def __init__(self, titolo, autore, pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.pubblicazione = pubblicazione

    def libro_recente(self):
        anni_recenti = ["2020", "2021", "2022", "2023", "2024"]
        if self.pubblicazione in anni_recenti:
            return f"Il libro {self.titolo} è recente"
        else:
            return f"Il libro {self.titolo} ha più di un quattro anni"
        
libro_uno = Libro("Klara and the Sun", "Kazuo Ishiguro", "2021" )
libro_due = Libro("To Kill a Mockingbird", "Harper Lee", "1960" )

print(libro_uno.libro_recente())
print(libro_due.libro_recente())

# ESERCIZIO 3

import math

class Cerchio:

    def __init__(self, raggio):
        self.raggio = raggio

    def area_cerchio(self):
        area = math.pi * self.raggio**2
        return area
    
    def circonferenza_cerchio(self):
        circonferenza = 2 * math.pi * self.raggio
        return circonferenza
    
cerchio = Cerchio(10)

print(f"L'area del cerchio è: {cerchio.area_cerchio()}")
print(f"La circonferenza del cerchio è: {cerchio.circonferenza_cerchio()}")

# ESERCIZIO 4 

class ContoBancario:
    def __init__(self, saldo_iniziale=0):
        self.saldo = saldo_iniziale # Gli importi vengono conserati qui fino alla fine del programma

    def deposita(self, importo):
        if importo > 0:
            self.saldo += importo
            print(f"Deposito di {importo} effettuato. Nuovo saldo: {self.saldo}")
        else:
            print("Importo non valido per il deposito.")

    def preleva(self, importo):
        if importo > 0 and importo <= self.saldo:
            self.saldo -= importo
            print(f"Prelievo di {importo} effettuato. Nuovo saldo: {self.saldo}")
        else:
            print("Importo non valido per il prelievo o saldo insufficiente.")


conto = ContoBancario(1000)

conto.deposita(500) # Il valore di importo viene assegnato qui dall' utente 
conto.preleva(200)
conto.deposita(1000)
conto.preleva(1500)

# ESERCIZIO 5

class Prodotto:

    def __init__(self, nome, prezzo, quantita_disponibile):
        self.nome = nome
        self.prezzo = prezzo
        self.quantita_disponibile = quantita_disponibile

    def valore_totale_prodotto(self, quantita): # valore totale prodotto all' acquisto
        if self.quantita_disponibile >= quantita:
            tot_valore = self.prezzo * quantita
            return f"Il costo complessivo di {quantita} prodotti è di {tot_valore}"
        else:
            return f"La quantita richiesta {quantita} non è disponibile in magazzino"
    
    def quantita_in_magazino(self, quantita):
        if self.quantita_disponibile >= quantita:
            return f"Scorte in magazzino: {self.quantita_disponibile}"
        else:
            return f"La quantita richiesta {quantita} non è disponibile in magazzino"

prodotto_uno = Prodotto("cuffiette sony", 35.50, 10)
prodotto_due = Prodotto("hard disk", 75, 6)
prodotto_tre = Prodotto("penna usb 128 GB", 9.99, 20)

print(prodotto_uno.valore_totale_prodotto(5))
print(prodotto_due.valore_totale_prodotto(7))
print(prodotto_tre.quantita_in_magazino(2))
print(prodotto_tre.quantita_in_magazino(24))

# ESERCIZIO 6

from random import randint 
import sys
import statistics
import matplotlib.pyplot as plt


# Esempio di automatizzazione
lista_numeri = []
k = randint(50,100)

for i in range(k):
    n = randint(1, 100)
    lista_numeri.append(n)

# Controllo in caso i dati inseriti tramite lista non fossero numeri !
def controllo_validita(lista_numeri):
    for i in lista_numeri:
        if not isinstance(i, (int, float)):
            print("La lista contiene dei valori non validi")
            sys.exit()
        
controllo_validita(lista_numeri)

# Creazione della classe e dei moduli per l'analisi dati

class Analisi_dati:

    def __init__(self, lista_numeri):
        self.lista_numeri = lista_numeri

    def valore_minimo(self):
        minimo = min(self.lista_numeri)
        return f"Il valore minimo è di {minimo}"
    
    def valore_massimo(self):
        massimo = max(self.lista_numeri)
        return f"Il valore massimo è di {massimo}"
    
    def media(self):
        media_tot = sum(self.lista_numeri) / len(self.lista_numeri)
        return f"La media è di: {round(media_tot, 2)}"
    
    def mediana(self):
        if len(self.lista_numeri) % 2 == 0:
            lista_ordinata = sorted(self.lista_numeri) 
            mediana_pari = (lista_ordinata[len(lista_ordinata) // 2 - 1] + lista_ordinata[len(lista_ordinata) // 2]) / 2
            return f"La mediana è di: {mediana_pari}"
        else:
            lista_ordinata = sorted(self.lista_numeri) 
            mediana_dispari = lista_ordinata[len(lista_ordinata) // 2]
            return f"La mediana è di: {mediana_dispari}"

    def moda(self):
        frequenza_moda = {}
        for i in self.lista_numeri:
            if i in frequenza_moda:
                frequenza_moda[i] += 1
            else:
                frequenza_moda[i] = 1
        
        moda = max(frequenza_moda, key=frequenza_moda.get)
            
        occorrenze_max = list(frequenza_moda.values()).count(frequenza_moda[moda])
        if occorrenze_max > 1:
            return f"Non c'è una moda unica."
        else:
            return f"La moda è: {moda}"
        
    def quartili(self):
        quartiles = statistics.quantiles(self.lista_numeri)
        return f"I tre quartili sono {quartiles}"
    
    def deviazione_standard(self):
        ds = statistics.stdev(self.lista_numeri)
        return f"La deviazione standard è di {round(ds, 2)}"
    
    def varianza(self):
        varianza = statistics.variance(self.lista_numeri)
        return f"La varianza è di {round(varianza, 2)}"
    
    def visualizza_istogramma(self):
        plt.hist(self.lista_numeri, bins=20, color='blue', edgecolor='black')
        plt.title('Distribuzione dei dati')
        plt.xlabel('Valore')
        plt.ylabel('Frequenza')
        plt.grid(True)
        plt.show()
    
    
analisi_dati = Analisi_dati(lista_numeri)

print(
    f"\nPresentazione della lista presa in esame:\n\n{lista_numeri}\n\n"
    f"{analisi_dati.valore_minimo()}\n"
    f"{analisi_dati.valore_massimo()}\n"
    f"{analisi_dati.quartili()}\n"
    f"{analisi_dati.media()}\n"
    f"{analisi_dati.mediana()}\n"
    f"{analisi_dati.moda()}\n"
    f"{analisi_dati.deviazione_standard()}\n"
    f"{analisi_dati.varianza()}\n"
)

print(f"{analisi_dati.visualizza_istogramma()}")