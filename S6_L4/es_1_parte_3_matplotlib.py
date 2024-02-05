# Esercizio 3/3 
'''
• Utilizzando i metodi di rappresentazione grafica dei DataFrame, 
visualizziamo l'andamento di tutte le azioni sullo stesso grafico 
• Tramite pyplot, spostiamo la legenda in basso a destra
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

plt.plot(stockdata["Year"], stockdata["AAPL"], label="AAPL")
plt.plot(stockdata["Year"], stockdata["IBM"], label="IBM")
plt.plot(stockdata["Year"], stockdata["MSFT"], label="MSFT")
plt.plot(stockdata["Year"], stockdata["SBUX"], label="SBUX")
plt.plot(stockdata["Year"], stockdata["GSPC"], label="GSPC")

plt.title("Andamento delle azioni")
plt.xlabel("Anno")
plt.ylabel("Valore")
plt.legend(loc=4)

plt.show()




