# # 📘 Python: Classi e oggetti (appunti riordinati)

# ---

# ## 1. Classe e oggetto

# **Concetto:**

# | | Cos'è |
# |---|---|
# | **Classe** | La **definizione** di un tipo di oggetto: dice quali dati e quali operazioni avrà. È un tipo di dato *non basilare*, creato da noi. |
# | **Oggetto** | L'**istanza reale** creata a partire dalla classe, con i suoi valori propri. |

# Una classe può contenere:
# - **variabili** (attributi)
# - **metodi**, cioè funzioni associate alla classe
# - **metodi speciali**, come il costruttore
# Il **nome della classe** ha tre funzioni: dà il nome alla classe, è il nome del costruttore e indica il tipo degli oggetti che crea. Gli appunti la definiscono anche "l'astrazione del mondo reale", collegandola all'OOP della prima lezione.

# > **⚠️ Precisazioni:**
# > 1. Nelle lezioni precedenti si diceva che i tipi non basilari sono "gli oggetti". Qui il concetto si precisa: a essere creata da noi è la **classe**, e gli oggetti sono le sue istanze.
# > 2. Gli appunti usano "variabili di classe" e "attributi" come sinonimi. Il termine usato dalla documentazione ufficiale è **attributi**.
# > 3. Una classe si può **annidare** dentro un'altra, come scrivi tu, ma negli appunti non c'è nessun esempio.
# > 4. Dire "una classe si definisce una sola volta" vale come regola pratica. Python tecnicamente permette di ridefinirla (vale l'ultima definizione), e due file diversi possono avere ciascuno una propria classe con lo stesso nome.

# ---

# ## 2. La prima classe: `Mirko`

# ```python
# class Mirko:
#     nome = " "                  # attributo di classe

#     def saluta(self):
#         return "ciao mirko"

# Ogg_1 = Mirko()                 # creo due oggetti
# Ogg_2 = Mirko()

# Ogg_2.nome = "Martina"
# print(Ogg_1.nome)
# print(Ogg_2.nome)
# print(Ogg_1.saluta())
# ```

# **Risultato:**

# | Istruzione | Output |
# |---|---|
# | `print(Ogg_1.nome)` | uno spazio (sembra una riga vuota) |
# | `print(Ogg_2.nome)` | `Martina` |
# | `print(Ogg_1.saluta())` | `ciao mirko` |

# > **⚠️ Punti da capire bene:**
# > - `Ogg_2.nome = "Martina"` **non modifica la classe**: crea un valore di `nome` valido solo per `Ogg_2`. `Ogg_1` continua a usare quello della classe (`" "`).
# > - Negli appunti era scritto `return("ciao mirko")`. Le parentesi sono inutili: `return` è una parola chiave, non una funzione.

# ---

# ## 3. Il costruttore `__init__` e `self`

# **Concetto:** il costruttore è il metodo che prepara un oggetto appena creato. Fuori dalla classe lo richiami con il **nome della classe** (`Mirko()`), dentro la classe si scrive come `__init__` (da *inizializzazione*). Può ricevere dei parametri.
# IL SELF è sempre obbligatorio come primo parametro e  RAPPRESENTA L'OGGETTO

# **Sintassi:**

# ```python
# class persona:
#     def __init__(self, nome, eta):
#         self.nome = nome
#         self.eta = eta
# ```

# - `self` è il primo parametro dei metodi e rappresenta **l'oggetto specifico** su cui lavori.
# - `self.nome = nome` salva il parametro come attributo dell'oggetto.
# - Quando chiami il metodo, `self` viene passato **in automatico**: tu non lo scrivi.

# ```python
# p = persona("Luca", 20)    # esempio mio, per mostrare l'uso
# print(p.nome)              # Luca
# ```

# > **⚠️ Correzioni:**
# > 1. Gli appunti dicono che "ogni metodo tranne quelli statici vuole il `self`". Non è esatto: i metodi **di classe** usano `cls`. Solo i metodi **di istanza** usano `self` (vedi sezione 5).
# > 2. `self` è un nome per convenzione, ma tutti i programmatori Python lo usano: meglio non cambiarlo.
# > 3. Per i nomi di classe la convenzione ufficiale (PEP 8) è la **maiuscola iniziale** (`Persona`), come `Mirko` e `Automobile`.
# >
# > **[⚠️ LACUNA: negli appunti `self` non è mai definito.]**
# >
# > **[⚠️ LACUNA: la classe `persona` non viene mai usata, e il commento "#Variabile di classe" rimane senza codice.]**

