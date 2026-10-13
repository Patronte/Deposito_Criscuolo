#Creo la classe membro squadra

class MembroSquadra:
    #al costruttore do nome ed eta
    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta
    #creo la funzione descrivi per fare identikit
    def descrivi(self):
        print(f"Il giocatore {self.nome} è un Pippo ed ha: {self.eta}")    

#creo classe giocatore
class Giocatore(MembroSquadra):
    #costruttore eredita parametri del padre e aggiunge n_maglia
    def __init__(self, nome, eta,ruolo, n_maglia):
        #non saprei spiegare riga 17, ma se non utilizzo essa o il super, i parametri del padre non sono accessibili, eccomi data la risposta
        MembroSquadra.__init__(self, nome, eta) #se al posto di questo c'è differenza usando il super, la differenza non l'ho capita
        self.ruolo=ruolo
        self.n_maglia=n_maglia
    #funzione gioca partita per "deployare" un giocatore in campo
    def gioca_partita(self):
        print(f"Il giocatore {self.nome}, col numero maglia {self.n_maglia} scende in campo")
#classe allenatore sempre figlia di classe membrosquadra        
class Allenatore(MembroSquadra):
    #al costruttore sempre i valori del padre + i nuovi
    def __init__(self, nome, eta,anni_di_esperienza):
        MembroSquadra.__init__(self, nome, eta)
        self.anni_di_esperienza=anni_di_esperienza
    #funzione per far dare all'allenatore con x nome e x anni di esperienza, direttive ai giocatori
    def dirige_allenamento(self):
        print(f"L'allenatore {self.nome}, con {self.anni_di_esperienza} suggerisce tattiche alla sua squadra")

#nuova subclass assistente, della classe membrosquadra        
class Assistente(MembroSquadra):
    #costruttore eredita e aggiunge nuovi parametri o argomenti
    def __init__(self, nome, eta,specializzazione):
        MembroSquadra.__init__(self, nome, eta)
        self.specializzazione=specializzazione
    #funzione che stampa un messaggio in cui l'assistenze svolge un'azione
    def supporta_team(self):
    #aaamirko
        print(f"L'assistente {self.nome}, specializzato in  {self.specializzazione} scende in campo ad assistere il Pippo") #al posto di pippo volevo usare{Giocatore.nome}") o qualcosa per richiamare un giocatore specifico in base al nome
    
#creo la classe squadra
class Squadra:
    #al costruttore dico che è un contenitore di liste? o una lista?
    def __init__(self):
        
        self.squadra=[]
    
    def aggiungi_giocatore(self, giocatore): 
    
        self.squadra.append(giocatore)
        
#Creo un oggetto, della classe giocatore, con i propri args o paramtr        
G1= Giocatore("Mirko", 31, "Attacante" , 10)
G2= Giocatore("Marko", 21, "Difensore" , 5)
G3= Giocatore("Merko", 41, "Portiere" , 15)
G4= Giocatore("Murko", 26, "Centrocampista" , 20)
#Creo ogg Allenatore
Al1= Allenatore("Smerko",32,6)
Al2= Allenatore("Smirko",52,15)
#Creo ogg Assistente
As1= Assistente("Smorko",28,"Fisioterapista")
As2= Assistente("Smurko",48,"Primo Soccorso")

#eseguo la chiamata del primo ogg creato e della sua funzione per vedere se viene eseguita
G1.gioca_partita() #Eureka
Al1.dirige_allenamento() #Eureka
As1.supporta_team()#Eureka
