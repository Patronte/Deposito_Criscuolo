 #Importo le librerie panda e numpy
import numpy as np
import pandas as pd


#--------------ESEMPI--------------
#slicing di array
arr_2d = np.array([[1, 2, 3, 4],
 [5, 6, 7, 8],
 [9, 10, 11, 12]])
# Slicing sulle righe
print(arr_2d[1:3]) # Output: [[ 5 6 7 8]
# [ 9 10 11 12]]
# Slicing sulle colonne
print(arr_2d[:, 1:3]) # Output: [[ 2 3]
# [ 6 7]
# [10 11]]
# Slicing misto
print(arr_2d[1:3, 1:3]) # Output: [[ 6 7]
# [10 11]]

#Ulteriori esempi
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# Slicing di base
print(arr[2:7]) # Output: [2 3 4 5 6]

# Slicing con passo
print(arr[1:8:2]) # Output: [1 3 5 7]

# Omettere start e stop
print(arr[:5]) # Output: [0 1 2 3 4]
print(arr[5:]) # Output: [5 6 7 8 9]

# Utilizzare indici negativi
print(arr[-5:]) # Output: [5 6 7 8 9]
print(arr[:-5]) # Output: [0 1 2 3 4]

#FANCY INDEXING sinstassi
arr2 = np.array([10, 20, 30, 40, 50])
# Utilizzo di un array di indici
indices = np.array([1, 3])
print(arr2[indices]) # Output: [20 40]
# Utilizzo di una lista di indici
indices = [0, 2, 4]
print(arr2[indices]) # Output: [10 30 50] 

 



#ESERCIZIO1---------------
#creo una variabile alla quale assegno un array da 10 a 49
seiUnMagoArray= np.arange(10,50)
#lo stampo
print(seiUnMagoArray)
#ne stampo il tipo
print(seiUnMagoArray.dtype)
#ne modifico il tipo in float (era int)
seiUnMagoArray.dtype=float
#ne stampo di nuovo il tipo
print(seiUnMagoArray.dtype)
#ne stampo lo shape (la forma)
print(seiUnMagoArray.shape)


#ESERCIZIO2--------------
import numpy as np
import pandas as pd
# Esercizio su NumPy Slicing Consegna: 
# 1.Crea un array NumPy 1D di 20 numeri interi casuali compresi tra 10 e 50. #OK 1d monodimensionale perché potevo fare pure + array tipo ([1,2,3,4],[5,6,7,8])
jhonny=np.random.randint(10,51,size=20)
#aiutato con ia a fare il random.randint e i valori in parentesi, ho installato lmstudio  e llama 3.8 instruct come modello, mi funziona offline
print(jhonny)
#  2.Utilizza lo slicing per estrarre i primi 10 elementi dell'array.
print(jhonny[0:11])
#  3.Utilizza lo slicing per estrarre gli ultimi 5 elementi dell'array. 
print(jhonny[15:21])
# 4.Utilizza lo slicing per estrarre gli elementi dall'indice 5 all'indice 15 (escluso).
print(jhonny[5:15])
# 5.Utilizza lo slicing per estrarre ogni terzo elemento dell'array.
print(jhonny[0:21:3]) #qui non sono sicuro vada bene, ho rispettato lo step, ma potevo omettere in qualche modo start e stop? ok ho trovato un esempio che me l'ha mostrato
print(jhonny[::3])    #versione senza dare start e stop
# 6.Modifica, tramite slicing, gli elementi dall'indice 5 all'indice 10 (escluso) assegnando loro il valore 99.
jhonny[5:10]=99
print(jhonny[5:10])
#jhonny[5:10] = np.full(5,99)
#mi sembrava strano, ho chiesto :   perché 5,99 e non solo 99?  5 sono gli elementi e 99 il valore ad essi associati? non è bastato indicare gli indici 5:10?
#risposta : array[5:10] = 99  lo preferisco, lo userò
# 7.Stampa l'array originale e tutti i sottoarray ottenuti tramite slicing. 
#e come lo faccio? non l'ho già fatto? al massimo mi è venuto in mente di assegnare ad ogni punto/slice precedente, una variabile, così mi richiamo ciascuno di essi

# Obiettivo: Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre e modificare sottoarray specifici da un array più grande.





# Esercizio 3 --------------------Slicing e F.Indexing
# Consegna:
# 1.Crea una matrice NumPy 2D di dimensioni 6x6 contenente
array_2d= np.array([[1,2,3,4,80,90],
                    [5,6,7,8,70,60],
                    [9,10,11,12,50,40],
                    [13,14,15,16,30,33],
                    [17,18,19,20,55,56],
                    [21,22,23,24,57,58]])
# numeri interi casuali compresi tra 1 e 100.
# 2.Estrai la sotto-matrice centrale 4x4 dalla matrice
# originale.
sotto_m_centrale= print(array_2d[1:5,0:4]) #la prima parentesti sono start e stop della colonna, gli altri start e stop per la riga
# 3.Inverti le righe della matrice estratta (cioè, la prima riga
# diventa l'ultima, la seconda diventa la penultima, e così
# via).
#ok devo usare RESHAPE.... NON è vero perché mi crea solo sottomatrici io voglio riordinare senza modificare i dati
print(sotto_m_centrale[::-1]) #non capivo dagli appunti se c'era spiegato, usato ia
#alternativa sempre ia,
m_centrale_invertita=np.flipud(sotto_m_centrale)
print(m_centrale_invertita)
#SCAMMATO DALLE IA PERCHé NON FUNZIONA NESSUNO DEI DUE MODI, poi ci provo da solo (col print di sotto, e va, ma volevo farlo sulla variabile creata)
#tentativo fallito sulla variabile creata:  print(sotto_m_centrale[0:6-1])
print(array_2d[1:6:-1])
#secondo me sto fallendo perché la variabile ha un print, dovrei togliere il print e farlo esterno all'assegnazione mi sa 

