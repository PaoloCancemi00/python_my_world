# Esercizio 2  (1/2)
'''
Scarichiamo l'Iris dataset da qui: https://archive.ics.uci.edu/dataset/53/iris 
Troveremo un file .data, che è un CSV, e un file .names con i metadati; 
questa versione del dataset non ha i nomi di colonna. • 
Leggiamo il file e carichiamolo in un DataFrame mediante pd.read_csv() 
senza utilizzare altri parametri • 
Stampiamo le prime cinque righe 
• Stampiamo i nomi di colonna: descrivono cosa c'è nella colonna relativa?
'''
import pandas as pd

iris = pd.read_csv("Dataset/iris/iris.data", header=None)

print(f"\n {iris.head()} \n")

nuovi_nomi_colonna = ['sepal length in cm', 'sepal width in cm', 'petal length in cm', 'petal width in cm', 'class']

print(f"Attribute Information: \n 1. sepal length in cm \n 2. sepal width in cm \n 3. petal length in cm\n 4. petal width in cm \n 5. class: \n -- Iris Setosa \n -- Iris Versicolour \n -- Iris Virginica")