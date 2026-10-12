# =============================================================================
#  GLI OGGETTI E LE CLASSI IN PYTHON
#  (appunti teorici + pratici)
# =============================================================================
#
#  INDICE
#   1. Teoria: classe e oggetto
#   2. Prima classe: variabili di classe e metodi
#   3. Il costruttore __init__ e gli attributi di istanza
#   4. Esempio completo: Automobile
#   5. I tre tipi di metodi (istanza, classe, statico)
#   6. Esempio di metodo di classe: Contatore
#   7. I metodi speciali (dunder): __str__, __len__, __call__
#   8. Riepilogo finale
#
# =============================================================================


# =============================================================================
# 1. TEORIA: CLASSE E OGGETTO
# =============================================================================
#
# CLASSE
#   - È la DEFINIZIONE di un tipo di dato non basilare (creato da noi).
#   - È l'astrazione del mondo reale: descrive com'è fatto un "tipo" di cosa.
#   - Può contenere:
#       * variabili (attributi / variabili di classe)
#       * metodi = funzioni associate alla classe
#       * metodi speciali (es. il costruttore __init__)
#   - Variabili e metodi normali li scriviamo noi;
#     i metodi speciali sono forniti da Python (sono impliciti in ogni classe).
#   - Una classe si definisce UNA volta sola (anche se importata da 10 file),
#     ma da essa si possono creare infiniti oggetti.
#   - Le classi possono stare anche dentro altre classi.
#
# OGGETTO
#   - È la cosa REALE creata a partire dalla classe (si dice "istanza").
#   - È una copia univoca della classe, con le sue proprietà uniche.
#   - Può usare i metodi della classe e avere variabili tutte sue.
#
# IL NOME DELLA CLASSE serve a:
#   1. nominare la classe
#   2. chiamare il costruttore (Mirko() crea un oggetto)
#   3. indicare il tipo degli oggetti che crea
#
# CONVENZIONE: i nomi delle classi iniziano con la lettera MAIUSCOLA (Persona,
# Automobile), mentre gli oggetti di solito si scrivono in minuscolo
# (auto1, ogg_1).


# =============================================================================
# 2. PRIMA CLASSE: VARIABILI DI CLASSE E METODI
# =============================================================================

class Mirko:
    # Variabile di classe (condivisa da tutti gli oggetti, finché non la si
    # ridefinisce su un singolo oggetto)
    nome = " "

    # Metodo di istanza: ogni metodo (tranne quelli statici) vuole il self
    def saluta(self):
        return "ciao mirko"


# Creazione degli oggetti: si chiama il costruttore col nome della classe
ogg_1 = Mirko()
ogg_2 = Mirko()

# Modifico la variabile SOLO sull'oggetto 2
# (ogg_1 continua a vedere il valore della classe)
ogg_2.nome = "Martina"

print(ogg_1.nome)        # " "
print(ogg_2.nome)        # Martina
print(ogg_1.saluta())    # ciao mirko


# =============================================================================
# 3. IL COSTRUTTORE __init__ E GLI ATTRIBUTI DI ISTANZA
# =============================================================================
#
# - Il costruttore è il metodo che CREA e INIZIALIZZA l'oggetto.
# - Fuori dalla classe lo "chiamiamo" con il nome della classe: Persona(...)
#   Dentro la classe si definisce con il nome __init__ (initialization).
# - Può ricevere dei parametri (oltre a self).
# - self = l'oggetto che si sta creando/usando.
# - Se non lo scriviamo, Python ne usa uno vuoto:
#       def __init__(self):
#           pass
#
# I metodi speciali esistono a prescindere da noi: possiamo modificarli o
# lasciarli vuoti, ma non toglierli.

class Persona:
    # Metodo costruttore
    def __init__(self, nome, eta):
        self.nome = nome   # attributo di istanza
        self.eta = eta     # attributo di istanza


# =============================================================================
# 4. ESEMPIO COMPLETO: AUTOMOBILE
# =============================================================================

class Automobile:
    # Attributo di classe (uguale per tutte le automobili)
    numero_di_ruote = 4

    # Metodo costruttore
    def __init__(self, marca, modello):
        # Attributi di istanza (diversi per ogni oggetto)
        self.marca = marca
        self.modello = modello

    # Metodo di istanza
    def stampa_info(self):
        print("L'automobile è una", self.marca, self.modello)


# Creo gli oggetti
auto1 = Automobile("Fiat", "500")
auto2 = Automobile("BMW", "X3")

auto1.stampa_info()   # L'automobile è una Fiat 500
auto2.stampa_info()   # L'automobile è una BMW X3


