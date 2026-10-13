# # 📘 Python: I cicli `while` e `for`, e `range()` (appunti riordinati)

# ---

# ## 1. Le due domande di ogni ciclo

# **Concetto:** prima di scrivere un ciclo, rispondi a due domande:

# 1. **Qual è la condizione per cui si ripete?**
# 2. **Qual è il modo per romperlo (farlo finire)?**

# Se la seconda risposta manca, il ciclo non finisce mai (**ciclo infinito**).

# > **[⚠️ LACUNA: la parola "iterazione" è usata ma non definita. Per la documentazione ufficiale è un singolo passaggio del ciclo, cioè una ripetizione del blocco.]**

# ---

# ## 2. Il ciclo `while`

# **Concetto:** ripete un blocco di codice finché la condizione è vera.

# **Sintassi:**

# ```python
# while condizione:
#     # blocco ripetuto finché la condizione è vera
# ```

# ### Esempio 1: ciclo "matematico"

# ```python
# conteggio = 0
# while conteggio < 5:       # quando ripete: finché conteggio < 5
#     print(conteggio)
#     conteggio += 1         # come romperlo: ad ogni giro conteggio sale
# ```

# **Risultato:** stampa `0`, `1`, `2`, `3`, `4`.

# | Giro | `conteggio` | `conteggio < 5` | Azione |
# |---|---|---|---|
# | 1 | 0 | vera | stampa 0, poi diventa 1 |
# | 2 | 1 | vera | stampa 1, poi diventa 2 |
# | 3 | 2 | vera | stampa 2, poi diventa 3 |
# | 4 | 3 | vera | stampa 3, poi diventa 4 |
# | 5 | 4 | vera | stampa 4, poi diventa 5 |
# | 6 | 5 | **falsa** | il ciclo finisce |

# Negli appunti la riga era scritta `(conteggio)+=1`. Le parentesi sono inutili, la forma normale è `conteggio += 1`, che equivale a `conteggio = conteggio + 1`.

# ### Esempio 2: ciclo con uscita decisa dall'utente

# L'idea degli appunti: il ciclo continua finché l'utente non scrive `end`. Così com'è scritto il codice però **non funziona**:

# ```python
# # VERSIONE DEGLI APPUNTI (con errori)
# while "controllore":
#     print("ciao")
#     scelta = input("scrivi end per uscire")
#     if scelta.lower()== "end":
#     controllore = False
# ```

# > **⚠️ Correzioni:**
# > 1. `while "controllore":` usa la **stringa** `"controllore"`, non la variabile. Una stringa non vuota vale sempre `True`, quindi il ciclo non finisce mai.
# > 2. La variabile `controllore` non viene mai creata prima del ciclo.
# > 3. `controllore = False` deve essere **indentata** sotto l'`if`, altrimenti Python dà `IndentationError`.
# > 4. Il titolo "ciclo che si ripete una sola volta" non corrisponde al codice: il ciclo si ripete **finché l'utente non scrive `end`**.

# **Versione corretta:**

# ```python
# controllore = True
# while controllore:
#     print("ciao")
#     scelta = input("scrivi end per uscire ")
#     if scelta.lower() == "end":
#         controllore = False
# ```

# `.lower()` è un metodo delle stringhe: trasforma il testo in minuscolo, così `END`, `End` ed `end` vengono riconosciuti tutti.

# > **Nota:** quando l'utente scrive `end`, il blocco finisce di essere eseguito e solo dopo Python ricontrolla la condizione. Il ciclo si ferma quindi al giro successivo.

# ---

# ## 3. `for` o `while`: quando usare quale

# | | `for` | `while` |
# |---|---|---|
# | **Quando** | Valori **determinati o determinabili** (so quante volte o su cosa ripetere) | Valori **non determinabili** in anticipo |
# | **Struttura** | Le condizioni stanno **tutte in una riga** | Si divide in **condizione di ripetizione** e **punto di rottura** |

