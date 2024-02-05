# Esercizio 2/3 
'''
Estraiamo le prime 20 istanze della colonna AAPL delle azioni di Apple, 
e visualizziamo il grafico tramite pyplot, in modo che: 
• il grafico sia rosso 
• la linea sia tratteggiata 
• vi sia un pallino come marker 
• l'asse delle ascisse si chiami "Data" 
• l'asse delle ordinate si chiami "Valore" 
• il titolo del grafico sia "Azioni Apple" 
• il markerfacecolor sia nero 
• la linea abbia spessore uguale a 2
'''

import pandas as pd
from matplotlib import pyplot as plt
import sys

try:
    stockdata = pd.read_csv("Dataset/stockdata.csv")
except:
    print("Errore nel caricamento del file stockdata.csv")
    sys.exit()

stockdata["Year"] = pd.to_datetime(stockdata["Date"]).dt.year
data_grouped = stockdata.groupby("Year")["AAPL"].mean()

plt.plot(data_grouped.index, data_grouped.values, marker="o", markerfacecolor="black", color="red", linewidth=2, linestyle="--")
plt.title("Andamento delle azioni Apple nel tempo")
plt.xlabel("Anno")
plt.ylabel("Valore medio")
plt.grid(True)

plt.show()
















