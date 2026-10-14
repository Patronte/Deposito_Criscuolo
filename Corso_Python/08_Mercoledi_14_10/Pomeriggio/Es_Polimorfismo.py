# creare una classe base MetodoPagamento e diverse classi derivate che rappresentano diversi metodi di pagamento. Questo scenario permetterà di vedere il polimorfismo in azione, permettendo alle diverse sottoclassi di implementare i loro specifici comportamenti di pagamento, pur aderendo all'interfaccia comune definita dalla classe base.
# 1. Classe MetodoPagamento:
# 	• Metodi:
# 		• effettua_pagamento(importo): un metodo che ogni sottoclasse dovrà implementare.
# 2. Classi Derivate:
# 	• CartaDiCredito:
# 		• Metodi come effettua_pagamento(importo) che simula un pagamento tramite carta di credito.
# 	• PayPal:
# 		• Metodi come effettua_pagamento(importo) che simula un pagamento tramite PayPal.
# 	• BonificoBancario:
# 		• Metodi come effettua_pagamento(importo) che simula un pagamento tramite bonifico bancario.
# 3. GestorePagamenti:
# 	• Una classe che usa un'istanza di MetodoPagamento per effettuare pagamenti, senza preoccuparsi del dettaglio del metodo di pagamento.
#Creo la classe met pagamento
class MetodoPagamento:
    #le assegno la funzione effettua pagamento senza darle un self.importo=importo altrimenti assegna il valore di importo a metodo pagamento
    def effettua_pagamento(self, importo):
        pass

class CartaDiCredito(MetodoPagamento):
    
    def effettua_pagamento(self, importo):
        
        print(f"Il pagamento di {importo} euro è stato effettuato con Carta di Credito")
        
        
class PayPal(MetodoPagamento):
    
    def effettua_pagamento(self, importo):
            
            print(f"Il pagamento di {importo} euro è stato effettuato con PayPal")

class BonificoBancario(MetodoPagamento):
    
    def effettua_pagamento(self, importo):
            
            print(f"Il pagamento di {importo} euro è stato effettuato con Bonifico Bancario")

class GestorePagamenti:
    def __init__(self, importo):
         pass
    def paga(self, importo):
        pass
    


# Teatro è la classe dove andremo a usare gli elementi, non è imparentata nè a posto standard ne vip, nel teatro ho la lista dei posti , 
# fare solo 3 file e 3 posti, ogni posto può essere occupato da una sola persona potremmo farlo con 3 liste 1 per fila in cui ogni posto è false e quando viene prenotato è true, o il contrario
# 2 classi figlie, posto vip è un extra, le parti obbligatorie sono posto posto standard e teatro,
# Andiamo a creare un sistema ripetibile che simuli un teatro:
# quando prenoto il posto gli dievo chiedere se vuole quello standard e vip, e se vuole il vip quali servizi extra vuole 
# Classe Base: Posto
# • Attributi privati:
# 	• _numero (intero): il numero del posto.
# 	• _fila (stringa): la fila in cui si trova il posto.
# 	• _occupato (booleano): stato del posto, se è occupato (True) o libero (False).
# • Metodi:
# 	• __init__(numero, fila): inizializza il posto impostando _occupato a False.
# 	• prenota(): prenota il posto se non è già occupato; in caso contrario, segnala che il posto è già occupato.
# 	• libera(): libera il posto se è occupato; altrimenti segnala che il posto non era prenotato.
# 	• Getter: per recuperare il numero, la fila e lo stato (occupato/libero).
# Classi Derivate
# • PostoVIP:
# 	• Attributi aggiuntivi: servizi_extra (ad es. una lista di servizi come "Accesso al lounge", "Servizio in posto").
# 	• Metodi:
# 		• Sovrascrive il metodo prenota() per gestire, oltre alla prenotazione, l'attivazione dei servizi extra.
# • PostoStandard:
# 	• Attributi aggiuntivi: costo (un valore numerico che rappresenta il costo della prenotazione, ad esempio per prenotazione online).
# 	• Metodi:
# 		• Può sovrascrivere prenota() per includere la visualizzazione del costo o altre particolarità della prenotazione.
# Classe Teatro
# • Attributi:
# 	• _posti: una lista contenente tutti gli oggetti posti (sia VIP che Standard).
# • Metodi:
# 	• aggiungi_posto(posto): per aggiungere un nuovo posto alla lista.
# 	• prenota_posto(numero, fila): cerca nella lista il posto corrispondente al numero e alla fila indicati e, se lo trova, invoca il metodo prenota() sul posto.
# 	• stampa_posti_occupati(): stampa tutti i posti che risultano occupati.

#creo la classe posto
class Posto:
 #do al costruttore il parametro di _numero #da rivedere se basta numero tra parentesi o fila e occupato sono mandatori
    def __init__(self, _numero):

         self._numero=_numero
#creo la funzione prenota, con parametri di numero e fila 
#prenota e libera vogliono nelle classi figlio anche gli if        
    def prenota(self, _numero,_fila):
        pass
#creo la funzione fila, con stato di occupato e numero, dovrei metterci anche fila?
    def libera(self, _occupato, _numero):
        pass
   #bisogna rivedere i getter e setter se vanno fatti diversamente, se quelli fatti sono almeno in parte giusti
    #col decoratore property andiamo a definire i getter e setter di numero, fila e occupato
    @property    
    
    def _numero(self):
    
        pass
    
    @_numero.setter
    def set_numero(self,_numeroNuovo):
        if len(_numeroNuovo) < 6 :
            pass
    
    
    def _fila(self):
        
        pass
    
    @_fila.setter     
    
    def _occupato(self):
        pass
    @_occupato.setter
        
        pass

#creo la classe PostoStandard
class PostoStandard(Posto):
    #al costruttore do nei parametri numero e costo
    def __init__(self, _numero, costo):
    
        self.costo=costo
#la funzione prenota qui avrà numero e fila, mi domando se lo stato di occupato ci vuole o meno nei parametri, visto che dopo lo userei negli if
    def prenota(self, _numero,_fila):
        pass
    
#creo la classe teatro
class Teatro:
    #al costruttore do il parametro di posto, al quale ho poi assegnato _posto come lista, la consegna voleva sia vip che standard, ma non facendo l'extra non ho bisogno di una seconda lista per i vip
    def __init__(self, _posto):
        self._posto=_posto
        _posto=[]
    # bisogna creare ancora i 3 metodi della consegna