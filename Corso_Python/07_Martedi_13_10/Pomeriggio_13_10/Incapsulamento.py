# # 📘 Python: L'incapsulamento in dettaglio (appunti riordinati)

# Questo blocco approfondisce la prima regola dell'OOP vista nel blocco precedente.

# ---

# ## 1. Definizione

# **Concetto:** l'incapsulamento è la capacità di **nascondere i dettagli interni dell'implementazione** di una classe ed **esporre verso l'esterno solo ciò che è necessario**. Permette di decidere cosa si vede **fuori** e cosa si vede **dentro** la classe.

# > Questa definizione chiarisce in parte la frase della lezione precedente ("nascondere nel codice o dal codice"): il nascondere riguarda la visibilità dentro e fuori dalla classe.

# ---

# ## 2. Livelli di indentazione e isolamento

# **Concetto (dai tuoi appunti):** più un elemento si trova *in profondità* nell'indentazione, più è isolato. Se incapsulo a livello 4, i livelli 3, 2, 1 e 0 non lo vedono.

# **Esempio degli appunti:**

# ```python
# # lvl_0
# class x:
#     # lvl_1
#     def y():
#         # lvl_2
#         if True:
#             # lvl_3
#             pass
# ```

# > **⚠️ Correzioni:**
# > 1. **Non tutti i livelli isolano.** In Python creano uno spazio separato (*scope*) le **funzioni**, le **classi** e poche altre strutture. Un `if`, un `for` o un `while` **non** lo creano: lo hai visto negli esempi della lezione precedente, dove `x = 10` dentro l'`if` era visibile anche fuori. Nel tuo esempio quindi `def y()` isola, mentre `if True:` no.
# > 2. **La direzione conta.** Un livello interno può *leggere* le variabili di quello esterno, ma l'esterno non vede ciò che è stato creato dentro.
# > 3. Nell'esempio i livelli sono **da 0 a 3**, mentre il testo parla di "lv4". C'è una piccola incoerenza.
# > 4. `def y():` è scritto **senza `self`**: `x.y()` funziona, ma `x().y()` darebbe `TypeError`.

# **Esempio mio, per vedere l'isolamento con le funzioni:**

# ```python
# def esterna():
#     x = 10
#     def interna():
#         y = 5
#         return x + y        # interna vede x (livello esterno)
#     return interna()

# print(esterna())            # 15
# # print(y)                  # NameError: y esiste solo dentro interna()
# ```

# > **[⚠️ LACUNA: lo *scope* è ancora senza spiegazione nei tuoi appunti. Non è chiaro come le due cose (livelli di indentazione e `if` della lezione precedente) si colleghino all'incapsulamento. Chiedi a Mirko.]**

# ---

# ## 3. Incapsulamento attivo e passivo

# **Dagli appunti:**
# - **Attivo:** lo uso io deliberatamente.
# - **Passivo:** me lo ritrovo in base a come scrivo il codice.

# > **[⚠️ LACUNA: questa distinzione non compare nella documentazione ufficiale di Python, quindi non posso verificarla. Non ci sono esempi: è probabile che sia una classificazione del corso.]**

# ---

# ## 4. Gli strumenti dell'incapsulamento

# Negli appunti sono chiamati "metodi dell'incapsulamento".

# | Strumento | Sintassi | Cosa fa |
# |---|---|---|
# | **Attributo privato** | `__nome` | Nascosto fuori dalla classe |
# | **Metodo privato** | `__metodo()` | Richiamabile solo dentro la classe (nei metodi pubblici) |
# | **Attributo protetto** | `_nome` | Segnala "uso interno": per la classe e i suoi figli |
# | **Getter e setter** | `get_...` / `set_...` | Leggono e modificano un attributo in modo controllato |

# > **⚠️ Correzione:** gli attributi non sono metodi, quindi è meglio chiamarli **strumenti** o **meccanismi**.

# ### 4.1 Attributi privati

# **Concetto:** un attributo con il doppio underscore davanti non è accessibile da fuori con il suo nome.

# **L'esempio degli appunti (era dentro `'''...'''`):**

# ```python
# class parametri_privati:
#     __nome = "Mirko"
#     def __init__(self, nome):
#         self.__nome = nome

# O_pp = parametri_privati("Mirko")
# print(O_pp.__nome())
# ```

# **Risultato:** `AttributeError`, perché da fuori `__nome` non esiste con quel nome.

# > **⚠️ Precisazioni:**
# > - Anche senza il nascondimento ci sarebbe un secondo errore: `__nome()` con le **parentesi** tenta di chiamare una stringa come se fosse una funzione, dando `TypeError`.
# > - Per leggere il valore si usa un metodo pubblico: `O_pp.get_nome()` (vedi sezione 4.4).
# > - Come detto nella lezione precedente, il doppio underscore attiva il *name mangling*: l'attributo si chiama in realtà `_parametri_privati__nome` ed è raggiungibile se lo scrivi per intero. È una protezione "di cortesia".
# > - Gli appunti dicono che l'attributo privato stabilisce "se è leggibile fuori da quel punto, **e da chi**". In Python non puoi scegliere *chi* può leggerlo: o ha il nome originale o non lo ha.
# >
# > **[⚠️ LACUNA: non è scritto se l'errore sia voluto, cioè se l'esempio serva a mostrare che l'accesso fallisce.]**

# ### 4.2 Metodi privati

# **Concetto (dagli appunti):** si richiamano dentro i metodi pubblici.