# ---

# ## 4. Il ciclo `for`

# **Concetto:** scorre una sequenza un elemento alla volta.

# - **ELEMENTO:** variabile che rappresenta l'elemento corrente in ogni iterazione.
# - **SEQUENZA:** ciò su cui si itera (una lista, una stringa, o l'output di `range()`).

# **Sintassi:**

# ```python
# for elemento in sequenza:
#     # blocco eseguito una volta per ogni elemento
# ```

# > **[⚠️ LACUNA: negli appunti sono definiti ELEMENTO e SEQUENZA, ma lo schema `for ... in ...:` non è scritto. L'ho ricavato dall'esempio e dalla documentazione ufficiale.]**

# **Esempio che funziona:**

# ```python
# numeri = [1, 2, 3, 4, 5]
# for numero in numeri:
#     print(numero)
# ```

# **Risultato:** stampa `1`, `2`, `3`, `4`, `5`, uno per riga.

# **Esempio che dà errore:**

# ```python
# limite = 5
# for numero in limite:
#     print(numero)
# ```

# **Risultato:** `TypeError: 'int' object is not iterable`. Un intero non è una sequenza, quindi non si può scorrere.

# > **[⚠️ LACUNA: negli appunti non è scritto che questo secondo esempio sia un errore. Probabilmente serve a introdurre `range()`, ma andrebbe confermato.]**

# ---

# ## 5. La funzione `range()`

# **Concetto:** `range()` genera una **sequenza di numeri interi**. Serve quando vuoi usare un `for` su un numero invece che su una lista.

# ```python
# for i in range(5):
#     print(i)        # 0, 1, 2, 3, 4
# ```

# > **⚠️ Correzioni:**
# > 1. Gli appunti dicono che `range(5)` "vale 1-2-3-4-5". È **sbagliato**: parte da **0** e si ferma a **4**. Gli appunti si correggono da soli più avanti ("0 a 4").
# > 2. Gli appunti dicono che salvato in una variabile `range` "salverà una lista". Non è così: viene salvato un oggetto `range`, non una lista. Per ottenere una lista serve `list(range(5))` oppure `[*range(5)]` (sezione 6).
# > 3. Nella documentazione ufficiale `range` è un **tipo di sequenza**, non una funzione vera e propria, anche se si usa come una funzione.
# >
# > **[⚠️ LACUNA: la frase "essendo definita in partenza/maniera statica, a differenza dell'intero non crea conflitti" non è chiara. Non la interpreto.]**

# ### I 3 parametri

# | Parametro | Obbligatorio? | Significato | Default |
# |---|---|---|---|
# | **start** | No | Da dove parte | `0` |
# | **stop** | **Sì** | Dove finisce, **escluso** dalla sequenza | / |
# | **step** | No | Di quanto avanza ogni volta | `1` |

# ```python
# # solo stop
# for i in range(5):
#     print(i)              # 0, 1, 2, 3, 4

# # start e stop
# for i in range(0, 5):
#     print(i)              # 0, 1, 2, 3, 4  (stesso risultato)

# # start, stop e step
# for i in range(0, 10, 2):
#     print(i)              # 0, 2, 4, 6, 8
# ```

# Nell'ultimo caso il commento originale ("conterà da 0 a 10") è impreciso: il 10 è **escluso**, quindi la sequenza termina a **8**.

# > **Nota dalla documentazione:** con un solo numero, `range(5)`, quel numero è lo **stop**. Con due numeri sono **start e stop**.

# ---

# ## 6. L'operatore `*` (splat / unpacking)

# **Concetto:** davanti a una sequenza, `*` ne "spacchetta" gli elementi uno per uno. Dentro le parentesi quadre li raccoglie in una **nuova lista**.

# ```python
# lista = [*range(10)]
# lista2 = [*range(1, 10, 2)]
# print(lista)     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(lista2)    # [1, 3, 5, 7, 9]
# ```

