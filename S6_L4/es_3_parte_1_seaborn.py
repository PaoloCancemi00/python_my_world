# Esercizio 1/2 
'''
Da seaborn importiamo il dataset titanic, 
mediante: import seaborn as sns titanic = sns.load_dataset('titanic') 
• Quanti ponti c'erano sulla nave? 
• Ci sono dati mancanti? Dove? Quanti? Che logica potremmo usare per gestirli? 
• Tramite seaborn visualizziamo un lmplot sulle colonne age e fare; 
che cosa stiamo guardando?
'''

# SEABORN

import seaborn as sns 
from matplotlib import pyplot as plt

titanic = sns.load_dataset('titanic')
print(titanic)

# Counting the number of decks on the ship
num_decks = titanic['deck'].nunique() 
print("Number of decks on the ship:", num_decks)

# Checking for missing data
missing_data = titanic.isnull().sum() 
print("Missing data:\n", missing_data)

# Plotting a lmplot
sns.lmplot(x='age', y='fare', data=titanic, ci=None)

plt.show()























