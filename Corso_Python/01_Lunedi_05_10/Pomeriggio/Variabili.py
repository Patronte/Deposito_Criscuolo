# # 📘 Python: Variabili e tipi di variabili (appunti riordinati)

# ---

# ## 1. Cos'è una variabile

# **Concetto:** una variabile è un nome che si riferisce a un valore conservato in memoria. Se usi di nuovo lo stesso nome, ti riferisci allo stesso valore. L'`=` è l'**operatore di assegnazione**: prende il valore a destra e lo associa al nome a sinistra. Il valore può essere un numero, una stringa, un booleano e così via.

# **Struttura di un'assegnazione:**

# ```python
# nomeVariabile = "valore"
# # nome variabile | operatore di assegnazione | valore assegnato
# ```

# > **⚠️ Precisazione:** in Python non si "dichiara" una variabile come in altri linguaggi. Viene creata nel momento in cui le assegni un valore la prima volta.
# >
# > **[⚠️ LACUNA: negli appunti compare "tipo della variabile" come quarto elemento dell'assegnazione. In Python il tipo non si scrive: lo decide Python dal valore. Manca la spiegazione di come vederlo (di solito con `type()`).]**

# ---

# ## 2. Regole per i nomi delle variabili

# **Regole (dagli appunti):**
# - niente spazi
# - solo lettere, numeri e trattino basso (`_`)
# - devono iniziare con una lettera o un underscore

# ```python
# nomeVariabile = 1    # valido
# nome1 = 2            # valido
# nomeCognome = 3      # valido
# _privata = 4         # valido (inizia con underscore)

# # 1nome = 5          # NON valido: inizia con un numero
# # nome cognome = 6   # NON valido: contiene uno spazio
# ```

# > **⚠️ Precisazioni:**
# > 1. Python distingue maiuscole e minuscole: `nome` e `Nome` sono due variabili diverse.
# > 2. Non si possono usare le **parole riservate** del linguaggio (es. `if`, `for`, `while`, `True`) come nomi.
# > 3. "Le variabili iniziano con la minuscola" è una **convenzione**, non una regola obbligatoria. Lo stile `nomeVariabile` (camelCase) è tipico di altri linguaggi. La guida di stile ufficiale di Python (PEP 8) consiglia lo **snake_case**, cioè `nome_variabile` e `nome_cognome`. Chiedi al docente quale stile usate nel corso.

# ---

# ## 3. Tipi di variabili

# ### 3.1 Primitivi e non primitivi

# **Dagli appunti:**
# - **Basilari/primitivi** (numeri, lettere, booleani): sono già dentro Python.
# - **Non basilari/non primitivi:** li creiamo noi, "praticamente solo gli oggetti".

# > **⚠️ Correzione:** la distinzione è utile all'inizio, ma non è precisa. In Python **ogni valore è un oggetto**, compresi numeri e stringhe, e la documentazione ufficiale non usa il termine "primitivo". Esistono inoltre altri tipi già presenti nel linguaggio oltre a quelli elencati (ad esempio le liste). Quelli creati da noi si chiamano **classi**.
# >
# > **[⚠️ LACUNA: manca la spiegazione di cosa sia un "oggetto" e di come se ne crei uno. Probabilmente verrà trattato con la OOP.]**

# ### 3.2 Numeri interi (`int`)

# **Concetto:** numeri senza parte decimale.

# > **[⚠️ LACUNA: nel punto sugli interi gli appunti mescolano interi e decimali ("e quelli con la virgola") e dicono che le operazioni aritmetiche valgono per questi e "sugli altri tipi di numeri no". Non è chiaro a quali "altri tipi di numeri" ci si riferisca. Manca anche l'elenco delle operazioni aritmetiche (`+`, `-`, `*`, `/` e così via).]**

# ### 3.3 Numeri con la virgola (`float`)

# **Concetto:** numeri con parte decimale, positivi o negativi. Si scrivono con il **punto**, non con la virgola.

# ```python
# prezzo = 3.14
# temperatura = -2.5
# ```

# > **⚠️ Correzione:** negli appunti c'è scritto "no operazioni aritmetiche" per i float. È **sbagliato**: i float supportano le operazioni aritmetiche, e c'è anche una contraddizione con la riga sugli interi, dove le operazioni valgono per entrambi.

