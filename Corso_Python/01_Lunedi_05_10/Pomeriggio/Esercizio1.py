#esercizio 1
'''Andare a creare una variabile per ogni tipo di dato,
che prende in input ogni tipo di "tipo" basilare e stamparli
tutti in unico print, dopodichè far inserire all'utente
due numeri e comprovare gli operatori, logici e di confronto.'''
#creazioni variabili per ogni tipo di dato primitivo
int = int(input("Inserisci un numero: "))
float = float(input("Inserisci un numero: "))
string = input("Inserisci una parola : ")
bool = bool(input("Inserisci un valore booleano True o False: "))
char = input("Inserisci un char : ")
#stampa le varie variabili in succesione separate da uno spazio
print (bool, " ", float, " " , int, " ", string, " ", char, " ")
#chiedi all'utente di inserire un intero
numint1 = int(input("Inserisci un int"))
numint2 = int(input("Inserisci un int"))
#stampa con IF nelle parentesi
print(numint1 < numint2 and numint1 > numint2)
print(numint1 < numint2 or numint1 > numint2 or numint1 == numint2)
print( not(numint1 > numint2 and numint1 > numint2))