# ```python
# def __metodo_privato(self):
#     print("sono dentro")
# ```

# > **[⚠️ LACUNA: nell'esempio il metodo `__metodo_privato` viene definito ma **mai chiamato**: manca un metodo pubblico che lo richiami.]**

# **Cosa succede (verificabile dalla documentazione):**

# ```python
# # O_pp.__metodo_privato()    # AttributeError se chiamato da fuori
# # dentro la classe si scrive: self.__metodo_privato()
# ```

# ### 4.3 Attributi protetti

# **Concetto:** un attributo con **un solo** underscore (`_protetto`) segnala che è "per uso interno": lo usano la classe e i suoi figli. Gli appunti precisano giustamente che **non è una regola**.

# ```python
# print(O_pp._protetto)     # funziona anche da fuori: stampa una riga vuota
# ```

# L'esempio lo dimostra: l'attributo viene letto da fuori senza problemi. È solo una **convenzione** tra programmatori e Python non la fa rispettare.

# ### 4.4 Getter e setter

# **Concetto:** sono due metodi pubblici che permettono di accedere a un attributo privato in modo controllato.

# | Tipo | Scopo |
# |---|---|
# | **Getter** | Restituisce il valore dell'attributo |
# | **Setter** | Lo modifica, di solito dopo aver fatto dei controlli |

# > **[⚠️ LACUNA: i termini getter e setter non sono definiti nei tuoi appunti. La spiegazione sopra è ricavata dall'uso nel codice.]**
# >
# > **⚠️ Precisazione:** in Python il modo più usato per farlo è il decoratore `@property`. Non compare nei tuoi appunti, quindi non lo approfondisco.

# ---

# ## 5. L'esempio completo

# ```python
# class Parametri_privati():
#     __nome = "mirko"                 # attributo privato
#     _protetto = ""                   # attributo protetto

#     def __init__(self, nome):
#         self.__nome = nome

#     def get_nome(self):              # getter
#         return self.__nome

#     def set_nome(self, nome_nuovo):  # setter
#         if len(nome_nuovo) < 0:
#             print("sei un pippo")
#         else:
#             self.__nome = nome_nuovo

#     def __metodo_privato(self):      # metodo privato
#         print("sono dentro")

# O_pp = Parametri_privati("mirko")
# print(O_pp.get_nome())
# O_pp.set_nome("Marco")
# print(O_pp.get_nome())

# print(O_pp._protetto)
# ```

# **Risultato:**

# ```
# mirko
# Marco

# ```

# L'ultima riga è vuota perché `_protetto` contiene una stringa vuota.

# ### Cosa si può fare da fuori

# | Istruzione | Risultato |
# |---|---|
# | `O_pp.get_nome()` | ✅ funziona |
# | `O_pp._protetto` | ✅ funziona (è solo convenzione) |
# | `O_pp.__nome` | ❌ `AttributeError` |
# | `O_pp.__metodo_privato()` | ❌ `AttributeError` |
# | `O_pp._Parametri_privati__nome` | ✅ funziona (*name mangling*) |

# > **⚠️ Errore da correggere:** nel setter la condizione `len(nome_nuovo) < 0` **non è mai vera**, perché la lunghezza di una stringa non è mai negativa. Il controllo quindi non scatta mai, nemmeno con una stringa vuota. Se l'intenzione era rifiutare i nomi vuoti, serve `== 0`:

# ```python
# def set_nome(self, nome_nuovo):
#     if len(nome_nuovo) == 0:
#         print("Il nome non può essere vuoto")
#     else:
#         self.__nome = nome_nuovo
# ```

# Il motivo del setter è proprio questo: modificare l'attributo **solo se il valore è accettabile**. In questo modo l'incapsulamento diventa utile.

# > **⚠️ Precisazione:** il nome `Parametri_privati` mescola maiuscola e underscore. Per le classi PEP 8 consiglia la forma `ParametriPrivati`. Inoltre `__nome` e `_protetto` sono **attributi**, non "parametri": un parametro è quello della funzione (come `nome` in `__init__`).

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. Nel setter `len(...) < 0` non è mai vero: serve `== 0`.
# 2. Solo funzioni e classi creano uno scope: `if`, `for` e `while` no.
# 3. Un livello interno vede quello esterno, non il contrario.
# 4. `O_pp.__nome()` ha due problemi: l'accesso è bloccato e le `()` provano a chiamare una stringa.
# 5. Gli attributi privati usano il *name mangling*: sono nascosti, ma non inaccessibili. E non si può decidere "da chi".
# 6. Gli attributi non sono "metodi dell'incapsulamento": sono strumenti.
# 7. `__nome` e `_protetto` sono attributi, non parametri.
# 8. Nell'esempio dei livelli, `def y()` è senza `self`, e i livelli vanno da 0 a 3, non a 4.

# **Lacune da colmare:**
# - Scope delle variabili, ancora senza spiegazione
# - Il legame tra livelli di indentazione, esempi con `if` e incapsulamento
# - Incapsulamento attivo e passivo: nessun esempio, e non verificabile nella documentazione ufficiale
# - Definizione di getter e setter, e `@property`
# - Esempio d'uso di un metodo privato richiamato da un metodo pubblico
# - Se l'errore di `O_pp.__nome()` sia voluto
# - Le altre 3 delle "7 regole" dell'OOP e la definizione di astrazione, ancora da recuperare

# Quando vuoi, incolla il prossimo blocco.