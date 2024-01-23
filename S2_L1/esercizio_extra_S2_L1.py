# Esercizio 1
"""
Scrivi una funzione che prenda una serie di input dall'utente utilizzando un ciclo while e li stampi 
con la funzione print senza andare a capo. 
Il ciclo while si deve interrompere quando l'utente preme INVIO senza scrivere nulla.
"""
parola_senza_andare_a_capo = ""

while True:
    parola_inserita = input("Inserire una parola, premere q o Q per terminare il programma --> ")
    if parola_inserita ==  "Q" or parola_inserita == "q":
        break
    else:
        parola_senza_andare_a_capo = parola_senza_andare_a_capo + " " + parola_inserita
        continue

print(parola_senza_andare_a_capo)