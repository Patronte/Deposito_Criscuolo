# while con dentro for
# Chiedi all'utente di inserire un numero
# il programma dovrebbe quindi fare un conto alla rovescia a partire da quel numero fino a zero, stampando ogni numero
# e chiederti se vuoi ripetere o no

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




# secondo esercizio while con diversi while

