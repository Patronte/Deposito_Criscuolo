 # Esercitazione
#  Scrivi un programma che esegua le seguenti operazioni:
#  1. Chiedi all'utente di inserire un numero intero positivo n. Se l'utente inserisce un numero negativo o zero, continua a chiedere un numero fino a quando non viene inserito un numero positivo.
# non è una funzione


#chiedo un numero all'utente
richiestaN = int(input("Inserisci un numero positivo: ")) 
#fintanto che il numero è minore o uguale a 0, glielo richiedo
while richiestaN <= 0:
    #richiedo l'input all'utente
    retry = int(input("Pippo Inserisci un numero positivo: "))
    #se il nuovo input è maggiore di 0, OPPURE la richiestaN è maggiore di 0 
    if retry >0 or richiestaN > 0:
#assegna a richiestaN il valore di retry (questo non ha troppo senso, forse dovevo separare le due condizioni)
        retry=richiestaN
#Commentino provocatorio all'utente
        print("Era facile")
#avevo messo il break per chiudere il while, ma se devo unire tutti i punti credo mi darà problemi questo break        
        break
#Commentino provocatorio all'utente    
    else:
        print("Pippus Maximus ")
        
#  2. Genera una lista di numeri interi casuali tra 1 e n (incluso). La lunghezza della lista deve essere n.
# usa i range

#Qui potevo non usare il for ed uitlizzare lo splatter nel range, ci ho provato dopo aver svolto questo così, non riuscivo ed ho eliminato il tentativo
#mi son generato la lista col ciclo for, e tramite il  +1 ho incluso l'ultimo numero e mandato i singoli elementi in stampa. Ora sto dubitando di aver seguito effettivamente la traccia o meno, nello specifico la parte della lista 
for n in range(richiestaN+1):
    print(n)

#  3. Utilizza un ciclo for per calcolare e stampare la somma dei numeri pari nella lista.
  #Qui ho sfruttato il for precedente, visto che pensavo fosse corretto, ora dubito ancora della questione lista visto che dubito di averne stampate 
    
#ciclo for 
for n in range(richiestaN+1):
    #se è pari, aggiungi ad n, n stesso, e poi stampamelo, non credo rispetti comunque la richiesta 
        if n % 2==0:
            n=n+n
          
            print(n)
#altrimenti stampami la verità
        else:
            print("Sei un Mega Pippo")
            # i give up let's go next  #commento del commento, qui mi so arreso     

# se gli faccio fare lo step non viene bene meglio usare solo lo stop
#  4. Utilizza un ciclo for per stampare tutti i numeri dispari nella lista.
#Qui liscio come l'olio, perché mi so creato la lista e l'ho utilizzata, sarà stato il range a buggarmi?
listaN=[1,2,3,4,5,6,7,8,9]
#per ogni numero nella lista se è dispari stampamelo
for n in listaN:
    if n % 2 != 0:
        print(n)

# esercizio di ieri al contrario
#  5. Utilizza un ciclo per determinare se un numero è pari. La funzione deve restituire True se il numero è pari, altrimenti False.
# se non voglio usare il numero primo uso il pari o dispari se faccio pari e dispari mi servono due funzioni

#inputto il numero 
chiedoN = int(input("Inserisci un numero, ti dico se è pari o dispari: ")) 

#creo la funziuone per analizzare se il numero in input è pari o dispari
def pari_dispari (chiedoN):
    if chiedoN % 2==0:
        print("Il nummero è Pari")
    else:
        print("Il numero è dispari")
#richiamo la funzione, avendo con parametro l'input utente        
pari_dispari(chiedoN) 
#se è pari assegno true all'input utente, altrimenti gli assegno false
if chiedoN % 2==0:
    chiedoN=True
else:
    chiedoN=False 
    
#forse ho rispettato la consegna




#  6. Utilizza un ciclo for per stampare tutti i numeri primi nella lista.

#  7. Infine, utilizza una struttura if per determinare se la somma di tutti i numeri nella lista è un numero primo e stampa il risultato
# come punto 5
#  8. tutto tramite funzioni richiamabili dal menu
# non è una funzione ( un while che mi chiede quale funzione voglio)  while if else  oppure il match   un unico while che deve eseguire queste operazioni 
# isola e poi unisci



