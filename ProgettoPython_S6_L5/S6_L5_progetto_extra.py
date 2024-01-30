import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sys

# Impostazioni di stile globali per i grafici
sns.set(style="whitegrid")

def pulisci_dati(df):
    """Pulisce il DataFrame rimuovendo valori mancanti."""
    return df.dropna()

def statistiche_descrittive(df, colonna):
    """Fornisce statistiche descrittive per una colonna specificata."""
    return df[colonna].describe()

def mostra_distribuzione_stipendi(df, colonna='salary_in_usd'):
    """Visualizza la distribuzione degli stipendi."""
    plt.figure(figsize=(10, 6))
    sns.histplot(df[colonna], kde=True, color="skyblue")
    plt.title('Distribuzione degli stipendi', fontsize=15)
    plt.xlabel('Stipendio (USD)', fontsize=12)
    plt.ylabel('Frequenza', fontsize=12)
    plt.show()

def analisi_stipendi_per_categoria(df, colonna_categoria, colonna_stipendio='salary_in_usd'):
    """Analizza gli stipendi in base a una variabile categorica."""
    plt.figure(figsize=(12, 6))
    sns.boxplot(x=colonna_categoria, y=colonna_stipendio, data=df, palette="Set2")
    plt.title(f'Distribuzione stipendi per livello di esperienza', fontsize=15)
    plt.xlabel('Livello di esperienza', fontsize=12)
    plt.ylabel('Stipendio annuo (USD)', fontsize=12)
    plt.show()

def analisi_temporale(df, colonna_stipendio='salary_in_usd'):
    """Analizza come gli stipendi cambiano nel tempo."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='work_year', y=colonna_stipendio, estimator='mean', color="purple")
    plt.title('Andamento stipendi nel tempo', fontsize=15)
    plt.xlabel('Anno', fontsize=12)
    plt.ylabel('Stipendio Medio (USD)', fontsize=12)
    plt.show()

def confronto_per_localita(df, colonna_localita, colonna_stipendio='salary_in_usd'):
    """Confronta gli stipendi in base alla località."""
    plt.figure(figsize=(15, 7))
    sns.boxplot(x=colonna_localita, y=colonna_stipendio, data=df, palette="Set3")
    plt.xticks(rotation=45)
    plt.title(f'Confronto stipendi per località dell\'azienda', fontsize=15)
    plt.xlabel('Località dell\'azienda', fontsize=12)
    plt.ylabel('Stipendio (USD)', fontsize=12)
    plt.show()

def main():
    try:
        # Caricamento dei dati
        percorso_file = 'ds_salaries.csv'
        stipendi_ds = pd.read_csv(percorso_file)
    except FileNotFoundError:
        print("File non trovato. Controlla il percorso del file.")
        sys.exit()
    except Exception as e:
        print(f"Si è verificato un errore durante il caricamento del file: {e}")
        sys.exit()

    # Pulizia dei dati
    stipendi_ds_puliti = pulisci_dati(stipendi_ds)

    # Statistiche descrittive
    stats = statistiche_descrittive(stipendi_ds_puliti, 'salary_in_usd')
    print("Statistiche descrittive degli stipendi:\n", stats)

    # Visualizzazione della distribuzione degli stipendi
    mostra_distribuzione_stipendi(stipendi_ds_puliti)

    # Analisi degli stipendi in base al livello di esperienza
    analisi_stipendi_per_categoria(stipendi_ds_puliti, 'experience_level')

    # Analisi Temporale
    analisi_temporale(stipendi_ds_puliti)

    # Confronto per Località - dipendente e azienda
    confronto_per_localita(stipendi_ds_puliti, 'company_location')

# Avvio del programma 
main()
