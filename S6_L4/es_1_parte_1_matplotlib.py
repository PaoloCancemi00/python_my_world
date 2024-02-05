# Esercizio 1/3 
'''
Scarichiamo il dataset stockdata da https://github.com/plotly/datasets/blob/master/stockdata.csv 
• Estraiamo i dati della colonna MSFT relative all'andamento delle azioni di Microsoft, 
e visualizziamolo mediante pyplot • 
Estraiamo le prime 5 righe della colonna MSFT e della colonna date, 
e usiamoli come ascisse e ordinate su un grafico mediante pyplot 
• Facciamo lo stesso per le ultime 5 righe del dataset
'''

import pandas as pd
from matplotlib import pyplot as plt
import sys

try:
    stockdata = pd.read_csv("Dataset/stockdata.csv")
except:
    print("Errore nel caricamento del file stockdata.csv")
    sys.exit()
    
colonna_date = stockdata["Date"]
colonna_msft = stockdata["MSFT"]

plt.subplot(2, 1, 1)
plt.plot(colonna_msft, color ="g", linewidth=1, linestyle="-")
plt.title("Azioni di Microsoft 2007 - 2016", color="g")
plt.xlabel("Valore delle azioni di Microsoft", color=(.8, .4, 0))
plt.ylabel("Andamento nel tempo", color="#9999ff")
plt.grid(True)
plt.legend(loc=4, labels=['MSFT'])

plt.subplot(2, 2, 3)
cd = colonna_date.head()
cm = colonna_msft.head()
plt.plot(cd, cm, "o", color="m", linewidth=1, linestyle="-")
plt.title("Primi 5 MSFT", color="m")
plt.xlabel("Primi 5 giorni")
plt.ylabel("Valore delle azioni MSFT")
plt.grid(True)

plt.subplot(2, 2, 4)
cd = colonna_date.tail()
cm = colonna_msft.tail()
plt.plot(cd, cm, "o", color="b", linewidth=1, linestyle="-")
plt.title("Ultimi 5 MSFT", color="b")
plt.xlabel("Ultimi 5 giorni")
plt.ylabel("Valore delle azioni MSFT")
plt.grid(True)

plt.tight_layout()
plt.show()






















