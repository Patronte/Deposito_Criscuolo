# # 📘 Python: Controllo del flusso e condizioni (appunti riordinati)

# ---

# ## 1. Cos'è il controllo del flusso

# **Concetto:** è la capacità di alterare **quali righe vengono eseguite** e in che modo, escludendone alcune o ripetendone altre. Senza controllo del flusso Python leggerebbe il programma dall'alto in basso, una riga dopo l'altra.

# Negli appunti i controlli del flusso sono divisi in due tipi:

# | Tipo | Famiglia | Strumenti citati | Cosa fa |
# |---|---|---|---|
# | **Esclusivo** | Condizioni | `if`, `else`, `match` | Sceglie quale blocco di codice eseguire, escludendo gli altri |
# | **Ripetitivo** | Cicli / Iterazioni | `for`, `while` | Ripete un blocco di codice |

# > **⚠️ Precisazioni:**
# > 1. Negli appunti l'elenco delle condizioni è `if`, `else`, `match`, ma più avanti usi anche `elif`, che quindi fa parte della famiglia.
# > 2. Il ciclo `while` ripete finché la condizione è `True`, come scrivi. Il `for` invece, per la documentazione ufficiale, **scorre gli elementi di una sequenza** (ad esempio una lista) e si ferma quando finiscono. Quindi la frase "ripetono finché qualcosa è True" vale bene per `while`, meno per `for`.
# > 3. `match` esiste solo da **Python 3.10** in poi.
# >
# > **[⚠️ LACUNA: i cicli `for` e `while` sono solo nominati, senza spiegazione né esempi. Anche `match` è citato ma non spiegato né usato nel codice.]**
# >
# > **[⚠️ LACUNA: nella lezione precedente le famiglie dei controllori del flusso sembravano tre ("la famiglia delle condizioni, la famiglia dei cicli, e la famiglia dei..."), qui ne risultano due. Non è chiaro se la terza sia stata scartata o se resti da recuperare.]**

# ---

# ## 2. `if` ed `else`

# **Concetto:** `if` esegue un blocco di codice **solo se** la condizione è vera. `else` aggiunge un "altrimenti": il blocco che viene eseguito quando la condizione dell'`if` è falsa.

# **Sintassi:**

# ```python
# if condizione:
#     # blocco eseguito se la condizione è vera
# else:
#     # blocco eseguito altrimenti
# ```

# I due punti `:` alla fine della riga e **l'indentazione** del blocco sono obbligatori. È la regola dell'indentazione vista nella prima lezione: le righe rientrate appartengono all'`if`.

# **Esempio pratico:**

# ```python
# x = 1
# if x > 9:
#     print("Eccellente")
# else:
#     print("Sub-Eccellente")
# ```

# **Risultato:** `Sub-Eccellente`, perché `1 > 9` è falso e quindi parte l'`else`.

# > **[⚠️ LACUNA: il commento "primo esempio di indentazione (intrinseca all'if) e proprietarietà" non è chiaro, in particolare la parola "proprietarietà". Non lo interpreto.]**
# >
# > **[⚠️ LACUNA: gli operatori di confronto (`>`, `==`) sono usati ma mai spiegati. Manca l'elenco completo (`<`, `>=`, `<=`, `!=`) e la differenza tra `=` (assegnazione) e `==` (confronto).]**

# ---

# ## 3. `elif`

# **Concetto:** permette di controllare **più condizioni** in sequenza.

# **Regole dagli appunti:**
# - `elif` può stare solo **dopo** l'`if` e **mai dopo** l'`else`
# - se ne possono avere quanti ne servono
# - ci può essere **un solo** `if` e **un solo** `else`

# > **⚠️ Precisazione:** l'`else` è **facoltativo**. Puoi scrivere `if` e `elif` senza `else`.

# **Sintassi:**

# ```python
# if condizione1:
#     ...
# elif condizione2:
#     ...
# elif condizione3:
#     ...
# else:
#     ...
# ```

# **Esempio pratico:**

# ```python
# x = 1
# if x > 0:
#     print("va bene e' maggiore di 0")
# elif x > 10:
#     print("UAU è maggiore di 10")
# elif x == 1:
#     print("wa è popio uguale")
# else:
#     print("niente chicco")
# ```

# **Risultato:** `va bene e' maggiore di 0`

# > **⚠️ Punto fondamentale:** Python controlla le condizioni **dall'alto in basso** ed esegue **solo il primo blocco** la cui condizione è vera, poi salta tutto il resto. Qui `x > 0` è vera per `x = 1`, quindi gli altri rami **non vengono nemmeno controllati**.
# >
# > Per lo stesso motivo il ramo `x > 10` è costruito male: qualunque numero maggiore di 10 è anche maggiore di 0, quindi sarebbe già stato catturato dal primo `if`. Quel ramo **non verrà mai eseguito**. Anche `x == 1` non verrebbe mai raggiunto. L'**ordine** delle condizioni conta.

# | Condizione | Valore con `x = 1` | Eseguito? |
# |---|---|---|
# | `x > 0` | vera | ✅ sì, e il controllo si ferma qui |
# | `x > 10` | non controllata | ❌ |
# | `x == 1` | non controllata | ❌ |
# | `else` | non controllato | ❌ |

# ---

# ## 4. `if` annidati

# **Concetto:** un `if` può stare **dentro un altro `if`**. Il blocco interno viene valutato solo se la condizione esterna è vera. L'annidamento si riconosce dal **doppio livello di indentazione**.

# **Esempio pratico:**

# ```python
# x = 1
# if x > 0:
#     print("Il numero è positivo")
#     if x == 100:
#         print("wow è popio 100")
# else:
#     print("Il numero è zero")
# ```

# **Risultato con `x = 1`:** `Il numero è positivo`. L'`if` esterno è vero, quello interno (`x == 100`) è falso e non stampa niente.

# > **⚠️ Correzione:** il messaggio dell'`else` dice "Il numero è zero", ma l'`else` si attiva per **qualsiasi valore non maggiore di 0**, quindi anche per i numeri negativi (ad esempio `-5`). Il messaggio sarebbe corretto solo se la condizione fosse `x == 0`. Per distinguere i tre casi serve un `elif`:
# >
# > ```python
# > if x > 0:
# >     print("Il numero è positivo")
# > elif x == 0:
# >     print("Il numero è zero")
# > else:
# >     print("Il numero è negativo")
# > ```
# >
# > **[⚠️ LACUNA: non è scritto a cosa servisse il caso `x == 100` nell'esercizio, né perché si usi un `if` annidato invece di un `elif`.]**

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. Il `for` non ripete "finché qualcosa è True": scorre gli elementi di una sequenza (questo vale per il `while`).
# 2. L'`else` non coincide con "zero": copre tutti i casi non gestiti dai rami precedenti.
# 3. Il ramo `elif x > 10` dopo `if x > 0` non viene mai raggiunto: l'ordine delle condizioni è importante.
# 4. `elif` va aggiunto all'elenco della famiglia delle condizioni.
# 5. L'`else` è facoltativo.

# **Lacune da colmare:**
# - Spiegazione ed esempi di `for`, `while` e `match`
# - Operatori di confronto e differenza tra `=` e `==`
# - Significato di "proprietarietà" nel commento sull'indentazione
# - Scopo del caso `x == 100` nell'esempio annidato
# - Se esistesse una terza famiglia di controllo del flusso, citata nella lezione precedente

# Quando vuoi, incolla il prossimo blocco.