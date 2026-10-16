# Esercizio: Gestionale di un’Officina di Elettrodomestici
# Concetti obbligatori: incapsulamento, ereditarietà, polimorfismo, uso di type() per controllare
# gli oggetti e metodi “variatici” (con parametri variabili).
# Stai progettando il software di base per un’officina che si occupa di riparare elettrodomestici
# (lavatrici, frigoriferi, forni, ecc.). Il programma dovrà modellare gli elettrodomestici, i
# ticket di riparazione e alcune operazioni dell’officina, usando la programmazione ad oggetti.
# 1. Classe base: Elettrodomestico
# Crea una classe base chiamata Elettrodomestico che rappresenti un elettrodomestico generico.
# Attributi (incapsulati, cioè privati):
# __marca (stringa)
# __modello (stringa)
# __anno_acquisto (intero)
# __guasto (stringa che descrive il problema principale)
# Metodi:
# Costruttore __init__(self, marca, modello, anno_acquisto, guasto)
# Getter e setter per tutti gli attributi, con eventuali controlli minimi (es. l’anno non può essere nel
# futuro).
# descrizione(self): restituisce una stringa con marca, modello, anno e guasto.
# stima_costo_base(self): restituisce un valore numerico generico (es. costo base di diagnosi).
# Regola 1 – Incapsulamento: tutti gli attributi devono essere privati (__attributo) e accessibili solo
# tramite getter/setter.

class Elettrodomestico:
    
    def __init__(self,marca:str,modello:str,anno_acquisto:int,guasto:str):
    
        self.__marca=marca
    
        self.__modello=modello
    
        self.__anno_acquisto=anno_acquisto
    
        self.__guasto=guasto

    def get_marca(self):
    
        return self.__marca

    def set_marca(self,marca):
    
        self.__marca=marca
    
    def get_modello(self):
    
        return self.__modello

    def set_modello(self,modello):
    
        self.__modello=modello
        
    
    def get_anno_acquisto(self):
    
        return self.__anno_acquisto

    def set_anno_acquisto(self,anno_acquisto):
    
        if anno_acquisto >2026:
    
            print("Errore: la data non può essere nel futuro")
    
        else:
    
            self.__anno_acquisto=anno_acquisto
        
    def get_guasto(self):
    
        return self.__guasto

    def set_guasto(self,guasto):
    
        self.__guasto=guasto  
    
    def descrizione(self):
    
        return (f"L'elettrodomestico della marca:{self.__marca}, il modello è: {self.__modello}, acquistato in data: {self.__anno_acquisto} ha il seguente guasto:{self.__guasto}")
        
    def stima_costo_base(self):
    
        return  150


class Lavatrice(Elettrodomestico):
    
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, capacita_kg:int,giri_centrifuga:int):
        
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__capacita_kg=capacita_kg

        self.__giri_centrifuga=giri_centrifuga

    def get_capacita_kg(self):
    
        return self.__capacita_kg

    def set_capacita_kg(self,capacita_kg):
    
        self.__capacita_kg=capacita_kg    
    
    
    def get_giri_centrifuga(self):
    
        return self.__giri_centrifuga

    def set_giri_centrifuga(self,giri_centrifuga):
    
        self.__giri_centrifuga=giri_centrifuga    
    
    
        
    def stima_costo_base(self):

        costo_base=100

        if self.__capacita_kg > 30:

            return costo_base+20

        else:

            return costo_base


# 2.Frigorifero
# Attributi aggiuntivi:
# litri (intero)
# ha_freezer (booleano)
# Override di stima_costo_base(self): il costo può cambiare se ha il freezer o se i litri superano una
# certa soglia.
class Frigorifero(Elettrodomestico):
    
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, litri:int,ha_freezer:bool):
        
        super().__init__(marca, modello, anno_acquisto, guasto)
        
        self.__litri=litri

        self.__ha_freezer=ha_freezer

    def get_litri(self):
    
        return self.__litri

    def set_litri(self,litri):
    
        self.__litri=litri    
    
    
    def get_ha_freezer(self):
    
        return self.__ha_freezer

    def set_ha_freezer(self,ha_freezer):
    
        self.__ha_freezer=ha_freezer    

        
    def stima_costo_base(self):

        costo_base=120

        if self.__ha_freezer and self.__litri>50:

            return costo_base+110


        elif self.__ha_freezer or  self.__litri > 50:

            return costo_base+70

        else:

            return costo_base


