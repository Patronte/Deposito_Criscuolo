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
#   7. Riepilogo finale
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
# 7. RIEPILOGO FINALE
# =============================================================================
#
#   CLASSE   -> definizione/astrazione (il "progetto"), scritta una volta sola
#   OGGETTO  -> istanza reale creata dalla classe, con proprietà uniche
#   __init__ -> costruttore: inizializza gli attributi dell'oggetto
#   self     -> l'oggetto corrente (serve in tutti i metodi tranne gli statici)
#   cls      -> la classe corrente (metodi di classe)
#
#   Attributo di classe   -> condiviso da tutti (es. numero_di_ruote)
#   Attributo di istanza  -> proprio di ogni oggetto (es. self.marca)
#
#   Metodo di istanza -> self      | lavora sull'oggetto
#   Metodo di classe  -> cls       | @classmethod
#   Metodo statico    -> nessuno   | @staticmethod
#
# (Ripasso: PDF pag. 117)