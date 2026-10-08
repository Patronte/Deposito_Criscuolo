#dammi un numero positivo, se è negativo, te lo richiedo
'''
richiesta= 0
while richiesta <= 0:
   richiesta = int(input("Inserisci un numero "))
      
somma = 0
somma = somma +   richiesta
print(somma)
'''


#1. Ciclo while
#Descrizione: Scrivi un programma che chieda all'utente di inserire numeri interi fino a quando l'utente inserisce il numero 0.
# Quando viene inserito il numero 0, il programma deve calcolare e stampare la somma di tutti i numeri inseriti.
'''
somma=[]
while True:
    richiesta= int(input("Scrivi un numero "))
    if richiesta == 0:
        break
    elif richiesta!=0:
        somma.append(richiesta)
    else:
        print("Errore! ")
totale = 0
for numero in somma:
    totale= totale+numero
print(totale)

'''
#svolto da mirko
'''
somma = 0
numero = int(input("Inserisci un numero: "))
while numero != 0:
    somma=somma+numero
    numero= int(input("Inserisci un altro numero: "))
    
print("La somma totale è: ", somma)
'''

#2. Ciclo for
#Descrizione: Scrivi un programma che chieda all'utente di inserire una parola e poi utilizzi un ciclo for per stampare ogni lettera della parola su una nuova riga.

#3. Ciclo range
#Descrizione: Scrivi un programma che utilizzi un ciclo for con range per stampare fino a un massimo N dato dall'utente tramite uno steps dato dall'utente (ES 2 per volta).

#4(extra, racchiudi i 3 precedenti in un unico while con if a scelta per ognuno di essi)




# Esercizio Completo
# Descrizione: Scrivi un programma che chieda all'utente di inserire un numero intero positivo n. Il programma deve poi eseguire le seguenti operazioni:

listaNumeri= []

richiestaN = int(input("Scrivi un numero intero positivo "))

while richiestaN <=0:
    richiestaN=int(input("Scrivi un intero positivo "))

    if richiestaN > 0:
        richiestaN=int(input("Scrivine un altro "))
        break
        
for x in listaNumeri:
    print(listaNumeri.append)        

# 1. Utilizzare un ciclo while per garantire che l'utente inserisca un numero positivo. Se l'utente inserisce un numero negativo o zero,
# il programma deve continuare a chiedere un numero fino a quando non viene inserito un numero positivo.
# 2. Utilizzare un ciclo for con range per calcolare e stampare la somma dei numeri pari da 1 a n.
# 3. Utilizzare un ciclo for per stampare tutti i numeri dispari da 1 a n.
# 4. Utilizzare una struttura if per determinare se n è un numero primo. Un numero primo è divisibile solo per 1 e per se stesso. Il programma deve stampare se n è primo o no.
# 5. Stampare tutto

#SVOLTI DA MIRKO
'''

scelta = ""

while scelta != "fine":

    scelta = input("Scegli esercizio: es1 - es2 - es3 - fine: ")

    # ESERCIZIO 1
    if scelta == "es1":

        somma = 0
        numero = int(input("Inserisci un numero: "))

        while numero != 0:
            somma = somma + numero
            numero = int(input("Inserisci un altro numero: "))

        print("La somma totale è:", somma)


    # ESERCIZIO 2
    if scelta == "es2":

        parola = input("Inserisci una parola: ")

        for lettera in parola:
            print(lettera)


    # ESERCIZIO 3
    if scelta == "es3":

        massimo = int(input("Inserisci il numero massimo: "))
        step = int(input("Inserisci lo step: "))
        start = int(input("Inserisci lo start: "))

        for x in range(start, massimo + 1, step):
            print(x)


    if scelta != "es1" and scelta != "es2" and scelta != "es3" and scelta != "fine":
        print("Sei un pippo")


print("Programma terminato")
'''