'''


# Un'azienda vuole gestire i suoi impiegati tramite un sistema informatico. Esistono diversi ruoli all'interno dell'ufficio, ma tutti gli impiegati hanno alcune caratteristiche comuni, come il nome, il cognome e lo stipendio.
# Inoltre, ogni impiegato ha un metodo per calcolare il suo stipendio mensile, che può variare a seconda del ruolo.
# Obiettivi:
# 1. Creare una classe astratta Impiegato con:
# 	• Un costruttore che accetta nome, cognome e stipendio base.
# 	• Un metodo astratto calcola_stipendio() che dovrà essere implementato dalle classi derivate.
# 2. Creare due classi derivate:
# 	• ImpiegatoFisso: riceve lo stipendio base senza modifiche.
# 	• ImpiegatoAProvvigione: riceve lo stipendio base più un bonus basato sulle vendite.
# 3. Implementare una funzione che stampi le informazioni degli impiegati e il loro stipendio calcolato.

#importo il metodo astratto e la classe ABC
from abc import ABC, abstractmethod
#creo la classe impiegato figlia di abc
class Impiegato(ABC):
    #do al costruttore i parame n cgnm stipendio
    def __init__(self, nome,cognome,stipendioBase):
    
        self.nome=nome
    
        self.cognome=cognome
    
        self.stipendioBase=stipendioBase
    #forzo i figli a ereditare il metodo astratto calcola stipendio
    @abstractmethod
    def calcola_stipendio(self):
        pass
    
#creo la classe impiegatofisso figlio di impiegato    
class ImpiegatoFisso(Impiegato):
    #eredito il metodo calcola stipendio, e lo sviluppo
    def calcola_stipendio(self):
        print(f"L'impiegato recepisce {self.stipendioBase} ogni mese")    
    def infoDipendente(self):    
        print(f"L'impiegato {self.nome},{self.cognome} recepisce {self.stipendioBase} ogni mese")

        
#creo l'altra classe figlio, AProvvigione
class ImpiegatoAProvvigione(Impiegato):
    #eredito e sovrascrivo(obbligatoriamente) il metodo del padre
    def calcola_stipendio(self):
        pass
    def infoDipendente(self):    
        print(f"L'impiegato {self.nome},{self.cognome} recepisce {self.stipendioBase} ogni mese")
    
        
#creo l'oggetto ImpiegatoFisso1        
IF1=ImpiegatoFisso("Mirko","Campari(Soda)", 2500)
IAP1=ImpiegatoAProvvigione("Murloc","Aperol",2000)

'''



# Esercizio: Sistema Astratto di Trasporto Merci
# Requisiti
# 1. Classe Astratta: VeicoloTrasporto
# Crea una classe astratta chiamata VeicoloTrasporto, che rappresenti un veicolo generico per il trasporto di merci.
# La classe deve contenere:
# Attributi comuni (protetti)
# • _targa : stringa
# • _peso_massimo : intero (capacità di carico in kg)
# • _carico_attuale : intero (inizialmente 0)
# Metodi
# • Un costruttore che inizializza i campi comuni.
# • Un metodo concreto:
# 	• carica(peso)
# 		• Aumenta il carico attuale se possibile, altrimenti segnala che il peso supera la capacità.
# • Un metodo concreto:
# 	• scarica()
# 		• Riporta il carico attuale a 0.
# • Un metodo astratto:
# 	• costo_manutenzione()
# 		• Ogni veicolo deve avere un costo di manutenzione calcolato secondo regole diverse.
# 2. Sottoclassi Concrete
# Crea almeno tre sottoclassi che estendono la classe astratta e implementano il metodo costo_manutenzione() secondo regole differenti:
# a) Camion
# • Attributo extra: numero_assi
# • Regola manutenzione (esempio):
# 	• 100 € per asse + 1 € per kg di carico massimo
# b) Furgone
# • Attributo extra: alimentazione (es. "diesel", "elettrico")
# • Regola manutenzione:
# 	• Se elettrico: 200 €
# 	• Se diesel: 150 €
# c) Motocarro
# • Attributo extra: anni_servizio
# • Regola manutenzione:
# 	• 50 € per ogni anno di servizio
# 3. Classe GestoreFlotta
# Crea una classe che gestisca un elenco di veicoli:
# Attributi
# • veicoli : lista di oggetti derivati da VeicoloTrasporto.
# Metodi
# • aggiungi_veicolo(veicolo)
# • rimuovi_veicolo(targa)
# • costo_totale_manutenzione():
# 	• Somma dei costi di manutenzione di tutti i veicoli (polimorfismo sugli oggetti astratti).
# • stampa_veicoli():
# 	• Elenca targa, tipo e carico attuale.

