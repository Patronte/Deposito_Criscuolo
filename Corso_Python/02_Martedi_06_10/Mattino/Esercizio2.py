#IF ELSE ELIF

#Creare una serie di condizioni una dentro l'altra che a fronte di un umput per ogni if decidano se farti passare o no( 3 livelli, fate un paragone con ==)
#Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare  append remove modifica
'''
#Esercizio 1  IF ANNIDATO
passwordUtente = input("Inserisci una password a caso ")

passwordCorretta = "Password123"

if passwordUtente != passwordCorretta: 
   
    passwordUtente = input("Inserisci la password sbagliata ")
    
    print("Password Errata!")
    
    if passwordUtente == passwordCorretta:
    
        passwordUtente = input("Inserisci la password giusta ")
      
        print("Accesso Consentito")
       
        if passwordUtente == "":
        
            passwordUtente = input("Non Inserire una password ")
        
            print("Inserisci una password nel campo richiesto")

#Esercizio 2, errato/incompleto  tramite le liste, aggiungi, rimuovi, modifica
stanzeOccupate= [12,40,27,86,50]
if stanzeOccupate >= 5 :
    print("L'albergo è pieno")
elif stanzeOccupate < 5 : 
    print("Ci sono stanze disponibili")
elif stanzeOccupate != 0:
    print("Ci sono stanze occupate")
else : 
    print("Non ci sono stante disponibili")
    
# Esercizio 2 tipo 2 (svolto da prof Mirko)
#dati
lista = [1,2,3]
scelta = input("cosa vuoi fare? aggiungi, rimuovi, modifica ")

if scelta == "aggiungi" :
    scelta2 = input("scegli una parola")
    lista.append(scelta2)
    
    print(lista)
elif scelta == "rimuovi":
    print("scegli cosa rimuovere fra: ", lista)
    scelta2 = int(input("scegli il numero "))
    lista.remove(scelta2)
    
    print(lista)  
elif scelta == "modifica":
    print("scegli quale posizione modificare da 0 con limite a", len(lista)-1 )
    scelta2 = int(input("scegli una posizione"))
    scelta3 = input("scegli una parola da aggiungere")
    lista[scelta2] = scelta3
    
    print(lista)   
else: 
    
    print("Scelta sbagliata")
    
    '''
    #Esercizio 2 tipo 3 (svolto da me)
    
lista1 = ["Tizio","Caio","Sempronio","Genovebba","Moretti","Mirko", "Caparezza"]
lista2 = [1,2,3,4,5,6,7]
scelta = input("Quale lista vuoi confrontare? lista1 o lista2? ")
if scelta == "lista1" :
    print(lista1)
    
    if scelta == "lista1" :
        input(modifica)
    elif modifica == "aggiungi":
        input("Scegli cosa aggiungere")
        lista1.append(lista1)
        
elif scelta == "lista2":
    print(lista2)
else : 
    print("Scelta errata, riprova")
    
