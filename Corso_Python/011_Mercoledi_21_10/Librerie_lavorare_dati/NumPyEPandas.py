# Due librerie fondamentali per lavorare con i dati:
# NumPy & Pandas

# _________NUMPY_________

# NumPy: è una libreria externa che introduce gli Array (delle super liste) 
# la sua caratteristica principale è il BROADCASTING

# BROADCASTING: la capacità di fare calcoli matematici su un'intera montagna di dati, all'istante, senza usare cicli for
# PRINCIPI DEL BROADCASTING 
# ALLINEAMENTO DELLE DIMENSIONI SI VERIFICA SE UNO DEI DUE ARRAY è 
# ESPANSIONE DELLE DIMENSIONI
# APPLICAZIONE DELL'OPERAZIONE
# Perché usare gli Array di NumPy invece delle liste normali di Python?
# 1. OMOGENEITÀ DEI DATI: Una lista normale può contenere tipi misti (es. [1, "ciao", True]). 
#    Un Array di NumPy obbliga TUTTI gli elementi a essere dello stesso identico tipo 
#    (es. tutti interi o tutti float). Questo permette una gestione ordinata.
# 2. EFFICIENZA IN MEMORIA (C-Velocity): Le liste di Python salvano i dati in posizioni 
#    disperse nella memoria. Gli Array di NumPy li salvano in un blocco unico e continuo. 
#    Essendo scritto in linguaggio C, NumPy dialoga direttamente con l'hardware: per questo 
#    i calcoli sono migliaia di volte più veloci di un ciclo for.
# 3. LE MATRICI (Array a 2 Dimensioni): Con NumPy si possono creare tabelle di numeri 
#    (Matrici) inserendo delle liste dentro un'altra lista. 
#    Il comando .shape permette di sapere quante righe e colonne ci sono.


# Metodi rapidi di generazione NumPy:
# np.zeros(5) --> Crea un array vuoto di 5 zeri (utilissimo per inizializzare tabelle).
# np.ones(5)  --> Crea un array di 5 elementi tutti impostati a 1.

# ----ESEMPIO DI CODICE----

import numpy as np  # importiamo la libreria nel file attuale.

# Creiamo una lista (array) di NumPy (Array a 1 dimensione)
lista_array = np.array([1, 2, 3])

# Moltiplichiamo TUTTO per 2
risultato = lista_array * 2
print(risultato)
print(lista_array.shape)  # Output: (3,) -> Significa che ha 3 elementi

# Matrice a 2 dimensions (Tabella con 2 righe e 3 colonne)
matrice = np.array([[1, 2, 3], [4, 5, 6]])
print(matrice.shape)  # Output: (2, 3) -> Significa 2 righe e 3 colonne


# ________PANDAS_________

# PANDAS: serve per gestire tabelle di dati complesse (come faremmo su excel)
# DATAFRAME: in Pandas una tabella si chiama--> DataFrame 

# DATAFRAME: L'intera tabella. Se estraggo una sola colonna, diventa una Series.
# SERIES: è una singola colonna, se dalla tabella con le voci nome, cose, città estraggo ogni colonna singolarmente, nomi sarà una series, e così via anche le altre
# Sintassi: tabella["Nome_Colonna"] --> Restituisce una Series.
# Con Pandas puoi caricare un file esterno, (.csv, .xlsx) con una sola riga di codice


#MANCANZA1 FUNZIONALITà CHIAVE DI PANDAS MANIPOLAZIONE DEI DATI, PULIZIA DEI DATI, ANALISI DEI DATI, INTEROPERABILITà presenti in slide 252
#MANCANZA2 multi index presente a slide 260 a 263 e 280
#MANCANZA3 Groupby slide 263 a 267 esercizi a 278
# Comandi di Ispezione Rapida del DataFrame:
# .info()     --> Mostra la struttura della tabella, i tipi di dati e se ci sono valori mancanti (Null).
# .describe() --> Calcola automaticamente media, max, min e deviazione standard di TUTTE le colonne numeriche insieme.


# Metodi Statistici rapidi utilizzabili sulle colonne (Series):
# .mean()   --> Calcola la media aritmetica (restituisce un singolo float)
# .max()    --> Trova il valore massimo presente nella colonna
# .min()    --> Trova il valore minimo presente nella colonna
# .sum()    --> Somma tutti i valori della colonna

# ----ESEMPIO DI CODICE----
import pandas as pd  # importiamo la libreria Pandas

# leggiamo il file CSV dei campioni di lol, grazie PeppeGiacco
tabella_campioni = pd.read_csv("LoLChampionsGiusepGiacc.csv")

# Guardiamo le prime 5 righe della tabella per capire com'è fatta
print(tabella_campioni.head())

# Isoliamo la colonna "Attacco" (Diventa una Series)
colonna_attacco = tabella_campioni["attackDamage"]

# Calcoliamo la media della colonna estratta
media_attacco = colonna_attacco.mean()
print(media_attacco)  # Output: restituisce un singolo numero float

# Con Pandas possiamo filtrare la tabella in vari modi, possiamo ad esempio chiedere 
# "Mostrami solo i campioni che hanno più di 600 di vita" oppure "Calcola la media dell'attacco di tutti i personaggi".
# Esempio sintassi filtro: tabella_campioni[tabella_campioni["vita"] > 600]

# --- Filtri a più condizioni ---
# In Pandas per unire più filtri si usa l'operatore "&" (SIGNIFICA: E contemporaneamente) 
# Ogni condizione deve OBBLIGATORIAMENTE stare dentro le parentesi tonde.
# Esempio: tabella_campioni[(tabella_campioni["hp"] > 600) & (tabella_campioni["attackDamage"] > 50)]

#MultiIndex è una capacità di Pandas ci permette di creare un indice con  + valori di indice tipo Paese+Anno
#il comando per il multiindice è set index 
#Pivot è una funzionalità avanzata di pandas che ci permette di modificare 

#GROUPBY: è una tecnica presa da SQL serve a prendere un gruppo di dati ed applicare ad essi una funzione, serve ad aggregare i dati insieme

#Primo step è sempre o creare o caricare, o usiamo dati sintetici, o dati reali 

#definire il percorso) scegliere il metodo per caricare i dati) esplorazione
#creare un file chiamato Esplorazione dove funzioni di analisi ripetibili 
#come metodo info dati gli passo il DF valorizzato mi riporto DF.info

#Esplorazione e pulizia
#Visualizzazione delle statistiche descrittive
print(df.describe())

#rimozione dei valori mancanti
df_clean= df.dropna()

#Selezione e Filtraggio
#Pandas fornisce metodi per selezionare specifiche colonne o righe da un DF 
#Selezione di una colonna
ages = df['età']
#Filtraggio basato su una condizione
adults = df[df['età'] >= 18]

#MANIPOLAZIONE DEI DATI
#include funzioni per modificare l'ordine dei dati, combinarli, con altri set di dati, o cambiare la loro struttura organizzativa
#Ordinamento dei dati per età
df_sorted = df.sort_values(by='età')
#sort ordina i valori rispetto a una colonna, per farla al contrario :reverse
#il merge unisce due dataframe in base ad una colonna in comune
#Unione di due DataFrame
merged_df = pd.merge(df, df_csv, on='nome')
#il merged_df  sarà un df che è l'unione di df, df_csv con punto di unione(on) la Colonna 'nome'

#Trasformazioni è l'operazione che trasforma un dato, lo cambia
#la manipolazione crea un nuovo dato lasciando integro il dato iniziale