
        

#Esercizio:  Andare a creare un sistema ripetibile 
# che permetta di inserire: sia al fondo che nella posizione che vogliamo noi,
# modificare, stampare ed eliminare liste, che sono divise dal tipo che viene scelto.
lista1=[1,2,3]
lista2 = ["Pippo", "Giovanna", "Maurizio"]

sceltaUtente = str(input("Su che lista vuoi lavorare? lista1(Numeri), lista2(Nomi) "))

if sceltaUtente.lower() == "lista1":
    print(lista1)
    sceltaUtente=lista1
    sceltaOp= int(input("Che operazione vuoi eseguire? inserire a fine lista(1), inserire dove vuoi(2), modificare(3) stampare(4) eliminare lista(5)"))
    match sceltaOp:
        case "1":
            sceltam1= int(input("Cosa vuoi inserire a fine lista? "))
            lista1.append(sceltam1)
            print(lista1)
        case "2":
            print(lista1)
            inserimento = int(input("Che elemento vuoi inserire, ed in che posizione? 0 è la prima posizione, seleziona prima la posizione, e poi ciò che vuoi inserire tipo  2, 15  "))
            
                        
elif sceltaUtente.lower() == "lista2":
    print(lista2)
    sceltaUtente=lista2
else:
    print("Scelta non valida")
#Esercizio:  Andare a creare un sistema ripetibile che obblighi l'utente a inserire nome e codice, poi l'utente può accedere ad un secondo pezzo del menu, 
# solo se ha inserito i dati nella fase prima e dopo un login (codice == codice e nome == nome) questa seconda parte deve permettere di visionare due operazioni,
# somme e sottrazioni e salvare ogni risultato di ogni operazione, entrambi i menu ripetibili ( menu: registrazione // login --> dentro login: le due operazioni e visualizza risultati)



