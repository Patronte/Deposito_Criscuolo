# Due librerie fondamentali per lavorare con i dati:
# NumPy & Pandas

# _________NUMPY_________

# NumPy: è una libreria externa che introduce gli Array (delle super liste) 
# la sua caratteristica principale è il BROADCASTING

# BROADCASTING: la capacità di fare calcoli matematici su un'intera montagna di dati, all'istante, senza usare cicli for

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