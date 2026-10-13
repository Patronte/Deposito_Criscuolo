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
        
        
        
# Esercizio 1
# Creare una classe base Animale e diverse classi derivate che rappresentano diversi tipi di animali in uno zoo.
# Ogni classe derivata avrà attributi e metodi specifici che riflettono le caratteristiche e comportamenti unici degli animali che rappresentano.
# • Classe Animale:
# 	• Attributi:
# 		• nome (stringa che descrive il nome dell'animale)
# 		• eta (intero che rappresenta l'età dell'animale)
# 	• Metodi:
# 		• fai_suono(): un metodo che stampa un suono generico dell'animale.
# • Classi Figlie:
# 	• Creare almeno tre classi Figlie di Animale ES: Leone, Giraffa, e Pinguino.
# 	• Ogni classe avrà attributi e metodi specifici:
# 		• Per esempio, la classe Leone potrebbe avere un metodo caccia() che stampa un messaggio su come il leone sta cacciando.

class Animale:
   
    def __init__(self, nome,eta,verso):
        self.nome=nome
        self.eta=eta
        self.verso=verso
        
    def fai_suono(self):
        print(f" il verso di/del/della {self.nome} è {self.verso}")

class Leone(Animale):
    def __init__(self, nome, eta, verso,razza):
        Animale.__init__(self, nome,eta,verso)
        self.razza=razza
    
    def caccia(self):
          print("Il Leone caccia di notte, con le scarpe tutte rotte")
    
class Giraffa(Animale):
    def __init__(self, nome, eta, verso,razza):
        Animale.__init__(self, nome,eta,verso)
        self.razza=razza
        
class Elefante(Animale):
    def __init__(self, nome, eta, verso,razza):
        Animale.__init__(self, nome,eta,verso)
        self.razza=razza
        


# Esercizio Ereditarietà
# Esercizio 2
# Lo scopo di questo esercizio è creare un sistema di gestione per una fabbrica che produce e vende vari tipi di prodotti. Gli studenti dovranno creare una classe base chiamata Prodotto e diverse classi parallele che rappresentano diversi tipi di prodotti. Inoltre, dovranno creare una classe Fabbrica che gestisce l'inventario e le vendite dei prodotti.
# 1. Classe Prodotto:
# 	• Attributi:
# 		• nome (stringa che descrive il nome del prodotto)
# 		• costo_produzione (costo per produrre il prodotto)
# 		• prezzo_vendita (prezzo a cui il prodotto viene venduto al pubblico)
# 	• Metodi:
# 		• calcola_profitto: restituisce la differenza tra il prezzo di vendita e il costo di produzione.
# 2. Classi parallele:
# 	• Creare almeno due classi parallele a Prodotto, per esempio Elettronica e Abbigliamento.
# 	• Aggiungere attributi specifici per ciascun tipo di prodotto, come materiale per Abbigliamento e garanzia per Elettronica.
# 3. Classe Fabbrica:
# 	• Attributi:
# 		• inventario: un dizionario che tiene traccia del numero di ogni tipo di prodotto in magazzino.
# 	• Metodi:
# 		• aggiungi_prodotto: aggiunge prodotti all'inventario.
# 		• vendi_prodotto: diminuisce la quantità di un prodotto in inventario e stampa il profitto realizzato dalla vendita.
# 		• resi_prodotto: aumenta la quantità di un prodotto restituito in inventario.


class Prodotto:
    
    def __init__(self,nome, costo_produzione,prezzo_vendita):
        
        self.nome=nome
        
        self.costo_produzione=costo_produzione
        
        self.prezzo_vendita=prezzo_vendita
        
    
    def calcola_profitto(self):
        
        return self.prezzo_vendita-self.costo_produzione
    
class Abbigliamento(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita,materiale):
        
        Prodotto.__init__(self,nome, costo_produzione, prezzo_vendita)
        
        self.materiale=materiale

class Elettronica(Prodotto):
    
    def __init__(self, nome, costo_produzione, prezzo_vendita, ram):
        
        Prodotto.__init__(self, nome, costo_produzione, prezzo_vendita)
        
        self.ram=ram
#da qui guidato nella logica da IA        
class Fabbrica:
    
    def __init__(self):
    
        self.inventario=[]
    
    def aggiungi_prodotto(self,prodotto):
        self.inventario.append(prodotto)
        
        
    
    def vendi_prodotto(self, prodotto):
        self.inventario.remove(prodotto)
        return prodotto.prezzo_vendita-prodotto.costo_produzione
    def resi_prodotto(self):
        pass