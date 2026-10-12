# Oggetto è l'istanza reale della classe che può utilizzare i metodi e definire in maniera unica le variabili e usare i metodi
# Le CLASSI
# Cos'è una classe? una classe è una definizione di un oggetto e del tipo dell'oggetto, il nome è uguale al x del costruttore e 
# può avere variabili(var di class), funzioni(metodi) e funzioni speciali (es costruttore)
# variabili e metodi dobbiamo darli noi, mentre
# i metodi speciali sono forniti da python e  sono metodi impliciti alle classi  
 #L'OGGETTO è la cosa reale che creo dalla classe
# il nome della classe serve a 1, nominare la classe, 2 è il nome del costruttore, ed il tipo di oggetti che crea 

class Mirko: 
    #Variabile di classe
    nome = " "
    
    def saluta(self):
        return("ciao mirko")
    
        
    
#Inizializzazione dell'oggetto tramite costruttore    
Ogg_1 = Mirko()
Ogg_2 = Mirko()

Ogg_2.nome = "Martina"
print(Ogg_1.nome)   
print(Ogg_2.nome)
print(Ogg_1.saluta())

# la classe è la definizione di un tipo di dato non basilare il quale nome 
# il nome della classe è uguale al tipo di dato e al nome del costruttore
# l'oggetto è la 
# ogni classe può essere definita una volta sola es se colleghiamo 10 file, possiamo avere una sola classe "Mirko" ma infiniti oggetti della classe Mirko

# La classe è l'astrazione del mondo reale 
# Un oggetto è un'istanza di una classe, cioè una copia univoca della classe che ha le sue proprietà uniche
# le classi possono contenere metodi attributi e metodi speciali
# Le classi possono stare dentro altre classi 

# I metodi sono funzioni associate ad una classe

# Una classe puo avere variabili, i suoi metodi normali, ed i metodi speciali, uno di questi è il costruttore.
# Fuori dalla carte il costruttore porta lo stesso nome della classe, dentro la classe invece si chiama init( che sta per inizializzazione)
# Il costruttore è il metodo che
# il costruttore può volere una variabile 
# ogni metodo della classe tranne quelli statici, vuole il self


class persona:
    #Metodo costruttore
        def __init__(self, nome, eta):
            self.nome = nome
            self.eta = eta             
        #Variabile di classe
        
        
        
#Dichiaro la classe
class Automobile:
    #attributo di classe
    numero_di_ruote=4
    #metodo costruttore
    def __init__(self, marca,modello):
        #attributo di istanza
        self.marca=marca
        #attributo di istanza
        self.modello=modello
    #metodo di istanza
    def stampa_info(self):
        print("Lautomobile è una ", self.marca, self.modello)
        


#Crea un oggetto di automobile (gli ogg iniziano con la lettera Maiuscola)
Auto1= Automobile("Fiat", "500")
Auto2= Automobile("BMW", "X3")

#stampa "L'automobile, è una fiat 500"
Auto1.stampa_info()
Auto2.stampa_info()

#I metodi speciali delle classi esistono a prescindere da noi, che possiamo solo modificarli, non possiamo toglierli, o mod o lasci vuoti

    
#    def __init__(self):se non c'è il costruttore c'è questo
#         pass

#I metodi delle funzioni possono essere solo 3:
# - i metodi di istanza vogliono il self lavorano sugli oggetti
# - i metodi di classe: utilizzabili dalla classe, non ci va il self ma un cls (che sta per classe)  pro: no bisogno oggetto e lavorano dentro la classe contro: una volta modificata la classe tutti i futuri oggetti verranno modificati
# - i metodi statici: non lavorano con nessuno sono definiti con il decoratore  @staticmethod

class Calcolatrice:
    @staticmethod
    def somma(a,b):
        return a+b

#Uso del metodo statico senza creare un'istanza 
risulato=Calcolatrice.somma(5,3)

print(risulato)
#Output: 8
class Esempio:
    pass


#ESEMPIO Metodo decorato #METODO DELLA classe 
class Contatore:
    numero_istanze = 0 #Attributo di classe
    
    def __init__(self):
        Contatore.numero_istanze+=1
        #ogni volta che costruisco un oggetto aumenta contatore di uno
    @classmethod #decoratore perché ha la chiocciola
    def mostra_numero_istanze(cls):
        print("Sono state create" ,{cls.numero_istanze},"istanze. ")
    
c1=Contatore()
c2=Contatore()

Contatore.mostra_numero_istanze()

#pdf 117 recap 

#DUNDER METHOD--> METODI SPECIALI
# i più famosi sono :
# __init__ --> costruttore --> costruisce gli oggetti
# __str__ --> to string --> ti permette di stampare gli oggetti direttamente nel print
# __len__ --> la lunghezza --> riporta la lunghezza di un oggetto o una lista
# sono speciali perché esistono anche se non li usiamo nella classe
#VEDIAMO STR
class Studente:
    def __init__(self, nome, eta):
        self.nome=nome
        self.eta=eta
        
    def __str__(self):
        return "Studente: " + self.nome + ", età: " + str(self.eta)
    
studente1=Studente("Luca", 20)

print(studente1)

#VEDIAMO LEN
#ci da la lunghezza di ciò a cui lo attribuiamo
# serve a dire al sistema come deve stampare quando richiamiamo LEN

class Squadra:
    def __init__(self, nome, giocatori):
        self.nome = nome
        self.giocatori=giocatori

    def __len__(self):
        return len(self.giocatori)

squadra1=Squadra("Tigri", ["Luca", "Marco","Anna"])

print(len(squadra1))


#CALL PERMETTE DI USARE Un intero oggetto come se fosse una funzione
class Moltiplicatore:
    def __init__(self,numero):
        self.numero=numero
    def __call__ (self, valore):
        return valore * self.numero

doppio=Moltiplicatore(2)

print(doppio(10))