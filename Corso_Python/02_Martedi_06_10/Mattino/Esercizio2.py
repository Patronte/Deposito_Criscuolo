#IF ELSE ELIF

#Creare una serie di condizioni una dentro l'altra che a fronte di un umput per ogni if decidano se farti passare o no( 3 livelli, fate un paragone con ==)
#Andare a creare un if con vari elif e un else finale che gestisca un menu per la selezione di un crud basilare  append remove modifica
#Primo Esercizio IF ANNIDATO
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

#Esercizio 2 tramite le liste, aggiungi, rimuovi, modifica
stanzeOccupate= [12,40,27,86,50]
if stanzeOccupate >= 5 :
    print("L'albergo è pieno")
elif stanzeOccupate < 5 : 
    print("Ci sono stanze disponibili")
elif stanzeOccupate != 0:
    print("Ci sono stanze occupate")
else : 
    print("Non ci sono stante disponibili")
    
# quello di sopra not so much, ecco come l'ha fatto Mirko

lista = [1,2,3,]
scelta = input("Cosa vuoi fare? aggiungi, rimuovi, modifica")

if scelta == "aggiungi" : 
   scelta2 = input("scegli la parola")
   lista.append(scelta2)
   
   print(lista)
elif scelta == "modifica":
    print("Scegli quale posizione modificare da 0 con limite a", len(lista)-1)
   scelta2 = int(input("Scegli il numero"))
   lista.remove(scelta2)
   
   print(lista)
elif scelta == "modifica":
    print("scegli quale posizione modificare da 0 con limite a", len(lista)) 