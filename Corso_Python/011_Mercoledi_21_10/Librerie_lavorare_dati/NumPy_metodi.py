import numpy as np

arr = np.linspace(0,1, 5) #0 start #1 stop # 5 quantità di numeri da cui deve passare per arrivare da start a stop
print(arr) # Output: [0. 0.25 0.5 0.75 1. ]

random_arr = np.random.rand(3, 3)# 3 righe, 3 colonne
# Matrice 3x3 con valori casuali uniformi tra 0 e 1

print(random_arr)

arr = np.array([1, 2, 3, 4, 5])

sum_value = np.sum(arr)
mean_value = np.mean(arr)
std_value = np.std(arr)

print('Somma: ', sum_value,'Media: ', mean_value,'Deviazionestd: ', std_value) 