class Forno(Elettrodomestico):
    
    def __init__(self, marca:str, modello:str, anno_acquisto:int, guasto:str, tipo_alimentazione:str, ha_ventilato:bool):
        
        super().__init__(marca, modello, anno_acquisto, guasto)
        

        self.__tipo_alimentazione=tipo_alimentazione

        self.__ha_ventilato=ha_ventilato

    
    def get_tipo_alimentazione(self):
    
        return self.__tipo_alimentazione

    def set_tipo_alimentazione(self,tipo_alimentazione):
    
        self.__tipo_alimentazione=tipo_alimentazione    
    
    
    def get_ha_ventilato(self):
    
        return self.__ha_ventilato

    def set_ha_ventilato(self,ha_ventilato):
    
        self.__ha_ventilato=ha_ventilato    

        
        
    def stima_costo_base(self):

        costo_base=80

        if self.__tipo_alimentazione =="gas" and self.__ha_ventilato:

            return costo_base+150

        elif self.__tipo_alimentazione =="elettrico" and self.__ha_ventilato:

            return costo_base+120
        elif self.__tipo_alimentazione =="gas" and not self.__ha_ventilato :

            return costo_base+80
        elif self.__tipo_alimentazione =="elettrico" and not self.__ha_ventilato :
        
            return costo_base+60
        else:
            print("non hai inserito i parametri necessari")

# 3.Forno
# Attributi aggiuntivi:
# tipo_alimentazione (stringa: “elettrico”
# ,
# “gas”)

# ha_ventilato (booleano)
# Override di stima_costo_base(self): il costo può cambiare in base al tipo di alimentazione e alla
# presenza della funzione ventilata.
# Regola 2 – Ereditarietà: tutte le classi derivate devono usare Elettrodomestico come classe base ed
# ereditare i suoi attributi tramite super() nel costruttore.
# Regola 3 – Polimorfismo: tutte le sottoclassi devono fornire la propria versione di
# stima_costo_base(self), in modo che la chiamata a questo metodo su una lista mista di oggetti (Lavatrice,
# Frigorifero, Forno) produca risultati diversi a seconda del tipo.
class TicketRiparazione:
    def __init__(self,id_ticket:int,elettrodomestico:Elettrodomestico):
        self.__id_ticket=id_ticket
        self.__elettrodomestico=elettrodomestico
        stato=("aperto") # "in lavorazione", "chiuso")
        note=[]
        self.__stato=stato
        self.__note=note
        
    def get_stato(self):
    
        return self.__stato

    def set_stato(self,stato):
    
        self.__stato=stato

    def get_note(self):
    
        return self.__note

    def set_note(self,note):
    
        self.__note=note


    def aggiungi_nota(self,testo):
         self.__note.append(testo)
    
    def calcola_preventivo(self, *voci_extra):
        costo_base=self.__elettrodomestico.stima_costo_base()
        for v in voci_extra:
            costo_base+=v
        return costo_base
# 3. Classe TicketRiparazione
# Crea una classe TicketRiparazione che rappresenta un ticket aperto in officina.
# Attributi (incapsulati):
# __id_ticket (intero o stringa univoca)
# __elettrodomestico (un oggetto di tipo Elettrodomestico o sottoclasse)
# __stato (stringa: “aperto”, “in lavorazione”, “chiuso”)
# __note (lista di stringhe, inizialmente vuota)
# Metodi:
# Costruttore __init__(self, id_ticket, elettrodomestico)
# Getter e setter necessari (ad esempio per stato e note).
# aggiungi_nota(self, testo) per aggiungere una nota.
# calcola_preventivo(self, *voci_extra) → metodo variadico:
# usa elettrodomestico.stima_costo_base() come costo di partenza
# somma tutte le voci extra passate come parametri (*voci_extra)
# restituisce il totale.
# Nota: questo metodo deve funzionare con qualsiasi sottoclasse di Elettrodomestico
# (polimorfismo sul metodo stima_costo_base).

class Officina:
    def __init__(self,nome:str,tickets:TicketRiparazione):
        self.__nome=nome
        self.__tickets=tickets
        
    def aggiungi_ticket(self,ticket):
    def chiudi_ticket(self,id_ticket):
    def stampa_ticket_aperti(self):
    def totale_preventivi(self):
    
# 4. Classe Officina
# Crea una classe Officina che gestisce i ticket e gli elettrodomestici.
# Attributi:
# nome (stringa)
# tickets (lista di oggetti TicketRiparazione)
# Metodi:
# aggiungi_ticket(self, ticket)
# chiudi_ticket(self, id_ticket)
# stampa_ticket_aperti(self): mostra ID, tipo di elettrodomestico e stato.
# totale_preventivi(self): somma i preventivi di tutti i ticket.
# 5. Uso di type() e controllo degli oggetti
# All’interno della classe Officina (o in una funzione separata) implementa un
# metodo, ad esempio:
# statistiche_per_tipo(self)
# Questo metodo deve:
# Iterare su tutti i ticket.
# Usare type() (oppure isinstance()) per capire se l’elettrodomestico associato
# al ticket è una Lavatrice, un Frigorifero o un Forno.
# Contare quanti ticket ci sono per ciascuna sottoclasse.
# Stampare un piccolo report, per esempio:
# “Numero di lavatrici in riparazione: X”
# “Numero di frigoriferi in riparazione: Y”
# “Numero di forni in riparazione: Z”
# Requisito: il metodo deve utilizzare type() (o, come variante consigliata,
# isinstance()) per differenziare in base al tipo reale degli oggetti.