#Esercizio 3 (Medio):
# Crea una classe chiamata ContoCorrente. Questa classe dovrebbe avere:
# • Due attributi di istanza: intestatario e saldo (il saldo iniziale deve essere passato al costruttore, con valore di default 0).
# • Un metodo deposita che accetti un importo e lo aggiunga al saldo. Se l'importo è negativo o zero, stampa un messaggio di errore senza modificare il saldo.
# • Un metodo preleva che accetti un importo e lo sottragga dal saldo. Se il saldo non è sufficiente, stampa un messaggio di errore senza modificare il saldo.
# • Un metodo stampa_saldo che stampi una stringa del tipo "Il saldo di 'intestatario' è: 'saldo' €".

class ContoCorrente:
    #costruttore
    def __init__(self, intestatario, saldo=0):
        self.intestatario=intestatario
        self.saldo=saldo
    
    def deposita(self):
        deposito =int(input("Quanto vuoi depositare? ")) 
        if deposito <=0:
            print("Messaggio di errore, Pippo")
            pass
        else:
            self.saldo= self.saldo+deposito
            return self.saldo

    def prelievo(self):
        prelievo =int(input("Quanto vuoi prelevare? "))
        if prelievo>self.saldo:
            print("Messaggio di errore, Pippo2")
            pass
        else:
            self.saldo= self.saldo-prelievo
            return self.saldo
    def stampa_saldo(self):
        print("Il saldo di ", self.intestatario, "è : " , self.saldo, " €")


scelta_menu=""
while scelta_menu != "end" :
    pass



#Esercizio 4 ():
# Crea una classe chiamata Garage. Questa classe dovrebbe avere:
# • Un attributo di istanza capienza (numero massimo di auto) passato al costruttore.
# • Un attributo di istanza auto_presenti (lista di stringhe con le targhe), inizialmente vuota.
# • Un metodo parcheggia che accetti una targa e aggiunga l'auto alla lista. Se il garage è pieno, stampa un messaggio di errore. Se la targa è già presente, avvisa che l'auto è già in garage.
# • Un metodo rimuovi che accetti una targa e rimuova l'auto corrispondente. Se la targa non è presente, stampa un messaggio di errore.
# • Un metodo posti_libri che restituisca il numero di posti ancora disponibili.
# • Un metodo statico formato_targa_valido che accetti una stringa e restituisca True se la targa rispetta il formato italiano (2 lettere, 3 numeri, 2 lettere – es. "AB123CD"), False altrimenti. Suggerimento: si può usare il metodo .isalpha() e .isdigit() sulle sottostringhe.
# • Il metodo parcheggia deve usare formato_targa_valido per rifiutare targhe non valide prima di aggiungerle.


#creo la classe Garage
class Garage:
    
    #assegno gli att. di istanza capienza e auto presenti
    def __init__(self, capienza, auto_presenti):
        self.capienza=capienza
        self.auto_presenti=auto_presenti
       
    #utilizzo il dunder method len per ottenere il n. di auto presenti
    def __len__(self):
        return len(self.auto_presenti)
    #creo il metodo d'istanza parcheggia, con parametro self e autopresenti
    def parcheggia(self, auto_presenti):
        #se le auto presenti == alla capienza, il parcheggio sarà pieno
        if auto_presenti == self.capienza:
            print("Il parcheggio è pieno ") 
        #se le auto presenti sono meno della capienza, c'è posto, e permetto il deposito
        elif auto_presenti < self.capienza:
            #aggiungo +1 alle auto presenti
            self.autopresenti+=1
            #rimuovo 1 dalla capienza totale
            self.capienza-=1
            print("Hai depositato la tua auto ")
    #creo il metodo d'istanza rimuovi, parametri self e auto presenti
    def rimuovi(self, auto_presenti):
        #se le auto presenti==0, non c'è un auto da rimuovere
        if auto_presenti == 0:
            print("Non ci sono auto da rimuovere")
        #se le auto presenti sono + o uguali alla capienza, permetto l'op. (qui dovrei mettere un len per la capienza?, il >= credo vada sostituito)            
        elif auto_presenti>= self.capienza:            
            self.autopresenti-=1
            self.capienza+=1
        print("Hai depositato la tua auto ")
    
    #rimuovo alla capienza le auto presenti  
    def posti_liberi(self):
        return self.capienza-self.auto_presenti
    
    def formato_targa_valido(self):
        pass
    
    
x =input("")
while x != "end":
    pass



# puoi provare autonomamente es pag 140- 142 128-9