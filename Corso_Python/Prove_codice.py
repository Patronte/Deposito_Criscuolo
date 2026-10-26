""" numeri = [1, 2, 3, 4, 5, 6]
somma = 0
for n in numeri:
    if n % 2 == 0:
        somma += n
    else:
        somma -=n
print(somma)  """

""" import numpy as np
import pandas as pd

# Esercizio 2 Slicing e F.Indexing
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
# tentativo 1print(sotto_m_centrale[::-1]) #non capivo dagli appunti se c'era spiegato, usato ia
#alternativa sempre ia, 
# tentativo 2 m_centrale_invertita=np.flipud(sotto_m_centrale)
#print(m_centrale_invertita)
#SCAMMATO DALLE IA PERCHé NON FUNZIONA NESSUNO DEI DUE MODI, poi ci provo da solo (col print di sotto, e va, ma volevo farlo sulla variabile creata)
#tentativo fallito sulla variabile creata:  print(sotto_m_centrale[0:6-1])
print(array_2d[1:6:-1]) #alla fine ci so riuscito da solo ma il -1 mi mancava gravemente come pezzo, l'ho preso da uno dei tentativi falliti
#secondo me sto fallendo perché la variabile ha un print, dovrei togliere il print e farlo esterno all'assegnazione mi sa 

# 4.Estrai la diagonale principale della matrice invertita e
sotto_m_centrale2= array_2d[1:6:-1]
diagonally=sotto_m_centrale2.diagonal(offset=1, axis1=0, axis2=1) #questa provata da solo prendendo da pag 483 
sotto_m_centrale2= np.diag(sotto_m_centrale2) #questa presa da ia
print(sotto_m_centrale2)
#NIENTE DI CIò CHE HO PROVATO FUNZIONA, HO PROVATO ANCHE A CAMBIARE OFFSET AXIS1 E 2, ci ho perso troppo tempo vado al prossimo step, se è basato sul punto 4 mi strappo 5 capelli sappilo """
""" #SHAPE COME FUNZIONA? LA RISPOSTA è IN OUTPUT
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6], [7,8,9]])
print(arr.shape) # Output: (2, 3) 2= liste, 3 = elementi all'interno

arr_2d = np.array([[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12]])
# Slicing sulle righe
print(arr_2d[0:3]) #0:3 sono lo start e stop """

""" import numpy as np

arr = np.linspace(0,1, 5) #0 start #1 stop # 5 quantità di numeri da cui deve passare per arrivare da start a stop
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]

random_arr = np.random.rand(3, 3)# 3 righe, 3 colonne
# Matrice 3x3 con valori casuali uniformi tra 0 e 1

print(random_arr)

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print('Somma: ',sum_value,'Media: ',mean_value,'Deviazionestd: ',std_value) """

import numpy as np


arr = np.arange(6)
print(arr)
reshaped_arr = arr.reshape((2, 3))
print(reshaped_arr)
# Output: [[0 1 2] [3 4 5]]