# =============================================================================
# 5. I TRE TIPI DI METODI
# =============================================================================
#
# 1) METODI DI ISTANZA
#    - vogliono il self
#    - lavorano sul singolo oggetto
#
# 2) METODI DI CLASSE  (decoratore @classmethod)
#    - non vogliono il self ma il cls (= la classe)
#    - PRO: si usano senza bisogno di un oggetto e lavorano dentro la classe
#    - CONTRO: se modificano la classe, cambiano per tutti i futuri oggetti
#
# 3) METODI STATICI  (decoratore @staticmethod)
#    - non vogliono né self né cls
#    - non lavorano con nessun oggetto né con la classe: sono semplici
#      funzioni "raggruppate" nella classe

# --- Esempio di metodo statico ---
class Calcolatrice:
    @staticmethod
    def somma(a, b):
        return a + b


# Uso senza creare un'istanza
risultato = Calcolatrice.somma(5, 3)
print(risultato)   # 8


# =============================================================================
# 6. ESEMPIO DI METODO DI CLASSE: CONTATORE
# =============================================================================

class Contatore:
    numero_istanze = 0   # Attributo di classe

    def __init__(self):
        # Ogni volta che costruisco un oggetto, il contatore aumenta di uno
        Contatore.numero_istanze += 1

    @classmethod   # decoratore (si riconosce dalla chiocciola)
    def mostra_numero_istanze(cls):
        print("Sono state create", cls.numero_istanze, "istanze.")


c1 = Contatore()
c2 = Contatore()

Contatore.mostra_numero_istanze()   # Sono state create 2 istanze.


# =============================================================================
# 7. I METODI SPECIALI (DUNDER METHODS)
# =============================================================================
#
# "Dunder" = "double underscore": sono i metodi con il nome tra doppi
# underscore (__nome__). Sono i METODI SPECIALI di cui parlavamo sopra.
#
# Python li richiama AUTOMATICAMENTE quando usiamo certe funzioni o sintassi
# (print, len, le parentesi tonde...). Noi li scriviamo per dire al sistema
# COME deve comportarsi il nostro oggetto in quei casi.
#
# I più famosi:
#   __init__  -> costruttore: costruisce (inizializza) gli oggetti
#   __str__   -> "to string": decide cosa viene stampato con print(oggetto)
#   __len__   -> decide cosa restituisce len(oggetto)
#   __call__  -> permette di usare l'oggetto come se fosse una funzione
#
# Nota: __init__ e __str__ esistono già di default (ereditati da Python);
# noi li ridefiniamo per personalizzarli. Altri, come __len__ e __call__,
# funzionano solo se li scriviamo noi.


# --- __str__: come si stampa l'oggetto ---------------------------------------
# Senza __str__, print(oggetto) mostrerebbe qualcosa tipo
# <__main__.Studente object at 0x...>

class Studente:
    def __init__(self, nome, eta):
        self.nome = nome
        self.eta = eta

    def __str__(self):
        # Deve RESTITUIRE una stringa (str(...) per convertire l'età)
        return "Studente: " + self.nome + ", età: " + str(self.eta)


studente1 = Studente("Luca", 20)
print(studente1)   # Studente: Luca, età: 20


# --- __len__: cosa restituisce len(oggetto) ----------------------------------
# Serve a dire al sistema come comportarsi quando chiamiamo len() sull'oggetto.
# Qui scegliamo noi cosa contare: il numero di giocatori.

class Squadra:
    def __init__(self, nome, giocatori):
        self.nome = nome
        self.giocatori = giocatori

    def __len__(self):
        return len(self.giocatori)


squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])
print(len(squadra1))   # 3


# --- __call__: l'oggetto usato come una funzione -----------------------------
# Permette di "chiamare" l'intero oggetto con le parentesi: oggetto(valore)

class Moltiplicatore:
    def __init__(self, numero):
        self.numero = numero

    def __call__(self, valore):
        return valore * self.numero


doppio = Moltiplicatore(2)
print(doppio(10))   # 20


# =============================================================================
# 8. RIEPILOGO FINALE
# =============================================================================
#
#   CLASSE   -> definizione/astrazione (il "progetto"), scritta una volta sola
#   OGGETTO  -> istanza reale creata dalla classe, con proprietà uniche
#   __init__ -> costruttore: inizializza gli attributi dell'oggetto
#   self     -> l'oggetto corrente (serve in tutti i metodi tranne gli statici)
#   cls      -> la classe corrente (metodi di classe)
#
#   __str__  -> cosa mostra print(oggetto)
#   __len__  -> cosa restituisce len(oggetto)
#   __call__ -> permette di usare oggetto(...) come una funzione
#
#   Attributo di classe   -> condiviso da tutti (es. numero_di_ruote)
#   Attributo di istanza  -> proprio di ogni oggetto (es. self.marca)
#
#   Metodo di istanza -> self      | lavora sull'oggetto
#   Metodo di classe  -> cls       | @classmethod
#   Metodo statico    -> nessuno   | @staticmethod
#
# (Ripasso: PDF pag. 117)