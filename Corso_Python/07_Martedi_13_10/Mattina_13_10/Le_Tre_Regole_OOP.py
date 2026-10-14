# # 📘 Python: I pilastri dell'OOP (appunti riordinati)

# Il blocco contiene due parti: gli **appunti generati da IA dalle slide** (teoria ed esempio del conto bancario) e **i tuoi appunti dalla lezione di Mirko**. Le ho unite per concetto.

# ---

# ## 1. Panoramica

# **Concetto:** l'OOP si regge su tre regole fondamentali, più una alla base, l'**astrazione**.

# | Regola | Cosa fa (dalle slide) | Scopo |
# |---|---|---|
# | **Incapsulamento** | Nasconde i dettagli interni di una classe ed espone solo ciò che serve per usarla | Codice modulare e sicuro |
# | **Ereditarietà** | Crea nuove classi a partire da classi esistenti, riusandone e specializzandone il comportamento | Riuso e organizzazione gerarchica |
# | **Polimorfismo** | Permette di trattare oggetti di classi diverse attraverso un'interfaccia comune | Estensione e gestione flessibile |
# | **Astrazione** *(base)* | | |

# Secondo Mirko, senza le 3 regole fondamentali non c'è più OOP, e le 4 regole (astrazione compresa) funzionano **sempre tutte e 4 insieme**.

# > **⚠️ Precisazioni:**
# > - Come dice Mirko, in Python le 4 regole sono sempre "in gioco" almeno in parte: ogni classe eredita implicitamente dalla classe `object`. Il resto è un'affermazione didattica che non posso verificare nella documentazione.
# >
# > **[⚠️ LACUNA: nella prima lezione si parlava di "7 regole da imparare". Qui ne compaiono 4 (3 + astrazione). Le altre 3 non sono ancora comparse.]**
# >
# > **[⚠️ LACUNA: l'astrazione è citata come base, ma in questo blocco non ha una definizione.]**

# ---

# ## 2. Incapsulamento

# **Concetto:** nascondere dei dettagli interni, in modo che si possa interagire con l'oggetto solo tramite i metodi pubblici.

# ### Esempio dalle slide: `ContoBancario`

# ```python
# class ContoBancario:
#     def __init__(self, titolare, saldo_iniziale):
#         self.titolare = titolare
#         self.__saldo = saldo_iniziale      # attributo "privato"

#     def deposita(self, importo):
#         if importo > 0:
#             self.__saldo += importo

#     def visualizza_saldo(self):
#         return f"Saldo di {self.titolare}: {self.__saldo}€"

# conto = ContoBancario("Mario", 1000)
# conto.deposita(500)
# print(conto.visualizza_saldo())            # Saldo di Mario: 1500€
# ```

# L'attributo `__saldo` si modifica solo tramite `deposita()`, che controlla che l'importo sia positivo. Il doppio underscore `__` davanti al nome serve a nascondere l'attributo.

# ```python
# # print(conto.__saldo)   # AttributeError
# ```

# > **⚠️ Correzioni:**
# > 1. Le slide dicono prima "privato" e poi "**protetto**": sono due cose diverse. In Python non esiste un vero attributo privato.
# > 2. Con `__saldo` Python **cambia il nome** dell'attributo in `_ContoBancario__saldo` (*name mangling*). Da fuori `conto.__saldo` dà `AttributeError`, ma `conto._ContoBancario__saldo` funziona ancora. Il nascondere è quindi una protezione "di cortesia", non assoluta.
# > 3. Con **un solo** underscore (`_saldo`) si segnala per convenzione che l'attributo è interno, senza che Python lo blocchi.
# > 4. L'errore del `print` commentato è un `AttributeError`.
# >
# > **[⚠️ LACUNA: le f-string (`f"..."` con i valori tra `{}`) sono usate ma non spiegate: finora nei tuoi appunti si usavano `+` e `str()`.]**

# ### Gli esempi di Mirko sulla visibilità delle variabili

# ```python
# if True:
#     x = 10

# print(x)        # 10
# ```

# ```python
# x = 20
# if True:
#     x = 10

# print(x)        # 10 (non 20: l'assegnazione dentro l'if cambia la stessa x)
# ```

# In Python un `if` **non crea uno spazio separato** per le variabili: ciò che crei dentro è visibile anche fuori. Lo spazio separato (*scope*) lo creano ad esempio le **funzioni** e le classi.

# > **[⚠️ LACUNA: la frase "l'incapsulamento è la capacità di nascondere degli elementi o nel codice o dal codice"

# >
# > **[⚠️ LACUNA: non è chiaro come gli esempi con `if` si colleghino all'incapsulamento, perché in Python mostrano che la variabile *non* viene nascosta. La frase "ma se lo creo dichiarando prima una variabile fuori e poi una dentro" resta incompleta. Chiedi a Mirko cosa voleva dimostrare.]**
# >
# > **[⚠️ LACUNA: lo *scope* è già emerso come lacuna nella lezione sulle funzioni e non è ancora spiegato.]**

# ---

# ## 3. Ereditarietà

