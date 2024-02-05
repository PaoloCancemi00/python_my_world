# Esercizio 2/2 
'''
• Visualizzare un grafico con il numero di passeggeri di ogni classe di imbarco 
• Fare la stessa cosa per la colonna alive 
• Qual era la distribuzione delle tariffe (fare)? 
• Riusciamo a vedere la distribuzione delle età dei passeggeri rispetto alla classe di imbarco? 
Proviamo con un boxplot e con uno swarmplot 
• Visualizziamo un boxplot e un lmplot rispetto alle colonne fare e survived; che cose ne deduciamo?
'''

import seaborn as sns
import matplotlib.pyplot as plt

# Caricamento del dataset Titanic
titanic = sns.load_dataset('titanic')

plt.figure(figsize=(8, 6))
sns.countplot(x='class', data=titanic)
plt.title('Numero di Passeggeri per Classe di Imbarco')

plt.figure(figsize=(8, 6))
sns.countplot(x='alive', data=titanic)
plt.title('Numero di Passeggeri per Stato di Sopravvivenza')

plt.figure(figsize=(10, 6))
sns.histplot(titanic['fare'], kde=True)
plt.title('Distribuzione delle Tariffe sul Titanic')

plt.figure(figsize=(10, 6))
sns.boxplot(x='class', y='age', data=titanic)
plt.title('Distribuzione Età per Classe di Imbarco (Boxplot)')

plt.figure(figsize=(10, 6))
sns.swarmplot(x='class', y='age', data=titanic)
plt.title('Distribuzione Età per Classe di Imbarco (Swarmplot)')

plt.figure(figsize=(8, 6))
sns.boxplot(x='ì', y='morti', data=titanic)
plt.title('Distribuzione Tariffe per Sopravvivenza')
plt.show()





























