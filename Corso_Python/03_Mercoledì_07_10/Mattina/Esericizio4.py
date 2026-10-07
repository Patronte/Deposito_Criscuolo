# while con dentro for
# Chiedi all'utente di inserire un numero
# il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, stampando ogni numero
# e chiederti se vuoi ripetere o no
'''
a= int(input("Inserisci un numero "))

while a > 0: #biggest mistake dovrebbe essere qui
    for numero in range(a):
        print(a)
        (a)-=1
    if a == 0:
        print(a)
        x = input("Vuoi ripetere il conteggio? ")
        if x.upper() == "SI":
            input(a)
        elif x.upper() =="NO":
            print("Finito ")
        else:
            print("Errore inaspettato, riavvia ")
    else:
        print("finito ")
'''



# secondo esercizio while con diversi while

# Esercizio su Python: Cicli e Condizioni
# Punto 1: Utilizzo di if
# Scrivi un sistema che prende in input un numero e stampa "Pari" se il numero è pari
# e "Dispari" se il numero è dispari.
# Punto 2: Utilizzo di while e range
# Scrivi un sistema che prende in input un numero intero positivo n e stampa tutti i
# numeri da n a 0 (compreso), decrementando di 1.Deve potersi ripete all’infinito
# Punto 3: Utilizzo di for
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
# ciascun numero nella lista.
# Punto 4: Utilizzo di if, while e for insieme Scrivi un sistema che prende in input
# una lista di numeri interi che precedentemente è stata valorizzata dall’utente.
# Il sistema deve:
# 1.Utilizzare un ciclo for per trovare il numero massimo nella lista.
# 2.Utilizzare un ciclo while per contare quanti numeri sono presenti nella lista.
# 3.Utilizzare una condizione if per stampare "Lista Vuota" se la lista è vuota,
# altrimenti stampare il numero massimo trovato e il numero di elementi nella lista.
'''
#punto1
numero= int(input("Inserisci un numero "))
if numero % 2 == 0:
    print("Il numero è pari")
else :
    print("Il numero è dispari")    
    
    '''
    
#punto2
'''
while True: #l'infinito non sono stato in grado di farlo da solo, il resto si
    x = int(input("Scrivi un numero "))

    while x >= 0:
        print(x)
        (x)-=1
'''
# Punto 3: Utilizzo di for
# Scrivi un sistema che prende in input una lista di numeri e stampa il quadrato di
# ciascun numero nella lista.

#punto3
quadrato= []
numero = input("Inserisci dei numeri ")
for numero in quadrato:
    print(quadrato)