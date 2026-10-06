'''Collezioni aka liste ordinate e modificabile di dati hanno 4 caratteristiche,
- non è ne un tipo basilare ne un NON basilare è detto tipo composto 
tipo list
definizione  
ordinamento ordinato
elementi eterogenei
si definiscono tramite parentesi quadre 
'''
#creo collezioni
listaNum = [1,2,3,4,5,10]
listaNom = ["Peppe", "Mirko", "Muciaccia", "Andonio"]
listaMisto = [ "Peppino", 2, True, 4.20]
#stampo il primo elemento della listaNom
print(listaNom[0])
#modifico un elemento della listaNum
listaNum[2] = 500
#stampo la lista che è stata modificata grazie alla riga 16
print(listaNum)

#Utilizziamo i metodi, len, append, insert, remove, sort 

listaNum = [15,2,25,4,5,10]
listaNom = ["Peppe", "Mirko", "Muciaccia", "Andonio"]
listaMisto = [ "Peppino", 2, True, 4.20]
#stampa lista numeri
print(len(listaNum))
#aggiungi a fine lista il numero 6
listaNum.append(6)
print(listaNum)
#Inserisci in lista i seg valori
listaNum.insert(12,10)
#remove seguente valore
listaNum.remove(10)
print(listaNum)
#ordina la lista 
listaNum.sort()
print(listaNum)