# 4.Estrai la diagonale principale della matrice invertita e crea un array 1D contenente questi elementi.
#estraggo la matrice invertita assegnandola a smc2 
sotto_m_centrale2= array_2d[1:6:-1]
#provo il metodo array.diagonal
diagonally=sotto_m_centrale2.diagonal(offset=1, axis1=0, axis2=1) #questa provata da solo prendendo da pag 483 del pdf
np.diag(sotto_m_centrale2) #questa presa da ia
print(sotto_m_centrale2)
#NIENTE DI CIò CHE HO PROVATO FUNZIONA, HO PROVATO ANCHE A CAMBIARE OFFSET AXIS1 E 2, ci ho perso troppo tempo vado al prossimo step, se è basato sul punto 4 mi strappo 5 capelli sappilo
# mi manca di crearne successivamente un'array 1d contenente quegli elementi
#però penso che una volta ottenuta la diagonale princ. della matrice invertita,
#potevo poi fare una variabile a cui la assegnavo, e printare essa, tipo:
#diagochevolevo=np.array(diagoinvertita) quindi creavo una variabile contenente la creazione di un array e passava per parametro, la diagonale stessa che stavo provando a creare, 
#sicuramente hai capito più tu che io cosa volevo dire qui 

# 5.Sostituisci tutti gli elementi della matrice invertita che
# sono multipli di 3 con il valore -1.
for n in matrice_invertita[0:10]:
    if n % 3 == 0
#mi viene da fare un ciclo for, ma gli indici mi mandano troppo in confusione per portarlo al termine, poi a come ho capito non si usa con queste librerie in quanto + lento di esse e dei loro metodi 
#allora prima per sostituire i valori, ho selezionato gli indici di un'array(soggetto da sostituire)e assegnato = 99, numero con cui volevo sostituirlo così : jhonny[5:10]=99 &O questo jhonny[5:10] = np.full(5,99)
#ho trovato l'indexing booleano finalmente nel pdf dovrebbe diventare qualcosa del genere
print(matrice_invertita[matrice_invertita % 3==0 ]) #maledetto, si tu mirko, non è vero sei un grande, a mani basse best prof di tutti i corsi gratuiti, ma comunque un maledetto
# 6.Stampa la matrice originale, la sotto-matrice centrale
print(array_2d) #matrice originale
print(array_2d[1:5,0:4])#METODO2 subM_centrale=array_2d[1:5,0:4] + print(subM_centrale)     #sotto-matrice centrale
# estratta, la matrice invertita, la diagonale principale e la
# matrice invertita modificata.
# il fatto che a fine esercizio me li fai stampare tutti, mi fa pensare che la soluzione che ho trovato tramite il print non sia l'unica e che ti aspettavi un'assegnazione di variabile per ogni tipologia di modifica svolta, seguita da un print (un po' come metodo 2 per la sottomatrice centrale del punto6)
# Obiettivo:
# Esercitarsi nell'utilizzo dello slicing di NumPy per estrarre,
# modificare e manipolare sotto-matrici e array, applicando
# operazioni avanzate come l'inversione delle righe e la
# sostituzione condizionale degli elementi.



#ESERCIZIO FINALE DAY ONE CONSEGNA
# Crea uno script Python che esegua i seguenti passaggi:
# 1.Crea un array NumPy (ndarray) utilizzando np.arange con valori da 0 a
import numpy as np
import pandas as pd
aray= np.arange(0,50), 
# 49. più altre 50 posizioni casuali tra 49 e 101.
aray2= np.random.randint(49,102, size=50)
# Stampa l’array, il suo dtype e la sua shape.
risultato=np.append(aray,aray2) #ho sbattuto con merge, concat da solo, concatenate, e l'append forniti da ia 
print(risultato)
#stampo il type
print(risultato.dtype)
#stampo la shape 
print(risultato.shape) #output (100,) va bene come output?

# 2.Modifica il tipo di dato (dtype) dell’array in float64.
risultato.dtype=float
#Float64 non gli va bene, avendo messo il float  restituisce deprecation warning:
# Instead of changing the dtype on an array x, create a new array with x.view(new_dtype) #risultato.dtype=float, float64 (100,) 
# Verifica e stampa di nuovo dtype e shape.
print(risultato.dtype, risultato.shape) #Output: float64 (100,)
# 3.Utilizza lo slicing per ottenere:
risultato.dtype=int #LA GIOCATA
# i primi 10 elementi
print(risultato[0:11])
# gli ultimi 7 elementi
print(risultato[-7:101])
# gli elementi dall’indice 5 all’indice 20 escluso
print(risultato[5:20])
# ogni quarto elemento dell'array
print(risultato[::4])
# 4.Modifica tramite slicing gli elementi dall’indice 10 a 15 (escluso)
# assegnando loro il valore 999.
risultato[10:15]=999
print(risultato[10:15])
# 5.Utilizza la fancy indexing per selezionare:
# gli elementi in posizione [0, 3, 7, 12, 25, 33, 48]
indici=np.array([0,3,7,12,25,33,48])
print(risultato[indici])
# tutti gli elementi pari dell’array utilizzando una maschera booleana
maschera_pari=risultato%2==0
print(risultato[maschera_pari])
# tutti gli elementi maggiori della media dell'array
media= np.mean(risultato)
maschera_over_media=risultato>media
risultato_media=risultato[maschera_over_media]
print(risultato_media)
# 6.Stampa:
# l’array originale dopo tutte le modifiche
# tutti i sotto-array ottenuti tramite slicing e fancy indexin
