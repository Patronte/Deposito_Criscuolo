""" Appunti di Python, riordinati
1. Cos'è Python

Python è un linguaggio di programmazione con queste caratteristiche:

Interpretato: il codice che scriviamo viene tradotto ed eseguito da un interprete, senza dover creare prima un eseguibile.
Ad alto livello: ha un alto livello di astrazione, cioè è vicino al linguaggio umano e lontano da quello della macchina. Basso livello significa più vicino alla macchina.
Dinamico: una variabile può cambiare tipo (x = 5, poi x = "Mirko"), ma non può mai esistere senza un valore e quindi senza un tipo.
Orientato agli oggetti (OOP): la maggior parte di ciò che Python tratta è un oggetto (variabili, funzioni, ecc.).
Sicuro, ma più lento di altri linguaggi.

È un vero linguaggio di programmazione perché ha 3 elementi fondamentali: variabili, condizioni e cicli, funzioni.

OOP: le regole

Importantissima a livello lavorativo, ci aiuta a non ripetere lavoro. Essere OOP significa rispettare:

1 regola base: astrazione
3 regole fondamentali: incapsulamento, ereditarietà, polimorfismo
2. Le 3 capacità del programmatore

In ordine di importanza:

Leggere il codice
Metodologia
Scrivere il codice

Esplorare le librerie fa parte della metodologia: per sapere cosa fa float, lo scrivo in VS Code e leggo la descrizione che compare.

3. Struttura del codice

Indentazione: è lo spazio a sinistra della riga. Separa il codice in livelli di esecuzione: si parte dal livello 0 (più a sinistra) e a ogni indentazione si sale di livello. Se sbagli l'indentazione, il codice si rompe. Virgole e punti e virgola, invece, contano pochissimo.

Commenti

# commenta una singola riga
''' ... ''' (triplo apice) commenta più righe. Serve anche per escludere un pezzo di codice dall'esecuzione.
4. Funzioni integrate

Una funzione integrata (built-in) è già presente nel linguaggio, non l'abbiamo scritta noi. Si riconosce dalle parentesi tonde dopo il nome.

Quelle usate finora: print(), input(), int(), float(), len(), range().

python
nome = input("Inserisci il tuo nome: ")
eta = int(input("Inserisci la tua età: "))
print("Ciao, " + nome + "! Benvenuto in Python")
print(eta * 2)

Operazioni di base con print: 2+5, 6-5, 4/2, 4*2.

5. Variabili e tipi di dati
Variabili

Una variabile è un contenitore di valori. Una volta dichiarata, ogni volta che ripeti il suo nome ti riferisci alla stessa porzione di memoria.

Schema: nomeVariabile (nome) = (operatore di assegnazione) valore (che può essere un numero, una stringa, un booleano...). Il tipo dipende dal valore assegnato.

Regole per il nome:

Niente spazi
Solo lettere, numeri e trattino basso _
Deve iniziare con una lettera o con _, mai con un numero

Convenzione: le variabili si scrivono con l'iniziale minuscola (nomeVariabile, nome1, nomeCognome).

Costanti: sono comunque variabili, ma per convenzione si scrivono tutte maiuscole. Esempio: variabile peppe = 50, costante PEPPE = 50.

Tipi di dati

Due macrogruppi:

Primitivi (basilari): già presenti in Python
Non primitivi: li creiamo noi, in pratica sono gli oggetti

Primitivi:

int: numeri interi
float: numeri con la virgola (si scrive con il punto), positivi o negativi
str (stringhe): testo tra virgolette
char: singolo carattere
bool: True e False (rispettare maiuscole e minuscole)

Su int e float si possono fare le operazioni aritmetiche comuni.

Stringhe: sono primitive ma speciali, perché contengono più elementi (ogni lettera è un char) e hanno metodi propri: len(stringa), stringa.upper(), .lower(), .split().

python
a = "Magicka"
print(a[5])    # si parte a contare da 0

saluto = "Ciao"
nome = "Patronte"
messaggio = saluto + " " + nome    # concatenazione con +
print(messaggio)

Conversioni: da un tipo all'altro con int(), float(), bool().

6. Collezioni: le liste

La lista (tipo list) è una collezione ordinata e modificabile di elementi. Non è né un tipo primitivo né non primitivo: è un tipo composto.

4 caratteristiche:

Tipo: list
Elementi: possono essere misti (numeri, stringhe, booleani, anche altre liste)
Definizione: si scrivono con le parentesi quadre
Ordinamento: sono ordinate e modificabili

La peculiarità delle liste sono i metodi.

python
vuota = []
listaNum = [1, 2, 3, 4, 5, 10]
listaNom = ["Peppe", "Mirko", "Andonio"]
listaMisto = ["Peppino", 2, True, 4.20]
Indici

Si parte da 0. Con lista = [5, 4, 3, 2], print(lista[0]) dà 5 e print(lista[1]) dà 4.

Si può modificare un singolo elemento assegnandogli un nuovo valore: lista[1] = 20 → [5, 20, 3, 2].

(aggiunta) Gli indici negativi contano dalla fine: lista[-1] è l'ultimo elemento, lista[-2] il penultimo.

Metodi principali
Metodo	Cosa fa
len(lista)	restituisce la lunghezza
lista.append(x)	aggiunge x in fondo
lista.insert(i, x)	inserisce x alla posizione i (non sostituisce, sposta gli altri)
lista.remove(x)	rimuove il primo elemento uguale a x
lista.sort()	ordina la lista
python
listaNum = [15, 2, 25, 4, 5, 10]
listaNum.append(6)
listaNum.remove(10)
listaNum.sort()
print(listaNum)
7. Controllo del flusso

Il controllo del flusso è la capacità di alterare ciò che viene letto in esecuzione, escludendo o ripetendo parti di codice.

Famiglie:

Esclusivo: le condizioni (if, else, match)
Ripetitivo: i cicli/iterazioni (for, while)
[DA COMPLETARE: la terza famiglia citata a lezione; probabilmente le istruzioni di salto break, continue, pass, da verificare]
7.1 Condizioni

if / else: else aggiunge un "altrimenti". L'indentazione indica cosa appartiene all'if.

python
x = 1
if x > 9:
    print("Eccellente")
else:
    print("Sub-Eccellente")

elif: può stare solo dopo l'if e mai dopo l'else. Se ne possono avere quanti si vuole, ma sempre un solo if e un solo else. Viene eseguito solo il primo blocco con condizione vera.

python
if x > 0:
    print("maggiore di 0")
elif x == 1:
    print("uguale a 1")
else:
    print("niente")

if annidati: un if dentro un altro if.

python
if x > 0:
    print("Il numero è positivo")
    if x == 100:
        print("è proprio 100")
else:
    print("Il numero è zero")

match: controlla un'uguaglianza su più casi. Ha senso in un menù, tipicamente con le stringhe. Per gli altri tipi di confronto si usa in genere l'if.

python
comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case _:
        print("Comando non riconosciuto.")

case _ è il caso di default.

7.2 Cicli

I cicli ripetono un blocco di codice finché una condizione è vera. Ogni ciclo parte con 2 domande:

Quando si ripete? (la condizione)
Come lo rompo? (cosa fa finire il ciclo)

Quando usare quale:

for: su valori determinati o determinabili
while: quando non sono determinabili in anticipo

Il while ha la condizione e il punto di rottura in punti diversi; il for ha tutto in un'unica riga.

while

python
conteggio = 0
while conteggio < 5:       # quando si ripete
    print(conteggio)
    conteggio += 1         # come lo rompo

(aggiunta) Prima di scrivere un while, controlla: quale variabile è nella condizione? Dentro il ciclo cambia? Cambia nella direzione giusta per far diventare la condizione falsa? Se no, è un ciclo infinito (si ferma con Ctrl + C).

Esempio con uscita controllata:

python
continua = True
while continua:
    print("ciao")
    scelta = input("Scrivi end per uscire: ")
    if scelta.lower() == "end":
        continua = False

for

python
numeri = [1, 2, 3, 4, 5]
for numero in numeri:
    print(numero)
elemento (numero): variabile che rappresenta l'elemento corrente a ogni iterazione
sequenza (numeri): ciò su cui si itera (lista, stringa, range())

Attenzione: non si può iterare direttamente su un intero. for numero in 5 dà errore, serve range(5).

range()

Funzione integrata che genera una sequenza di numeri interi, utile per far ripetere un for un certo numero di volte. Ha 3 parametri:

start (opzionale, default 0)
stop (obbligatorio): fine della sequenza, escluso
step (opzionale, default 1): di quanto avanza
python
for i in range(5):          # 0, 1, 2, 3, 4
    print(i)
for i in range(0, 5):       # 0, 1, 2, 3, 4
    print(i)
for i in range(0, 10, 2):   # 0, 2, 4, 6, 8
    print(i)

Per trasformare un range in lista si usa l'operatore * (splat), che "spalma" gli elementi dentro la lista:

python
lista = [*range(10)]            # 0..9
lista2 = [*range(1, 10, 2)]     # 1, 3, 5, 7, 9

Se l'utente decide start, stop e step, li chiedo prima con input e poi li passo al range:

python
start = int(input("Inserisci lo start "))
stop = int(input("Inserisci lo stop "))
step = int(input("Inserisci lo step "))
lista3 = [*range(start, stop, step)]

break, continue, pass

break: esce subito dal ciclo
continue: salta il resto del blocco e passa all'iterazione successiva
pass: non fa niente, fa da segnaposto dove il codice richiede un blocco
8. Funzioni

Le funzioni sono la prova pratica dell'astrazione: blocchi di codice autonomi che eseguono una determinata operazione e si possono chiamare in qualsiasi punto del codice. Sono la base della modularità: scritta bene, una funzione è generica e si riusa (anche in un altro file cambiando le variabili).

Come si scrive:

def: parola chiave per definirla
nome della funzione
parametri tra parentesi (da 0 a infiniti)
corpo della funzione (le istruzioni indentate)
python
def saluta(nome):
    print("Ciao ", nome)

saluta("Mirko")      # chiamata

Parametri

Sono gli elementi necessari perché la funzione venga eseguita
Possono essere tipizzati: def saluta(nome: str):
Possono avere un valore di default, che fa da segnaposto:
python
def addizione(addendo1=0, addendo2=0):
    risultato = addendo1 + addendo2
    print("La somma è:", risultato)

addizione(3, 4)

return

Restituisce il valore scritto alla sua destra nel punto in cui la funzione è stata chiamata. Serve quando il dato deve essere riutilizzato altrove (in una variabile, in una lista...).

python
def moltiplicazione(n1=0, n2=0):
    return n1 * n2

risultatoM = moltiplicazione(10, 15)
print(risultatoM)     # 150
9. Generatori e decoratori

Sono tipici di Python e molto usati dai programmatori. Mirko vuole che li ricordiamo bene; ciò che segue è un approfondimento in più.

Generatori
Sono un tipo speciale di funzione che permette di creare un ciclo dentro una funzione. Usano la parola chiave yield, che funziona come un return ripetibile: restituisce un valore, poi la funzione riparte da dove si era fermata, riassegnando il nuovo valore.

Decoratori
Sono funzioni speciali che modificano un'altra funzione senza toccarne il codice. Si definiscono con due elementi: la @ e il wrapper. Il wrapper prende una funzione e ci aggiunge qualcosa prima e/o dopo.

python
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
10. Strumenti

VS Code: le barre (da verificare con quanto detto in aula)

Barra verticale/laterale (icone: file, ricerca, git, estensioni): lavora sull'intero progetto/workspace
Barra orizzontale/in alto (menu): lavora sul singolo file o lavoro specifico

GitHub
Sistema di versionamento: come i salvataggi di un videogioco, ma per le versioni di un programma.
Perché lo usiamo: per tenere traccia delle modifiche nel tempo, tornare a una versione precedente se qualcosa si rompe, e lavorare in team senza sovrascrivere il lavoro altrui.

11. Domande probabili di Mirko (ripasso rapido)
Cos'è una funzione integrata e come la riconosco? Funzione già pronta nel linguaggio; ha le parentesi tonde dopo il nome (print(), len(), range()).
Le 3 capacità del programmatore? Leggere, metodologia, scrivere (in ordine di importanza).
VS Code: barra orizzontale e verticale? Verticale = progetto intero; orizzontale = file singolo (da riconfermare).
Cos'è l'indentazione? Lo spazio a sinistra del codice; separa i livelli di esecuzione, se è sbagliata il codice si rompe.
Cos'è Python? Interpretato, ad alto livello, dinamico, orientato agli oggetti, sicuro ma più lento.
Cos'è GitHub e perché usarlo? Versionamento: tracciare le modifiche, tornare indietro, lavorare in team.
4 caratteristiche delle liste? Tipo list, elementi misti, parentesi quadre, ordinate e modificabili; peculiarità: i metodi.
Cosa sono i controllori del flusso? Gli elementi che dicono come vengono lette le righe: condizioni, cicli e [terza famiglia da completare]. """