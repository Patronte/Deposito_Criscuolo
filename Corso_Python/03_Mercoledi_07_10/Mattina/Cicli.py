# ogni ciclo parte con 2 domande, qual è la domanda per cui si ripete? qual è il modo per romperlo?


""" #ciclo matematico
conteggio = 0
while conteggio < 5 : #quando ripete(<5)
    print(conteggio)
    (conteggio)+=1 #come romperlo
    
 """
#ciclo che si ripete  una sola volta
"""
while "controllore":
    print("ciao")
    
    
    scelta = input("scrivi end per uscire")
    if scelta.lower()== "end":
    controllore = False
     """    
        
# # si usa il for su valori determinati o determinabili
# #il while quando non sono determinabili

# # il while si divide in condizioni di determinazione e punti di rotture
# #il for ha le condizioni tutte in unica riga

# #ELEMENTO è una variabile che rappresenta l'elemento corrente della
# sequenza in ogni iterazione.
# SEQUENZA è una sequenza di elementi su cui si desidera iterare,
# come una lista, una stringa o l'output della funzione range().
"""
numeri = [1,2,3,4,5]
for numero in numeri:
    print(numero)
    
limite = 5 
for numero in limite:
    print(numero)
    """
#RANGE() è una funzione integrata ci serve a far considerare un numero intero in una collezione, ed essendo definita in partenza/maniera statica, a differenza dell'intero non crea conflitti
#il range crea una sequenza di interi

# range(5) equivale a dire alla macchina che il range vale 1-2-3-4-5
# serve a simulare una sequenza di interi

# usato in una variabile invece, salverà una lista fino al valore descritto

# per definire un range si hanno 3 parametri, lo START (opzionale, se non lo metti parte da 0)
# lo STOP (obbligatorio) definisce la fine della sequenza, non viene conteggiato nella sequenza generata
# STEP (opzionale) conta di quanto va avanti nel conteggio, di base è 1 ma modificabile


#range solo stop conterà da 0 a 4 (5 posizioni)
for i in range(5):
    print(i)
#range start and stop (conterà da 0 a 4) (5 posizioni)
for i in range (0,5):
    print(i)
#range start stop and step (conterà da 0 a 10, lo stop a 10 arriverà a conteggiare fino ad 8 in quanto non tiene conto dell'ultima posizione 
for i in range(0,10,2):
    print(i)
    
#operatore * altresì noto come SPLAT serve a creare le liste
lista = [*range(10)] #ho spalmato il range di 10 dentro una lista
lista2 = [*range(1,10,2)] #creo una lista da 10 andando avanti di due in due
print(lista)
print(lista2)
#se voglio far dare all'utente l'input di start step e stop li chiedo prima e poi li splatto nella lista
scelta1 = int(input("Inserisci lo start "))
scelta2 = int(input("Inserisci lo stop "))
scelta3 = int(input("Inserisci lo step "))
lista3= [*range(scelta1, scelta2, scelta3)]
print(lista3)


#PASS CONTINUE AND BREAK 
il pass si usa quando non si vuole eseguire un'azione all'interno di un ciclo, fa da segnaposto