#importo il metodo astratto e la classe ABC
from abc import ABC, abstractmethod
#Creo la classe Padre, figlia di ABC
class VeicoloTrasporto(ABC):
    #inizializzo il costruttore con targa e peso max, il carico attuale lo assegno direttamente a 0
    def __init__(self,_targa,_peso_massimo):
        
        self._carico_attuale:int=0
        
        self._targa:str=_targa
        
        self._peso_massimo:int=_peso_massimo
    #la funzione carica peso, con parametro il peso da aggiungere, che immagino di dover chiedere in un input       
    def carica_peso(self,_peso_da_aggiungere):
        #ciclo IF se il carico att è minore del peso max, aggiungimi al carico attuale, il peso da aggiungere
        if self._carico_attuale < self._peso_massimo:
    
            self._carico_attuale+=_peso_da_aggiungere
    
            return

        else:
    
            print("A PIPPO")
    #funzione scarica peso  con parametro di carico attuale = a zero
    def scarica_peso(self,_carico_attuale):
        _carico_attuale==0
        return 
        
    
    #metodo astratto che definisco direttamente nei figli
    @abstractmethod
    def costo_manutenzione(self):
        pass

#creo la classe figlio, eredita i parametri del padre, ed aggiunge il numero di assi
class Camion(VeicoloTrasporto):
    #inizializzo il costruttore con parametro specifico di classe Camion, aggiunto numero assi
    def __init__(self, __targa, __peso_massimo, __carico_attuale,__numero_assi):
        
        self._targa = __targa
        
        self._peso_massimo=__peso_massimo
        
        self._carico_attuale=__carico_attuale
        
        self.numero_assi=__numero_assi    
    #variabile costo manutenzione, un semplice return che moltiplica il valore del numero assi x100 e del peso massimo x1 poi li somma
    #qui avri dovuto aggiungere altro, forse i parametri che utilizzo nel return, affianco al self di manutenzione
     #magari un input per chiedere gli stessi all'utente 
    def costo_manutenzione(self):
        
        return (self.__numero_assi*100)+(1*self.__peso_massimo)


#Classe Furgone figlio di VeicoloT
class Furgone(VeicoloTrasporto):
    #inizializzata al costruttore con aggiunta di alimentazione
    def __init__(self, __targa, __peso_massimo, __carico_attuale,__alimentazione):
        
        self._targa = __targa
        
        self._peso_massimo=__peso_massimo
        
        self._carico_attuale=__carico_attuale
        
        self._alimentazione=__alimentazione
        #funz cost manutenz
    def costo_manutenzione(self):
        #ciclo if alimentazione è elettrico sono 200 sbleuri, se diesel 150, altrimenti non avrai inserito bene il tipo
        if self._alimentazione=="elettrico":
        
            print(f"Il costo della manutenzione è pari ad euro 200")
        
        elif self._alimentazione=="diesel":
        
            print(f"Il costo della manutenzione è pari ad euro 150")
        
        else:
        
            print(f"Sei un pippo, il veicolo com'è alimentato?")            


#Classe Motocarro figlia di VeicoloT
class Motocarro(VeicoloTrasporto):
    #Al costruttore inizializzo anche gli anni di servizio oltre quelli base
    def __init__(self, __targa, __peso_massimo, __carico_attuale,__anni_servizio):
        
        self._targa = __targa
        
        self._peso_massimo=__peso_massimo
        
        self._carico_attuale=__carico_attuale
        
        self._anni_servizio=__anni_servizio
#funzione che mi restituisce in base agli anni di servizio, gli stessi moltiplicati per 50€
#affianco al self della funzione non dovevo mettere nei parametri gli anni serv?
    def costo_manutenzione(self):
        
        return (50*self._anni_servizio)
#Classe esterna (fatherless)
class GestoreFlotta:
    #al costruttore le inizializzo i veicoli, che rendo poi lista
    def __init__(self,veicoli):
    
        self.veicoli=veicoli
    
        veicoli=[]
#immagino avrei dovuto fare un self.veicoli.append()        
    def aggiungi_veicolo(self,veicolo):
    
        pass
#discorso simile con un remove + str in base alla targa    
    def rimuovi_veicolo(self,targa):
    
            pass
    #qui un ciclo for di v in veicoli oppure for {targa} in veicoli se si può fare
    def costo_totale_manutenzione(self):
    
            pass
    #qui ho un ciclo for di v in veicoli, neanche qui sono sicuro andasse proprio bene, il {self.veicoli}, mo so npò inventato, gli altri avevano senso
    #il self.veicoli che ho messo, dovrebbe andare bene perché ho inizializzato i veicoli? o doveva essere veicolo?  
    def stampa_veicoli(self):
    
            for v in self.veicoli:
    
                print(f"il veicolo con targa {self.targa} è di tipo:{self.veicoli} ed il suo carico attuale è di {self.carico_attuale}")
                
                          
#Overall non ho capito molto bene la questione degli underscore se non fosse stato per la traccia, non avrei ne protetto ne privatizzato alcun dato
#e per il gestore flotta, il  menu che avrei potuto creare con un match case o un ciclo while mi andava poi a richiamre cada funzione per cada scelta fatta dall'utente, presa in input, giusto? altrimenti me lo facevo con inputs e prints