# **Concetto:** creare un elemento **figlio** a partire da un elemento **padre**, formando una gerarchia. Il figlio eredita ciò che il padre rende visibile.

# | Termine negli appunti | Altri nomi |
# |---|---|
# | Classe padre / **super classe** | classe base |
# | Classe figlio / **sub classe** | classe derivata |

# **Sintassi:** il padre si scrive tra parentesi dopo il nome del figlio.

# ```python
# class Figlio(Padre):
#     ...
# ```

# ### Esempio base: `Animale` e `Cane`

# ```python
# class Animale:
#     def __init__(self, nome):
#         self.nome = nome

#     def parla(self):
#         print(self.nome + " fa suono generico. ")

# class Cane(Animale):                 # Cane eredita da Animale
#     def parla(self):
#         print(self.nome + " abbaia! ")

# animale_generico = Animale("AnimaleGenerico")
# cane = Cane("Fido")

# animale_generico.parla()             # AnimaleGenerico fa suono generico.
# cane.parla()                         # Fido abbaia!
# ```

# `Cane` non ha un proprio `__init__`, quindi usa quello di `Animale`: per questo `Cane("Fido")` funziona. Il metodo `parla()` è invece **riscritto** nel figlio.

# > **⚠️ Nota:** nei commenti l'output è `Fido abbaia` senza il punto esclamativo, mentre il codice stampa `Fido abbaia! `.
# >
# > **⚠️ Precisazione:** "ereditare tutto ciò che è visibile" ha un effetto concreto: un attributo con il doppio underscore (come `__saldo`) non è accessibile al figlio con il suo nome, per il *name mangling* visto sopra.

# ### Le 3 cose dell'ereditarietà (secondo Mirko)

# | Elemento | Tipo | Cosa fa |
# |---|---|---|
# | `super()` | metodo | Richiama il metodo del padre dentro il figlio |
# | **Ereditarietà multipla** | logica | Un figlio può avere più padri (padre1, padre2...) |
# | **Sovrascrittura** (*overriding*) | strategia | Il figlio riscrive un metodo ricevuto dal padre |

# > **⚠️ Correzioni:**
# > 1. `super()` è una **funzione integrata**, non un metodo (come `len`, vista nella lezione sulle liste).
# > 2. Gli appunti dicono "posso riscrivere i metodi del figlio". Più precisamente il figlio riscrive i metodi **ereditati dal padre**.
# > 3. "L'ereditarietà fa solo 3 cose" è lo schema di Mirko. Manca nell'elenco il meccanismo base `class Figlio(Padre)`.

# ### Esempio con più padri: `AutomobileSportiva`

# **Il codice come l'hai incollato:**

# ```python
# class AutomobileSportiva(Veicolo, DotazioniSpeciali):
#     def __init__(self, marca, modello, dotazioni, cavalli):
#         Veicolo.__init__(self, marca, modello)
#         DotazioniSpeciali.__init__(self, dotazioni)
#         self.cavalli = cavalli

# def mostra_informazioni(self):          # ← a margine sinistro, fuori dalla classe
#     super().mostra_informazioni()
#     ...
# ```

# > **⚠️ Errore da correggere:** nel testo incollato `def mostra_informazioni(self):` è **fuori dalla classe**. Diventa una funzione normale che nessuno chiama, quindi non sovrascrive niente. `auto_sportiva.mostra_informazioni()` userebbe il metodo di `Veicolo` e stamperebbe solo la prima riga. Se la funzione venisse chiamata, `super()` darebbe `RuntimeError`, perché fuori da una classe non sa a quale padre riferirsi. Controlla in VS Code: potrebbe essere solo un problema di copia-incolla.

# **Versione corretta:**

# ```python
# class Veicolo:
#     def __init__(self, marca, modello):
#         self.marca = marca
#         self.modello = modello

#     def mostra_informazioni(self):
#         print(f"Veicolo marca {self.marca}, modello {self.modello}")

# class DotazioniSpeciali:
#     def __init__(self, dotazioni):
#         self.dotazioni = dotazioni

#     def mostra_dotazioni(self):
#         print(f"Dotazioni speciali: {', '.join(self.dotazioni)}")

# class AutomobileSportiva(Veicolo, DotazioniSpeciali):
#     def __init__(self, marca, modello, dotazioni, cavalli):
#         Veicolo.__init__(self, marca, modello)
#         DotazioniSpeciali.__init__(self, dotazioni)
#         self.cavalli = cavalli

#     def mostra_informazioni(self):        # indentato DENTRO la classe
#         super().mostra_informazioni()
#         print(f"Potenza: {self.cavalli} CV")
#         self.mostra_dotazioni()

# auto_sportiva = AutomobileSportiva(
#     "Ferrari", "F8", ["ABS", "Controllo trazione", "Airbag laterali"], 720
# )
# auto_sportiva.mostra_informazioni()
# ```

# **Risultato:**

# ```
# Veicolo marca Ferrari, modello F8
# Potenza: 720 CV
# Dotazioni speciali: ABS, Controllo trazione, Airbag laterali
# ```

