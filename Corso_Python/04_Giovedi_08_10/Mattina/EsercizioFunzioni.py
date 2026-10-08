# Def
# 1. Esercizio Base: Indovina il numero
# Descrizione: Scrivi un programma che genera un numero casuale
# tra 1 e 100 (inclusi). L'utente deve indovinare quale numero è
# stato generato. Dopo ogni tentativo, il programma dovrebbe
# dire all'utente se il numero da indovinare è più alto o più
# basso rispetto al numero inserito. Il gioco termina quando
# l'utente indovina il numero o decide di uscire.
# 2. Esercizio Avanzato: Sequenza di Fibonacci fino a N
# Descrizione: Chiedi all'utente di inserire un numero N. Il
# programma dovrebbe stampare la sequenza di Fibonacci fino a N.
# Ad esempio, se l'utente inserisce 100, il programma dovrebbe
# stampare tutti i numeri della sequenza di Fibonacci minori o
# uguali a 100.
#Funzione indovina, chiede il numero da indovinare

#variabili di numero da indovinare e scelta dell'utente
numeroCasuale = int(input("Seleziona un numero da indovinare da 1 a 100: "))
sceltaN= int(input("Indovina il numero: "))

#funzione di scelta utente
def sceltaNumero(a=int): 
   
#Check se numero è + alto o + basso (da mettere in un while)
    if sceltaN > numeroCasuale:
        print("Il numero da indovinare è più basso") 
    elif sceltaN < numeroCasuale:
     print("Il numero da indovinare è più alto")    
    else : 
        print("Scelta non valida, riprova! ")
    
















'''
x = int(input(""))

def indovina(a=int):
   
    if  numero == NumerodaIndov:
        print("Congratulazioni, hai vinto! ")
 
    numero = int(input("Indovina il numero: "))
     
while True:
    NumerodaIndov = int(input("Scegli un numero da indovinare, da 1 a 100: "))
    indovina(NumerodaIndov)
    if NumerodaIndov > 100 or NumerodaIndov < 1:
        int(input("Questo numero non va bene, scegline un altro! "))
    
    scelta=input("VUOI RIGIOCARE? ")
    if scelta.upper()  == "NO":
        break    
    pass




NumerodaIndov= int(input("Seleziona un numero da indovinare, da 1 a 100: "))
'''