# > **⚠️ Correzioni:**
# > 1. Gli appunti dicono che `*` "serve a creare le liste". In realtà **spacchetta** una sequenza. È il fatto di stare dentro `[ ]` che produce una lista.
# > 2. Il commento "una lista da 10 andando avanti di due in due" è impreciso: `range(1, 10, 2)` parte da **1**, si ferma **prima di 10** e dà 5 numeri (1, 3, 5, 7, 9).
# > 3. Un modo più comune per ottenere lo stesso risultato è `list(range(10))`.
# >
# > **[⚠️ LACUNA: "splat" è il nome informale. Nella documentazione ufficiale si parla di *iterable unpacking*.]**

# ---

# ## 7. Start, stop e step scelti dall'utente

# ```python
# scelta1 = int(input("Inserisci lo start "))
# scelta2 = int(input("Inserisci lo stop "))
# scelta3 = int(input("Inserisci lo step "))
# lista3 = [*range(scelta1, scelta2, scelta3)]
# print(lista3)
# ```

# Il programma chiede i tre valori, costruisce il `range` e lo trasforma in lista. Esempio: con start 2, stop 12, step 3 stampa `[2, 5, 8, 11]`.

# > **⚠️ Precisazioni:**
# > - `input()` restituisce sempre una **stringa**, quindi `int(...)` serve per convertire il testo in numero. Senza, `range` darebbe errore.
# > - Se l'utente scrive qualcosa che non è un numero intero, `int()` dà `ValueError`.
# > - Lo step non può essere `0`: darebbe errore.
# >
# > **[⚠️ LACUNA: negli appunti `int()` è usata ma mai spiegata.]**

# ---

# ## 8. `pass`, `continue` e `break`

# **Dagli appunti:**
# - `pass` si usa quando non si vuole eseguire un'azione, ed "è un segnaposto".

# ```python
# for i in range(3):
#     pass      # il blocco non può restare vuoto: pass non fa nulla
# ```

# > **⚠️ Precisazione:** `pass` non serve solo nei cicli. Si usa ovunque Python richieda un blocco, ad esempio dopo un `if` o dentro una funzione ancora da scrivere.
# >
# > **[⚠️ LACUNA: `continue` e `break` sono nel titolo ma non sono spiegati. Non c'è nemmeno un esempio per `pass`, `continue` o `break`.]**
# >
# > **⚠️ Nota sul codice:** la riga "il pass si usa quando..." è scritta **senza `#` e fuori da una stringa**. Se esegui il file, Python dà `SyntaxError`. Va trasformata in commento con `#`.

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. `while "controllore":` è sempre vero: va usata la variabile (`while controllore:`), da creare prima del ciclo.
# 2. `controllore = False` va indentata sotto l'`if`.
# 3. `range(5)` genera 0, 1, 2, 3, 4, non 1-5.
# 4. `x = range(5)` non salva una lista: serve `list(range(5))` o `[*range(5)]`.
# 5. Con `range(0, 10, 2)` il 10 è escluso: l'ultimo numero è 8.
# 6. `*` spacchetta una sequenza, non "crea liste" da solo.
# 7. `range(1, 10, 2)` parte da 1 e finisce a 9.
# 8. `pass` serve ovunque serva un blocco, non solo nei cicli.
# 9. La riga su `pass` va commentata con `#`.

# **Lacune da colmare:**
# - Definizione di "iterazione"
# - Se l'esempio `for numero in limite` sia un errore voluto
# - Frase poco chiara su `range` ("definita in partenza... non crea conflitti")
# - Spiegazione di `int()` e dei possibili errori di conversione
# - **`break` e `continue`**: spiegazione ed esempi
# - Esempi d'uso di `pass`
# - `match` (citato nella lezione precedente) e la terza famiglia di controllo del flusso, ancora da recuperare

# Quando vuoi, incolla il prossimo blocco.