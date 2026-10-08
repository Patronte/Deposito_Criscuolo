#LE FUNZIONI IN PY le funzioni sono la comprova pratica dell'astrazione in quanto
#sono blocchi di codice autonomi che possono essere eseguite e chiamate in qualsiasi punto del codice, 
#eseguono una determinata operazione

#La funzione è un modo di organizzare il codice in unità modulari, sono la base della modularità
#fatta una funzione(bene) non avrai bisogno di riscriverla, essendo generica, la puoi copia incollare in un altro file modificando le variabili
#Come si scrive una funzione?
#def = parola chiave per definire la funzione,
#MatteoDiceCiao = nome della funzione (nome) parametri della funzione, e il corpo della funzione(il print nell'esempio)
#La funzione può avere da 1 a infinite funzioni al suo interno
'''
nome = input("Inserisci un nome: ")
def MatteoDiceCiao(nome):
    
    print("Ciao ", nome)
    
MatteoDiceCiao(nome)
'''
#i parametri sono gli elementi necessari a far si che la funzione venga eseguita
#possono essere da 0 a infiniti

#Chiamata della funzione
'''
addendo1 = int(input("Seleziona un numero: "))
addendo2 = int(input("Seleziona un numero: "))
risultato= 0
def addizione(addendo1 = 0, addendo2 = 0):
    risultato = addendo1+addendo2
    print("La somma dei due addendi è: " , risultato)
    
addizione(addendo1 ,addendo2)
'''
#Le funzioni hanno i parametri, modificabili 
#possono essere tipizzati, es def saluta(nome:str): 
#Parametri di default servono come placeholder (esempio sopra sarebbero addendo1= 0, addendo2= 0)
#Return richiama quello che c'è alla destra del return, nel punto in cui abbiamo richiamato la funzione 
#lo usiamo se ci serve riportare quel dato da qualche parte tipo una lista
'''
n1 = int(input("Seleziona un numero: "))
n2 = int(input("Seleziona un numero: "))
def moltiplicazione (n1=0, n2=0):
    return n1*n2
risultatoM = n1*n2

moltiplicazione(10,15)
print(risultatoM)
'''