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