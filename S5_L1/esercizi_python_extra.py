# ESERCIZIO 1

'''
# Calcolo del BMI:
peso = float(input("Inserisci il tuo peso in kg --> "))
altezza = float(input("Inserisci la tua altezza in metri --> "))

bmi = peso/altezza**2

print(f"Il tuo BMI è di {bmi}")

'''

# ESERCIZIO 2

'''
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
'''

# ESERCIZIO 3

'''
# Conteggio delle vocali:
lista_vocali = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U",]
testo = "Nel cuore di una cittadina tranquilla, sorgeva una vecchia biblioteca circondata da alberi secolari. Le pagine ingiallite dei libri custodivano storie dimenticate e segreti antichi. I visitatori potevano immergersi in mondi lontani sfogliando libri polverosi. Un giorno, una giovane studiosa, affascinata dalla storia locale, scoprì un manoscritto dimenticato che raccontava di un tesoro nascosto nei sotterranei della biblioteca. La scoperta la spinse in un'avventura intricata tra corridoi segreti e indovinelli misteriosi. Alla fine, trovò un baule antico che conteneva non solo ricchezze materiali, ma anche la saggezza del passato."
contatore = 0

for lettera in testo:
    if lettera in lista_vocali:
        contatore += 1

print(f"Le vocali in totale sono {contatore}")
'''

# ESERCIZIO 4
'''
# Lista inversa (senza reverse)
import random

lista_numeri = [random.randint(1, 100) for _ in range(10)]
print(lista_numeri)

lista_inversa = lista_numeri[::-1]
print(lista_inversa)
'''



# ESERCIZIO 5 

'''
def disegna_linea(punto1, punto2):
    x1, y1 = punto1
    x2, y2 = punto2

    pendenza = (y2 - y1) / (x2 - x1) if (x2 - x1) != 0 else float('inf')

    if abs(pendenza) > 1:
        print("La pendenza è troppo elevata per disegnare la linea.")
        return

    print(" " * int(x1) + "*", end="")
    for x in range(int(x1) + 1, int(x2)):
        y = int(y1 + pendenza * (x - x1))
        print("\n" + " " * x + "*" + " " * (y - x))

    print("\n" + " " * int(x2) + "*")

# Esempio di utilizzo
punto1 = (2, 5)
punto2 = (8, 10)
disegna_linea(punto1, punto2)
'''



