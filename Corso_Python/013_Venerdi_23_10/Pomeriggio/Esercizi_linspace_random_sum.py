import numpy as np


""" # ESERCIZIO1:
# Crea un array utilizzando linspace, cambia la sua forma con reshape,
# genera un array casuale e calcola la somma degli elementi.

# 1.Crea un array di 12 numeri equidistanti tra 0 e 1 usando linspace.

#dichiaro arr, tramite linspace, 
arr=np.linspace(0,1, 12) #gli do i valori start 0 stop 1 step 12(step inteso come quanti numeri deve generarmi, non quanti deve saltare)

#stampo
#print(arr)

# 2.Cambia la forma dell'array a una matrice 3x4.

#riassegno arr a reshaped_arr per comodità, gli do i valori di riga e colonna, in base ai 12 float che ho in arr(altrimenti non va, sono 12, se faccio un 3x3 copro 9 elementi con 3 fuori e da errore)
reshaped_arr = arr.reshape((3,4))

#stampo
#print(reshaped_arr)

#dico per comodità perché potevo fa pure nel print, troppo sborone però, mi calmo
#print(arr.reshape((3,4)))

# 3.Genera una matrice 3x4 di numeri casuali tra 0 e 1.
matrice_random= np.random.rand(3,4) #3 righe 4 colonne

#stampo
#print(matrice_random)

# 4.Calcola e stampa la somma degli elementi di entrambe le matrici.
somma=np.sum(reshaped_arr+matrice_random)
print(somma)

#FINE ES1 """


#ESERCIZIO2
# Obiettivo:
# Esercitarsi nell'utilizzo di linspace per generare sequenze di numeri, random per
# creare array di numeri casuali, e sum per eseguire operazioni di somma sugli array,
# incluso l'uso di condizioni per la somma parziale e gestire il salvataggio di file in
# merito.

# Consegna:
# 1.Utilizza np.linspace per creare un array di 50 numeri equidistanti tra 0 e 10.

#creo la matrice equidistante tra 0 e 10 contenente 50 numeri
numeri_equidistanti=np.linspace(0,10,50) #start, stop, amount/quantity
#print(numeri_equidistanti)

# 2.Utilizza np.random.random per creare un array di 50 numeri casuali compresi tra 0  e 1.
array_random= np.random.random(50) #amount/quantity
#print(array_random)

# 3.Somma i due array elemento per elemento per ottenere un nuovo array.
# I tentativo, fallito perché ottengo un singolo numero
# quindi np.sum mi fa la somma di tutti i valori presenti negli array, non l'addizione di ognuno di essi, col corrispettivo dell'altro array

# array_sommario = np.sum([numeri_equidistanti]+[array_random])
# print(array_sommario)

# II tentativo, dopo aver visto .add a slide 227

# array_sommario = np.add(numeri_equidistanti+array_random) 

#non ci siamo, la console mi dice che prende da 2 a 3 posizionali ma gliene ho dato uno, (numeri_equidistanti+array_random) a causa del + viene trattato come singolo argomento

# III tentativo, qui la cara vecchia virgola funziona come mi aspetto, in output del print mi restituisce 50 n.float che è ciò che volevo

array_sommario = np.add(numeri_equidistanti , array_random)

#print(array_sommario)

# 4.Calcola la somma totale degli elementi del nuovo array.
#qui stavo andando in confusione, pensavo di averlo già fatto nel punto precedente, poi pensavo di aver fatto una cosa per un'altra nel punto precedente,
# alla fine ho capito che qui vuoi quello che viene richiesto dal punto e mi basterà fare sum come nel tentativo fallito del punto precedente

som_tot_arr= np.sum(array_sommario)
#print(som_tot_arr) # l'output atteso è inutile che te lo scrivo avendo un array rand ad ogni avvio del file


# 5.Calcola la somma degli elementi del nuovo array che sono maggiori di 5.
#pocket di ragionamento: io ho #array_sommario=soggetto e  #>5 = condizione per prendere l'elemento/numero

arr_sommario_maggiore_5= np.sum(array_sommario[array_sommario>5]) #secondo me l'ho fatto giusto mi do una stellina per aver ricordato dagli esercizi di ieri come si facesse
#e mi segno per me BOOLEAN INDEXING  PAG 217
#print(arr_sommario_maggiore_5) 

# 6.Stampa gli array originali, il nuovo array risultante dalla somma e le somme calcolate.
print(numeri_equidistanti)#array originale 1 
print(array_random) #array originale 2 
print(array_sommario) #array risultante dalla somma che equivale anche alle somme calcolate?
#print(numeri_equidistanti+array_random) # non è questo, ci ho provato ma è la stessa cosa di stampare array_sommario


# 7.Salva i dati su un file TXT a ogni giro 
# #immagino di dover recuperare I/O che parte a 192 #si, lo farò
numeri_equidistanti
array_random
array_sommario
som_tot_arr
arr_sommario_maggiore_5
# 8.Rendi ripetibile il processo complessivo
# #la mia nemesi, ho intenzione di svolgere questo punto
# 9.Chiedi se si vuole sovrascrivere il TXT o no. #devo finire la lettura di I/O per svolgere 
#intanto ho creato un ciclo while nell'if metterò la sovrascrittura e nell'elif metterò "l'append" l'aggiunta a fine file che avevo visto sbirciando la teoria dal pdf
while True:
    risposta=input("Vuoi sovrascrivere il file? Y/N ").upper()
    if risposta == ("Y"):
        print('okbro')
        #w--> sovrascrivi
    elif risposta == "N":
        print('okkkbro')
        #a-->append a fine file
    else:
        print('scelta non valida, riprova')
        
        