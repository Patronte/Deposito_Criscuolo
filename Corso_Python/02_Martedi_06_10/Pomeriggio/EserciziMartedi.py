#presi gli esercizi svolti dalla repository di Mirko,
#Chiesto a Claude di estapolarmi una traccia per ogni esercizio
#Svolti da solo, facendomi aiutare da AI se necessario


# Esercizio 1 — Validazione a cascata
# Chiedi un numero all'utente. Se è maggiore di 10, chiedine un secondo. Se anche questo è maggiore di 50, chiedine un terzo.
# Se anche questo è maggiore di 100, stampa un messaggio di vittoria. Usa if annidati, uno dentro l'altro, su tre livelli.

""" x = int(input("Scrivi un numero: "))

if (x > 10):
    y = int(input("Scrivi un ulteriore numero: "))
    
    if (y > 50):
        z = int(input("Scrivi un ultimo numero: "))
        
        if (z > 100):
            print("Vittoria, sei un Pippo! ")
        else : 
            print("Riprova, sarai più fortunato ")
    else : 
        print("Riprova, sarai più fortunato ")    
else : 
    print("Riprova, sarai più fortunato ")
 """    
# Nota ES.1: risolto autonomamente, litigato con gli else che non avevo scritto in prima stesura, soluzione trovata a trial and error negli errori del terminale, a na certa avevo
# dichiarato nella condizione del 3° if z come un int--> if (int(z > 100)) l'ho tolto rendendomi conto che era superfluo e non mi dava errore per quel motivo

# Esercizio 2 — Gestione lista con menu (aggiungi/rimuovi/modifica)
# Parti da una lista con qualche elemento. Chiedi all'utente cosa vuole fare: aggiungere(append), rimuovere(remove) o modificare(riassegna un valore ad una lista esistente, selezionando in quale posizione).
# Aggiungi: chiedi un nuovo elemento e inseriscilo in fondo alla lista.
# Rimuovi: mostra la lista, chiedi quale elemento togliere (per valore, non per posizione) e rimuovilo.
# Modifica: chiedi una posizione e un nuovo valore, poi sostituisci l'elemento in quella posizione.
# Se la scelta non corrisponde a nessuna delle tre, stampa un messaggio di errore.
# Dopo ogni operazione, stampa la lista aggiornata.

#Nota Esercizio già svolto letto alla veloce prima di procedere 
'''
lista = [1,2,3,4,5]
scelta = input("Che operazione vuoi fare? aggiungere, rimuovere o modifica ")

if scelta.upper() == "AGGIUNGERE" :  #sto cazzo di upper(), l'ho provato in tutte le righe di questo if 
    
    scelta1 = int(input("Scrivi il numero che vuoi aggiungere "))
   
    lista.append(scelta1)
   
    print(lista)

elif scelta.upper() == "RIMUOVERE":
   
    print(lista)
   
    scelta2 = int(input("Scrivi quale numero vuoi rimuovere "))
   
    lista.remove(scelta2)
  
    print(lista)

elif scelta.upper() == "MODIFICA" :
  
    print(lista)
  
    print("Scegli quale posizione modificare da 0 con limite a ", len(lista)-1)
   
    scelta3 = int(input("da quale posizione vuoi modificare il numero? "))
    
    scelta4 = int(input("Con quale numero vuoi sostituirlo? "))
   
    lista[scelta3] = scelta4
    
    print(lista)

else :
   
    print("Scelta errata, riprovare ")
'''
#Nota ESERCIZIO 2 è stato no scristo,  -->  len(lista)-1)  e la modifica non sapevo come farla, né la modifica del valore in base alla posizione
#NOTA mi son guardato l'esercizio svolto per risolvere questi 2 intoppi

# Esercizio 3 — Maggiore età con match-case
# Chiedi l'età. Verifica se è maggiore o uguale a 18 (valore booleano). Trasforma quel risultato in una stringa ("maggiorenne" o "minorenne").
# Usa un costrutto match-case su quella stringa per stampare se può vedere il film oppure no.
'''
eta = int(input("Quanti anni hai? "))

if eta >= 18: 
    
    eta = "MAGGIORENNE"

elif eta < 18 and eta > 0: 

    eta = "MINORENNE"

else :
    print("Riprova, e scrivi la tua eta. ") 

    
match eta:
    
    case "MAGGIORENNE":
    
        print("Sei maggiorenne, goditi il film. ")
    
    case "MINORENNE":
    
        print("Sei minorenne, non te poi vede er film. ")
    
    case _:
    
        print("Anno di nascita non confermato, verifica la tua eta. ")
'''
#ESERCIZIO 3 NOTAE, ci ho molto più di quanto avrei dovuto, mi son rivisto il mio esempio di match e case fatto in Condizioni2.py per sbloccarmi la memoria


# Esercizio 4 — Calcolatrice con match-case
# Chiedi due numeri e un'operazione (addizione, sottrazione, moltiplicazione, divisione). Usa match-case per eseguire l'operazione giusta e stampare il risultato.
# Per la divisione, controlla prima se il secondo numero è zero: in quel caso stampa un messaggio invece di dividere.

operando1 = int(input("Seleziona il primo numero "))
operando2 = int(input("Seleziona il secondo numero "))
operazione = input("Seleziona il tipo di operazione: addizione +  sottrazione - moltiplicazione *  divisione / ")
operazione = operazione.lower()
match operazione:
    case "addizione":
        print(operando1+operando2)
    case "+" :  
        print(operando1+operando2)
    case "sottrazione":
        print(operando1-operando2)
    case "-":
        print(operando1-operando2)
    case "moltiplicazione":
        print(operando1*operando2)
    case "*":
        print(operando1*operando2)
    case"divisione" :
        if operando2 == 0 :
            print("MA CHE STAI A FA NUN SE PO DIVIDE PE ZERO AO")

    case"/" :
        if operando2 == 0 :
            print("MA CHE STAI A FA NUN SE PO DIVIDE PE ZERO AO")
        else: print(operando1/operando2)
    case "divisione":
        print(operando1/operando2)
    case "/":
        print(operando1/operando2)

#NOTEES4 dai Mirko ma che evoluzione qua, messo il .lower  alla singola variabile operazione  invece che ad ogni case come prima, e t'ho fatto pure sia testo che simbolo per l'operazione  
#poi però è venuto fuori l'if e la ho risolto a modo mio, però sento che avrei dovuto cancellare qualcosa, tipo una coppia di divisione senza l'if, non so se quell'else che ho messo, si applica a tutti e 2 gli if o no, e nsomma...       
# Esercizio 5 — Due liste, scelta per tipo
# Crea due liste: una di numeri, una di parole. Chiedi all'utente se vuole lavorare con le stringhe (S) o con i numeri (N). In entrambi i casi, 
# chiedi poi se vuole aggiungere o rimuovere un elemento, e agisci sulla lista corrispondente (stringhe o numeri). Gestisci anche il caso in cui
# la prima scelta non sia né S né N. Stampa la lista aggiornata dopo ogni operazione.