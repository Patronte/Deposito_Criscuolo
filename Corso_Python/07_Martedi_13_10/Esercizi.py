# Ecco la trascrizione del testo presente nell'immagine:
# Esercizio 5 (Facile) @staticmethod:
# Crea una classe chiamata Convertitore. Questa classe dovrebbe avere:
# • Un metodo statico euro_in_dollari che accetti un importo in euro e restituisca il valore convertito in dollari, usando un tasso fisso di 1.08.
# • Un metodo statico km_in_miglia che accetti una distanza in chilometri e restituisca il valore convertito in miglia, usando un fattore fisso di 0.621371.
# Testa la classe chiamando entrambi i metodi direttamente dalla classe, senza creare alcun oggetto.

#CIAO MIRKO, QUI CREO LA CLASSE CONVERTITORE
class convertitore:
    #QUI gli dico che il metodo def è statico
    @staticmethod
    #Qui gli dico che il "parametro" che non è il termine giusto durante la creazione della def, ma solo nel riempimento di essa, è importo
    def euro_in_dollari(importo):
        #Qui assegno importo ad importo
        importo=importo
        #Qui mi dichiaro il tasso di valuta
        tasso_valuta=1.08
        #Qui il tasso me lo calcolo moltiplicato per l'importo dato
        return importo*tasso_valuta
    
    #Dichiaro sempre metodo statico
    @staticmethod
    #creo def per convertire le distanze, argomento è distanza
    def km_in_miglia(distanza):
        #assegno distanza a distanza
        distanza=distanza
        #creo la var di conversione
        conversione = 0.621371
         #calcolo la distanza per la conversione
        return distanza*conversione
        
#Qui mi printo l'euro in dollari, del convertitore, con una cifra inserita di 125    
print(convertitore.euro_in_dollari(125))
#Qui stesso discorso perle miglia
print(convertitore.km_in_miglia(12))




# Esercizio 6 (Facile) @classmethod:
# Crea una classe chiamata Animale. Questa classe deve avere:
# • Un attributo di classe numero_animali, inizializzato a 0.
# • Due attributi di istanza: nome e specie, passati al costruttore.
# • Il costruttore deve incrementare numero_animali di 1 ogni volta che viene creato un nuovo animale.
# • Un metodo di classe quanti_animali che stampi una stringa del tipo "Numero di animali creati: 'numero_animali'".
# Crea almeno 3 oggetti Animale e poi chiama quanti_animali direttamente dalla classe, senza usare nessuna delle istanze create.


#creo class animale
class Animale:
    #gli dico che inizia da 0 animali, questo lo stavo inserendo come argomento del costruttore col default a 0
    numero_animali=0  
    #gli do specie e n    
    def __init__(self,nome, specie):
        self.nome=nome
        self.specie=specie
    
    def quanti_animali():
        print("Numero di animali creati: "+ Animale.numero_animali)    