# **Cosa spiegano i commenti di Mirko:**
# - **Ordine dei padri:** il primo padre elencato è il più importante. Python cerca metodi e attributi da sinistra a destra: questo ordine si chiama **MRO** (*Method Resolution Order*) e si vede con `AutomobileSportiva.__mro__`.
# - **Costruttori richiamati a mano:** entrambi i padri hanno un `__init__`. Con `super().__init__()` partirebbe solo quello di `Veicolo` (il primo), quindi li richiami uno per uno con `NomePadre.__init__(self, ...)`.
# - **`super()` per `mostra_informazioni`:** funziona perché il metodo c'è solo in `Veicolo`.

# > **⚠️ Precisazione:** `super()` non dipende dal fatto che il metodo sia in un solo padre: segue l'MRO e prende il **primo** padre che ha quel metodo. Se lo avessero entrambi, userebbe comunque quello di `Veicolo`.
# >
# > **[⚠️ LACUNA: MRO non è nominato negli appunti.]**
# >
# > **[⚠️ LACUNA: `', '.join(...)` è usato ma non spiegato (è un metodo delle stringhe che unisce gli elementi di una lista con un separatore).]**

# ---

# ## 4. Polimorfismo

# **Concetto:**
# - *Slide:* trattare oggetti di classi diverse attraverso un'interfaccia comune.
# - *Mirko:* la capacità di un elemento di cambiare forma e/o comportamento a un elemento senza cambiare ciò che rappresenta per il sistema.

# ### Esempio dalle slide: `Cane` e `Gatto`

# ```python
# class Animale:
#     def __init__(self, nome):
#         self.nome = nome

#     def fai_suono(self):
#         pass                         # segnaposto: lo definiscono le sottoclassi

# class Cane(Animale):
#     def fai_suono(self):
#         return "Bau Bau!"

# class Gatto(Animale):
#     def fai_suono(self):
#         return "Miao!"

# def ascolta_animale(animale_generico):
#     print(f"{animale_generico.nome} dice: {animale_generico.fai_suono()}")

# fido = Cane("Fido")
# buffy = Gatto("Buffy")

# ascolta_animale(fido)                # Fido dice: Bau Bau!
# ascolta_animale(buffy)               # Buffy dice: Miao!
# ```

# La funzione `ascolta_animale` lavora con qualunque animale: chiama `fai_suono()` e ogni oggetto risponde a modo suo. Il `pass` è il segnaposto visto nella lezione sui cicli.

# > **⚠️ Precisazione:** in Python il polimorfismo **non richiede** una classe padre comune: basta che l'oggetto abbia il metodo richiesto (*duck typing*). Qui l'ereditarietà è solo comoda per condividere `nome`.
# >
# > **⚠️ Nota sul codice:** le slide usano `if __name__ == "__main__":` per eseguire i test. Tutto l'esempio è però racchiuso tra `'''...'''`, quindi **non viene eseguito**.
# >
# > **[⚠️ LACUNA: `if __name__ == "__main__":` non è spiegato.]**
# >
# > **[⚠️ LACUNA: non è scritto il legame tra sovrascrittura e polimorfismo: nell'esempio `Cane`/`Animale` di Mirko la sovrascrittura di `parla()` è già un caso di polimorfismo.]**

# ---

# ## 5. Quanto è in mano al programmatore (secondo Mirko)

# | Regola | Programmatore | Macchina |
# |---|---|---|
# | Ereditarietà | ~90% | ~10% |
# | Incapsulamento | ~50% | ~50% |
# | Polimorfismo | *poco chiaro* | *poco chiaro* |

# > **[⚠️ LACUNA: per il polimorfismo c'è scritto "90%-10% 10% programmatore", che sembra l'opposto dell'ereditarietà. Da chiarire con Mirko.]**
# >
# > Queste percentuali non compaiono nella documentazione ufficiale: sono stime didattiche e non posso verificarle.

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. `def mostra_informazioni` va indentato dentro `AutomobileSportiva`, altrimenti non sovrascrive nulla.
# 2. `__saldo` non è davvero privato (*name mangling*), e le slide mescolano "privato" e "protetto".
# 3. `super()` è una funzione integrata, non un metodo.
# 4. La sovrascrittura riguarda i metodi ereditati dal padre.
# 5. Il polimorfismo in Python non richiede una classe padre (*duck typing*).
# 6. `super()` segue l'MRO e sceglie il primo padre, non solo "quello che ha il metodo".
# 7. Typo e dettagli: "ereditarità", e `Fido abbaia` senza `!` nel commento.
# 8. Gli esempi con `if` mostrano che in Python la variabile non viene nascosta.

# **Lacune da colmare:**
# - Le altre 3 delle "7 regole" dell'OOP e la definizione di astrazione
# - Il significato di "nascondere nel codice o dal codice"
# - Cosa voleva dimostrare Mirko con gli esempi su `if`, e la frase incompleta "dichiarando prima una variabile fuori e poi una dentro"
# - Scope delle variabili
# - MRO
# - f-string, `join`, `if __name__ == "__main__":`
# - Il significato delle percentuali sul polimorfismo

# Quando vuoi, incolla il prossimo blocco.