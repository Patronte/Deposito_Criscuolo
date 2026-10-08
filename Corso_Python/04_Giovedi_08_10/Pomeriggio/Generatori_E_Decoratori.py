'''GENERATORI

sono unici di python 
sono la base del lavoro di tutti i programmatori al mondo

sono una speciale tipo. di funzione, ti permette di creare un ciclo dentro una funzione
si usano tramite la variabile integrata YIELD, ci serve come un return, ripetibile
all'interno di un ciclo che riassegna alla variabile il nuovo valore, prima di far ripartire il ciclo

DECORATORI
sono una tipologia speciale di funzione che serve a modificare un'altra funzione senza modificare il codice 
si definiscono tramite 2 cose, LA @ e il WRAPPER

COSA FA IL WRAPPER? PRENDE UNA FUNZIONE, E CI PUò METTERE QUALCOSA SENZA MODIFICARE IL CODICE
'''
def decoratore(funzione):
    def wrapper():
        print("Prima dell'esecuzione della funzione")
        funzione()
        print("Dopo l'esecuzione della funzione")
    return wrapper

@decoratore
def saluta():
    print("Ciao!")
    
saluta()

'''MIRKO VUOLE CHE CI RICORDIAMO QUESTO di sopra, ciò che scrivo sotto, è un di +'''