# ---

# ## 4. Attributi di classe e attributi di istanza

# ```python
# class Automobile:
#     numero_di_ruote = 4                  # attributo di classe

#     def __init__(self, marca, modello):
#         self.marca = marca               # attributo di istanza
#         self.modello = modello           # attributo di istanza

#     def stampa_info(self):               # metodo di istanza
#         print("Lautomobile è una ", self.marca, self.modello)

# Auto1 = Automobile("Fiat", "500")
# Auto2 = Automobile("BMW", "X3")

# Auto1.stampa_info()
# Auto2.stampa_info()
# ```

# **Risultato:**

# ```
# Lautomobile è una  Fiat 500
# Lautomobile è una  BMW X3
# ```

# | Tipo | Dove si scrive | Valore |
# |---|---|---|
# | **Di classe** | Nel corpo della classe, senza `self` | **Condiviso** da tutti gli oggetti |
# | **Di istanza** | Dentro `__init__`, con `self.` | **Proprio** di ogni oggetto |

# > **⚠️ Precisazioni sul codice:**
# > - Nella stringa manca l'apostrofo (`Lautomobile`, dovrebbe essere `L'automobile`). Il commento negli appunti riportava la frase corretta.
# > - Nell'output c'è un **doppio spazio** dopo "una": la stringa finisce già con uno spazio e `print` ne aggiunge un altro tra gli argomenti.
# > - Gli appunti dicono che gli oggetti "iniziano con la lettera maiuscola" (`Auto1`, `Ogg_1`). È in contrasto con la regola della lezione sulle variabili (nomi minuscoli) e con PEP 8, che per gli oggetti consiglia la minuscola (`auto1`).
# >
# > **[⚠️ LACUNA: la differenza tra attributi di classe e di istanza è spiegata solo nei commenti del codice, non a parole.]**

# ---

# ## 5. I tre tipi di metodi

# Gli appunti scrivono "i metodi delle funzioni possono essere solo 3". Intendevano i metodi **delle classi**.

# | Tipo | Primo parametro | Decoratore | Lavora su |
# |---|---|---|---|
# | **Di istanza** | `self` | nessuno | il singolo oggetto |
# | **Di classe** | `cls` | `@classmethod` | la classe |
# | **Statico** | nessuno | `@staticmethod` | né oggetto né classe |

# ### Metodo statico

# ```python
# class Calcolatrice:
#     @staticmethod
#     def somma(a, b):
#         return a + b

# risultato = Calcolatrice.somma(5, 3)   # senza creare un oggetto
# print(risultato)                       # 8
# ```

# Nel codice originale la variabile si chiamava `risulato` (una `t` mancante): funziona comunque, ma conviene correggerla.

# ### Metodo di classe

# ```python
# class Contatore:
#     numero_istanze = 0                       # attributo di classe

#     def __init__(self):
#         Contatore.numero_istanze += 1        # +1 a ogni nuovo oggetto

#     @classmethod
#     def mostra_numero_istanze(cls):
#         print("Sono state create", cls.numero_istanze, "istanze.")

# c1 = Contatore()
# c2 = Contatore()

# Contatore.mostra_numero_istanze()
# ```

# **Risultato:** `Sono state create 2 istanze.`

# > **⚠️ Errore da correggere:** nel codice originale c'era `{cls.numero_istanze}` con le **graffe**. In Python le graffe creano un *insieme* (`set`), quindi l'output sarebbe stato `Sono state create {2} istanze. `. Le graffe vanno tolte, come nella versione sopra.
# >
# > **⚠️ Correzione sui "contro" dei metodi di classe:** gli appunti dicono che modificando la classe "tutti i futuri oggetti verranno modificati". La modifica di un attributo di classe riguarda **anche gli oggetti già creati**, a meno che non abbiano un valore proprio per quell'attributo (come `Ogg_2.nome`).
# >
# > **[⚠️ LACUNA: i *decoratori* (le righe con `@`) sono nominati ma non spiegati: negli appunti c'è solo "decoratore perché ha la chiocciola".]**

# ---

# ## 6. I metodi speciali (dunder)
# le funzioni dunder method sono speciali perché esistono anche se non li scriviamo, a livello logico lo sono perché stiamo sovrascrivendo dei metodi generici di tutte le classi  
# **Concetto:** sono metodi con nome tra doppi underscore (`__nome__`), chiamati *dunder* da "double underscore". Python li richiama in automatico in certe situazioni.