# ```python
# print(3.5 + 1.5)   # 5.0
# print(10 / 4)      # 2.5
# ```

# ### 3.4 Stringhe (`str`)

# **Concetto:** testo racchiuso tra virgolette. Sono tipi basilari ma speciali, perché contengono **più valori** (i caratteri) e hanno **metodi propri**.

# ```python
# nomeVariabile = "valore"
# ```

# > **⚠️ Correzione:** gli appunti dicono "ogni lettera è un CHAR". In Python **non esiste il tipo `char`**: ogni carattere è a sua volta una stringa di lunghezza 1.
# >
# > **⚠️ Precisazione:** le virgolette possono essere doppie `" "` o singole `' '`.
# >
# > **[⚠️ LACUNA: i "metodi propri" delle stringhe sono nominati ma non ne è elencato nessuno.]**

# ### 3.5 Booleani (`bool`)

# > **[⚠️ LACUNA: i booleani sono citati tra i tipi basilari, ma gli appunti non li spiegano. Mancano i due valori possibili (`True` e `False`, con la maiuscola iniziale) e il loro uso.]**

# ---

# ## 4. Indici delle stringhe

# **Concetto:** ogni carattere di una stringa ha una posizione (indice), e **si parte a contare da 0**. Si accede al carattere con le parentesi quadre.

# ```python
# a = "Magicka"
# print(a[5])   # k
# print(a[6])   # a
# ```

# | M | a | g | i | c | k | a |
# |---|---|---|---|---|---|---|
# | 0 | 1 | 2 | 3 | 4 | 5 | 6 |

# > **⚠️ Nota sul codice:** nei tuoi appunti questo blocco è racchiuso tra `'''...'''`. Quelle triple virgolette creano una stringa che Python ignora, quindi il codice **non viene eseguito**. Funziona da "commento", ma il modo normale per commentare è il simbolo `#`.

# ---

# ## 5. Concatenare le stringhe

# **Concetto:** si uniscono due o più stringhe con l'operatore `+`.

# ```python
# saluto = "Ciao"
# nome = "Patronte"
# messaggio = saluto + " " + nome
# print(messaggio)   # Ciao Patronte
# ```

# Il `" "` in mezzo serve per inserire lo spazio tra le due parole: senza, otterresti `CiaoPatronte`.

# ---

# ## 6. Input dell'utente

# **Concetto:** `input()` è una funzione integrata che mostra un messaggio e aspetta che l'utente scriva qualcosa. Il testo scritto viene salvato nella variabile.

# ```python
# domanda = input("Io sono una super intelligenza artificiale, cosa vuoi sapere? ")
# print("Non ne ho idea")
# ```

# Qualunque cosa scriva l'utente, il programma risponde sempre "Non ne ho idea", perché la variabile `domanda` non viene mai usata dopo.

# > **[⚠️ LACUNA: non è spiegato che `input()` restituisce **sempre una stringa**, anche se l'utente scrive un numero. È un punto importante per i prossimi esercizi.]**

# ---

# ## 7. I commenti

# Negli appunti usi il simbolo `#` per i commenti, ma non è scritto cosa sia.

# > **[⚠️ LACUNA: manca la spiegazione dei commenti. Un commento è una riga che inizia con `#` e che Python ignora.]**

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. I float **supportano** le operazioni aritmetiche (gli appunti dicono di no).
# 2. In Python non esiste il tipo `char`: un carattere è una stringa di lunghezza 1.
# 3. "Primitivi / non primitivi" è una semplificazione: in Python tutto è un oggetto.
# 4. Il tipo della variabile non si scrive nell'assegnazione, viene dedotto da Python.
# 5. La minuscola iniziale è una convenzione; lo stile consigliato è lo snake_case.

# **Lacune da colmare:**
# - Come vedere il tipo di una variabile (`type()`)
# - Elenco delle operazioni aritmetiche e significato di "altri tipi di numeri"
# - Metodi delle stringhe
# - Booleani: valori e uso
# - Cosa sia un oggetto
# - `input()` restituisce sempre una stringa
# - Commenti con `#`

# Quando vuoi, incolla il prossimo blocco.