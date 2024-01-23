# scrivere un algoritmo che, dato un numero,
# ne mostri la sua rappresentazione a lettere in italiano
# Esempio:
#   input: 1234 --> output: milleduecentotrentaquattro

import inflect                            # trascrive da numero a lettere in lingua inglese 
from googletrans import Translator        # traduce da lingua inglese a lingua italiana

n = int(input("Inserisci un numero --> "))

def traduci_numero(n):
    
    p = inflect.engine()
    word = p.number_to_words(n)
    

    translator = Translator()
    translation = translator.translate(str(word), src='en', dest='it')
    return translation.text

print(f"{n} in italiano: {traduci_numero(n)}")
