"""
================================================================================
APPUNTI: LE TRE REGOLE DELL'OOP (Programmazione Orientata agli Oggetti)
================================================================================

La programmazione orientata agli oggetti si basa su tre concetti fondamentali,
più uno alla base chiamato L'ASTRAZIONE.

1. INCAPSULAMENTO:
   Permette di nascondere i dettagli interni di una classe, esponendo solo le
   interfacce necessarie per interagire con essa.
   -> Scopo: Mantenere il codice modulare e sicuro.

2. EREDITARITÀ:
   Consente di creare nuove classi a partire da classi esistenti, riutilizzando
   e specializzando il comportamento definito nelle classi base.
   -> Scopo: Favorire la riusabilità e l'organizzazione gerarchica.

3. POLIMORFISMO:
   Permette di trattare oggetti di classi differenti attraverso una comune interfaccia.
   -> Scopo: Facilitare l'estensione e la gestione flessibile e dinamica.
================================================================================
"""

# --- ESEMPIO PRATICO IN PYTHON ---
'''
# 1. INCAPSULAMENTO (Uso di attributi privati con il doppio underscore __ )
class ContoBancario:
    def __init__(self, titolare, saldo_iniziale):
        self.titolare = titolare
        self.__saldo = saldo_iniziale  # Attributo privato (nascosto all'esterno)

    # Interfaccia pubblica per interagire in sicurezza con l'attributo nascosto
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo

    def visualizza_saldo(self):
        return f"Saldo di {self.titolare}: {self.__saldo}€"


# 2. EREDITARITÀ (La classe Cane eredita dalla classe base Animale)
class Animale:
    def __init__(self, nome):
        self.nome = nome

    def fai_suono(self):
        pass  # Verrà definito nelle sottoclassi

class Cane(Animale):  # Cane eredita da Animale
    def fai_suono(self):
        return "Bau Bau!"


# 3. POLIMORFISMO (Classi diverse hanno lo stesso metodo, usato allo stesso modo)
class Gatto(Animale):
    def fai_suono(self):
        return "Miao!"

# Una singola funzione può gestire oggetti diversi (Cane o Gatto) grazie al polimorfismo
def ascolta_animale(animale_generico):
    print(f"{animale_generico.nome} dice: {animale_generico.fai_suono()}")


# --- ESECUZIONE DEL CODICE ---
if __name__ == "__main__":
    print("--- Test Incapsulamento ---")
    conto = ContoBancario("Mario", 1000)
    conto.deposita(500)
    print(conto.visualizza_saldo())
    # print(conto.__saldo) # Questo genererebbe un errore perché il saldo è protetto!

    print("\n--- Test Ereditarietà e Polimorfismo ---")
    fido = Cane("Fido")
    buffy = Gatto("Buffy")

    ascolta_animale(fido)   # Chiama il metodo di Cane
    ascolta_animale(buffy)  # Chiama il metodo di Gatto
#SOPRA APPUNTI IA DA SLIDE sotto appunti miei
'''
#COME CI SPIEGA MIRKO
# senza le 3 regole fondamentali non abbiamo più l'OOP
# ognuna di queste 3 regole ha un significato, fa una cosa, 
# l'incapsulamento è la capacità di nascondere degli elementi/o nel codice o dal codice
'''
if True:
    x = 10

print(x)
#se lo printo esce 10

x=20
if True:
    x=10

print(x)
'''

#ma se lo creo dichiarando prima una variabile fuori e poi una dentro

# L'ereditarietà è la capacità di generare un elemento figlio  partendo da un elemento padre e generare una gerarchia, ci permette di ereditare tutto ciò che è visibile al figlio
# L'ereditarietà fa solo 3 cose:
# - un metodo: super(), 
# - una logica: ereditarietà multipla, esempio: io ho padre1 che fa figlio, posso avere anche padre 2-3-4 la classe padre è super classe, la figlio è sub classe
# - una strategia :sovrascrittura dei metodi (posso riscrivere i metodi del figlio)





# POLIMORFISMO è la capacità di un elemento di cambiare forma e o  comportamento senza cambiare ciò che rappresenta per il sistema 
# Queste 4 regole (astrazione comprese) funzionano SEMPRE TUTTE E 4 CONTEMPORANEAMENTE

#Classe base
class Animale:
    def __init__(self, nome):
        self.nome=nome
    def parla(self):
        print(self.nome+" fa suono generico. ")
#Classe derivata(eredita da Animale)
class Cane(Animale):
    
    def parla(self):
        print(self.nome + " abbaia! ")

animale_generico=Animale("AnimaleGenerico")

cane=Cane("Fido")

animale_generico.parla() #output: AnimaleGenerico fa suono generico.
cane.parla() #output: Fido abbaia



# IL SUPER SERVE A RICHIAMARE IL METODO DEL PADRE ANCHE NEL FIGLIO 

class Veicolo:
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello

    def mostra_informazioni(self):
        print(f"Veicolo marca {self.marca}, modello {self.modello}")

class DotazioniSpeciali:
    def __init__(self, dotazioni):
        self.dotazioni = dotazioni

    def mostra_dotazioni(self):
        print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")
        
# Quando inseriamo più genitori nel figlio, il primo che insieriamo sarà più importante
# es:
class AutomobileSportiva(Veicolo, DotazioniSpeciali ):
    #il Veicolo padre sarà + importante
#riscriviamo il costruttore perché vogliamo aggiungere un pezzo
    def __init__(self, marca, modello, dotazioni, cavalli):
#marca e modello sono del padre VEICOLO, dotazione è di dotazioneSpeciale, CAVALLI è nuovo
        Veicolo.__init__(self, marca,modello)
    #richiamo il costruttore del padre (VEICOLO) perché abbiamo il metodo init in entrambi i padri 
        DotazioniSpeciali.__init__(self,dotazioni)
        self.cavalli=cavalli
        
#funzione sovrascritta dal padre(presente nel padre)
def mostra_informazioni(self):
    super().mostra_informazioni()
    #Chiamiamo il metodo del padre (appartiene solo ad uno dei due quindi posso usare super())
    print(f"Potenza: {self.cavalli} CV ")
    self.mostra_dotazioni()
    #possiamo chiamare metodi di entrambe le superclassi 
    

auto_sportiva= AutomobileSportiva("Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720)

auto_sportiva.mostra_informazioni()

#l'ereditarietà è l'unica regola fondamentale più in mano al programmatore al 90% , un 10% nascosto in cui la macchina lo fa da sola
# L'incapsulamento è 50%-50%  
# Polimorfismo 90%-10% 10% programmatore