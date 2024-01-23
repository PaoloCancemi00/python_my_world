# scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 --> output: milleduecentotrentaquattro

# METODO 1

def translate_to_20(n):
    if n > 19:
        return "Out of range"

    NUMBERS = ["", "uno", "due", "tre", "quattro", "cinque", "sei", "sette",
               "otto", "nove", "dieci", "undici", "dodici", "tredici",
               "quattordici", "quindici", "sedici", "diciassette",
               "diciotto", "diciannove"]
    return NUMBERS[n]

def translate_to_100(n):
    if n < 20:
        return translate_to_20(n)
    if n > 99:
        return "Out of range"
    
    DECADES = ["venti", "trenta", "quaranta", "cinquanta", "sessanta", "settanta", "ottanta", "novanta"]
    decade = n // 10  # la decina da n
    unit = n % 10  # l'unità di n
    
    # Adatta la traduzione per evitare la presenza di zeri finali
    if unit == 0:
        # Aggiusta per il caso speciale di 90
        if decade == 9:
            return "novanta"
        else:
            return DECADES[decade - 2]
    else:
        return DECADES[decade - 2] + translate_to_20(unit)

def translate_to_1000(n):
    if n < 100:
        return translate_to_100(n)
    if n > 999:
        return "Out of range"
    
    hundreds = n // 100
    remainder = n % 100
    
    # Adatta la traduzione per evitare la presenza di zeri finali
    if remainder == 0:
        return translate_to_20(hundreds) + "cento"
    else:
        return translate_to_20(hundreds) + "cento" + translate_to_100(remainder)

def translate_number(n):
    if n < 0 or n > 10000:
        return "Out of range"
    elif n == 0:
        return "zero"
    elif n < 100:
        return translate_to_100(n)
    elif n < 1000:
        return translate_to_1000(n)
    else:
        thousands = n // 1000
        remainder = n % 1000
        
        if remainder == 0:
            return translate_to_20(thousands) + "mila"
        else:
            return translate_to_20(thousands) + "mila" + translate_to_1000(remainder)

# Chiedi all'utente di inserire un numero
user_input = int(input("Inserisci un numero da 1 a 10000: "))

# Stampa solo il numero dato dall'utente
print(translate_number(user_input))
