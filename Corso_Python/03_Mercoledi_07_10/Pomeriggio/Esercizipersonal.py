#PYTHON è un linguaggio di programmazione con 4 peculiarità
#1) è un linguaggio interpretato: significa che il linguaggio che usiamo per programmarlo viene 
# poi passato in linguaggio C prima di essere dato in pasto alla macchina per essere elaborato 
#2) è ad alto livello :(di astrazione) Il che significa che è più vicino al linguaggio umano ché al linguaggio macchina
#3) è dinamico :  il che implica che la sua è una forte tipizzazione delle variabili non è fissa, una x = può essere assegnato ad un numero, 
# ad un boolean, ad una string, ma non può rimanere senza assegnazione    
#4) E' ORIENTATO AGLI OGGETTI: <--Acronimo = OOP significa che la maggior parte di ciò che tratta, viene considerata un oggetto, come le variabili, le funzioni, e così via dicendo.
#4a) la programmazione ad oggetti a sua volta segue 1 regola base e 3 regole  fondamentali
#1 base) astrazione la regola base degli OOP 
#1)Incapsulamento
#2)ereditarietà 
#3)polimorfismo   
#INDENTAZIONE in python l'indentazione è lo spazio a sinistra del codice questo ci aiuta a separare il codice, su livelli di esecuzione, si parte sempre dal livello + a sinistra(livello 0) 
# man mano che si indenta, i livelli vanno a salire.
#LE VARIABILI in python non sono altro che dei contenitori di valori, una variabile può avere vari tipi, string bool int e così via
#per dichiarare una variabile bisogna seguire alcune regole:
#1) Non si possono inserire spazi nel suo nome
#2)può essere formata solo da lettere, numeri e _ trattino basso
#3) DEVONO iniziare con una lettera o un trattino basso, mai numeri.
#Le variabili possono essere usate anche per dichiarare delle COSTANTI, queste ultime saranno sempre VARIABILI, 
#ma verranno dichiarate in full caps lock è una norma tra programmatori.
#esempio variabile peppe = 50 esempio costante PEPPE = 50 
#TIPI DI DATI) principalmente sono due, primitivi e non primitivi
#DATI PRIMITIVI) sono quelli nativi del linguaggio di programmazione, NUMERI (interi e decimali) 
#STRINGHE(contenitori di seguenze di caratteri) CHAR (singolo carattere),BOOL i classici True and False (case sensitive)
#LE STRINGHE SONO SPECIALI PERCHE' COMPOSTE DA SINGOLI ELEMENTI E PERCHE' HANNO I METODI UNICI (len(stringa)) (stringa.upper())/lower/split
#COLLEZIONI IN PYTHON 
#LE LISTE tipo di dato list): una lista è una collezione ordinata e modificabile di elementi, questi possono essere di vari tipi, come interi, stringhe, booleani  anche altre liste e tipi di dati misti. 
# Lista=[] crea una lista vuota lista=[1,2,3,4] lista numerica, lista=[Peppe, 12, true, 4.5] una lista mista, e così via
#le liste sono indicizzate e partono da 0 per esempio se ho una lista=[5,4,3,2] e voglio stampare il secondo numero(4) posso così : Print(lista[1])
#allo stesso modo posso modificarla assegnando un nuovo valore a quello slot specifico  es dalla lista=[5,4,3,2], se scrivo  lista[1]= 20, e rimando la lista in stampa, comparirà così [5,20,3,2]
#per lavorare con le liste ci sono vari metodi incorporati:
# 1) len(lista) restituisce la lunghezza della lista
# 2) lista.append(valoredainserire) aggiungerà come ultimo valore della lista quello scelto
# 3) lista.insert(2, 10) il 2 in parentesi è l'indice di dove deve essere sostituito, e 10 il valore con cui sostituirlo
# 4) lista.remove(elementodarimuovere) rimuoverà l'elemento in lista che corrisponde a ciò che hai scritto in parentesi
# 5) lista.sort() per ordinare gli elementi della lista 


Patro = ["Jesus","Joacchin","Paperin","Mirkettin","Ballerin","Andonio","Ernesto","Liste","Valori"]
Patro.sort()
print(Patro)