# | Metodo | Si attiva quando... | Cosa fa |
# |---|---|---|
# | `__init__` | scrivi `Classe(...)` | inizializza l'oggetto |
# | `__str__` | usi `print(oggetto)` | decide come l'oggetto viene stampato |
# | `__len__` | usi `len(oggetto)` | restituisce la "lunghezza" dell'oggetto |
# | `__call__` | scrivi `oggetto(...)` | permette di usare l'oggetto come una funzione |

# ### `__str__`

# ```python
# class Studente:
#     def __init__(self, nome, eta):
#         self.nome = nome
#         self.eta = eta

#     def __str__(self):
#         return "Studente: " + self.nome + ", età: " + str(self.eta)

# studente1 = Studente("Luca", 20)
# print(studente1)
# ```

# **Risultato:** `Studente: Luca, età: 20`

# `str(self.eta)` serve perché `+` non può unire una stringa a un numero: l'età va prima convertita in testo. Senza `__str__`, `print(studente1)` mostrerebbe qualcosa come `<__main__.Studente object at 0x...>`.

# ### `__len__`

# ```python
# class Squadra:
#     def __init__(self, nome, giocatori):
#         self.nome = nome
#         self.giocatori = giocatori

#     def __len__(self):
#         return len(self.giocatori)

# squadra1 = Squadra("Tigri", ["Luca", "Marco", "Anna"])
# print(len(squadra1))        # 3
# ```

# > **⚠️ Correzione:** gli appunti dicono che `__len__` "serve a dire al sistema come deve stampare". In realtà dice come **calcolare la lunghezza** e deve restituire un numero intero. A stampare ci pensa `__str__`.

# ### `__call__`

# ```python
# class Moltiplicatore:
#     def __init__(self, numero):
#         self.numero = numero

#     def __call__(self, valore):
#         return valore * self.numero

# doppio = Moltiplicatore(2)
# print(doppio(10))           # 20
# ```

# `doppio` è un oggetto, ma `doppio(10)` lo usa come una funzione: Python esegue `doppio.__call__(10)`.

# > **⚠️ Correzione importante:** gli appunti dicono che i metodi speciali "esistono anche se non li usiamo nella classe" e che "possiamo solo modificarli, non toglierli". Questo vale per `__init__` e `__str__` (ereditati da `object`, la classe base di tutte le classi). **Non vale per `__len__` e `__call__`**: se non li scrivi, `len(oggetto)` e `oggetto(...)` danno `TypeError`.
# >
# > Se non scrivi un costruttore, c'è comunque un `__init__` di base che non fa nulla. Il tuo `def __init__(self): pass` è equivalente, ma non è obbligatorio scriverlo.

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. `{cls.numero_istanze}` con le graffe stampa un insieme (`{2}`): vanno tolte.
# 2. `__len__` e `__call__` **non esistono di default**: vanno scritti per essere usati.
# 3. `__len__` calcola la lunghezza, non stabilisce come stampare.
# 4. Il `self` non vale per tutti i metodi tranne gli statici: quelli di classe usano `cls`.
# 5. Modificare un attributo di classe cambia anche gli oggetti già creati (salvo valore proprio).
# 6. `Ogg_2.nome = "Martina"` crea un attributo solo di `Ogg_2`, non cambia la classe.
# 7. Nomi: classi con la maiuscola, oggetti con la minuscola (PEP 8), in contrasto con "gli oggetti iniziano con la maiuscola".
# 8. "Metodi delle funzioni" va letto come "metodi delle classi".
# 9. Typo nel codice: `Lautomobile` (apostrofo mancante), doppio spazio nell'output, `risulato`.
# 10. "Una sola classe per nome" è una regola pratica, non un obbligo.

# **Lacune da colmare:**
# - Frasi incomplete: *"Il costruttore è il metodo che..."*, *"l'oggetto è la..."*, *"il costruttore può volere una variabile"* (forse intendevi *parametri*)
# - Definizione di `self`
# - Spiegazione a parole di attributi di classe e di istanza
# - Decoratori (`@classmethod`, `@staticmethod`)
# - Classi annidate: nessun esempio
# - `class Esempio: pass`: serve solo come segnaposto, senza altro contesto
# - Il riferimento "pdf 117 recap": non è chiaro a quale materiale rimandi
# - Altri metodi speciali oltre ai quattro visti
# - Il legame con i principi dell'OOP: **ereditarietà, incapsulamento e polimorfismo** non compaiono in questo blocco, e restano ancora senza spiegazione le tre regole mancanti delle 7 citate nella prima lezione

# Quando vuoi, incolla il prossimo blocco.