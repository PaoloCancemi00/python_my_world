# Esercizio 
'''
Scarichiamo il dataset elections da 
https://github.com/plotly/datasets/blob/master/election.csv: 
• Con un grafico a barre confrontiamo i voti totali presi dai tre candidati 
(come somma di tutti i distretti) 
• Con un grafico a barre confrontiamo il numero di votanti per ogni distretto 
• Visualizzare un grafico a barre comparativo dove si confrontano i voti presi 
nei primi 4 distretti per ogni candidato 
• Visualizzarlo sia in formato appaiato che impilato (stacked) e salvare entrambi 
i grafici su disco in alta risoluzione
'''

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Caricamento del dataset
election_data = pd.read_csv("Dataset/election.csv")

# 1. Confronto dei Voti Totali dei Tre Candidati
total_votes_per_candidate = election_data[['Coderre', 'Bergeron', 'Joly']].sum()

# Creazione del grafico a barre per i voti totali dei tre candidati
plt.figure(figsize=(10, 6))
total_votes_per_candidate.plot(kind='bar')
plt.title('Voti Totali per Candidato')
plt.ylabel('Voti Totali')
plt.xlabel('Candidato')
plt.xticks(rotation=0)
plt.grid(axis='y')
plt.tight_layout()

# Salvataggio del grafico
plt.savefig('total_votes_per_candidate.png', dpi=300)

# 2. Confronto del Numero di Votanti per Distretto
plt.figure(figsize=(14, 8))
sns.barplot(x='district_id', y='total', data=election_data)
plt.title('Numero di Votanti per Distretto')
plt.ylabel('Numero di Votanti')
plt.xlabel('ID Distretto')
plt.xticks(rotation=90)
plt.tight_layout()

# Salvataggio del grafico
plt.savefig('voters_per_district.png', dpi=300)

# Preparazione dei dati per i grafici dei primi 4 distretti
first_four_districts = election_data.head(4)

# 3. Voti nei Primi 4 Distretti per Ogni Candidato - Formato Appaiato
plt.figure(figsize=(10, 6))
first_four_districts.set_index('district')[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar', stacked=False)
plt.title('Voti nei Primi 4 Distretti per Ogni Candidato (Appaiato)')
plt.ylabel('Voti')
plt.xlabel('Distretto')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvataggio del grafico
plt.savefig('votes_first_four_districts_bar.png', dpi=300)

# 4. Voti nei Primi 4 Distretti per Ogni Candidato - Formato Impilato
plt.figure(figsize=(10, 6))
first_four_districts.set_index('district')[['Coderre', 'Bergeron', 'Joly']].plot(kind='bar', stacked=True)
plt.title('Voti nei Primi 4 Distretti per Ogni Candidato (Impilato)')
plt.ylabel('Voti')
plt.xlabel('Distretto')
plt.xticks(rotation=45)
plt.tight_layout()

# Salvataggio del grafico
plt.savefig('votes_first_four_districts_stacked.png', dpi=300)

plt.show()










