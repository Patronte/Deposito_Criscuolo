# # 📘 Python: Collezioni e liste (appunti riordinati)

# ---

# ## 1. Cos'è una lista

# **Concetto:** una lista (`list`) è una collezione **ordinata** e **modificabile** di dati. Serve a tenere più valori in un'unica variabile.

# Le 4 caratteristiche dagli appunti:

# | Caratteristica | Significato |
# |---|---|
# | **Tipo** | È di tipo `list` |
# | **Definizione** | Si definisce con le parentesi quadre `[]` |
# | **Ordinamento** | È ordinata: ogni elemento ha una posizione fissa |
# | **Elementi** | Eterogenei: possono avere tipi diversi (numeri, stringhe, booleani...) |

# Gli appunti dicono che la lista non è né un tipo basilare né non basilare, ma un **tipo composto**. Il termine compare anche nel tutorial ufficiale di Python ("compound data types", cioè tipi che raggruppano altri valori), quindi qui è corretto.

# > **⚠️ Precisazioni:**
# > 1. **Collezione** è il nome più generale: la lista è solo un tipo di collezione. Ne esistono altre (tuple, set, dizionari).
# > 2. **"Ordinata"** vuol dire che gli elementi *mantengono la posizione* in cui li hai messi. Non vuol dire "messa in ordine crescente": quello lo fa il metodo `sort()` (vedi sezione 5).
# > 3. **"Modificabile"** si dice *mutabile*: puoi cambiare gli elementi dopo aver creato la lista.

# ---

# ## 2. Creare una lista

# ```python
# listaNum = [1, 2, 3, 4, 5, 10]
# listaNom = ["Peppe", "Mirko", "Muciaccia", "Andonio"]
# listaMisto = ["Peppino", 2, True, 4.20]   # elementi di tipi diversi
# ```

# - `listaNum`: solo numeri interi
# - `listaNom`: solo stringhe
# - `listaMisto`: stringa, intero, booleano e float insieme (lista eterogenea)

# ---

# ## 3. Leggere un elemento (indice)

# **Concetto:** come per le stringhe, si accede a un elemento con le parentesi quadre e **si parte a contare da 0**.

# ```python
# print(listaNom[0])   # Peppe
# ```

# | "Peppe" | "Mirko" | "Muciaccia" | "Andonio" |
# |---|---|---|---|
# | 0 | 1 | 2 | 3 |

# ---

# ## 4. Modificare un elemento

# **Concetto:** poiché la lista è modificabile, si può sostituire un elemento assegnando un nuovo valore a una sua posizione.

# ```python
# listaNum[2] = 500      # sostituisce il valore in posizione 2 (era 3)
# print(listaNum)        # [1, 2, 500, 4, 5, 10]
# ```

# > **⚠️ Nota:** negli appunti il commento dice "grazie alla riga 16". I numeri di riga cambiano appena modifichi il file, quindi conviene descrivere l'istruzione (come ho fatto sopra).

# ---

# ## 5. I metodi delle liste

# **Concetto:** un **metodo** è una funzione che appartiene a un oggetto e si chiama con il punto: `lista.metodo()`. Le liste ne hanno molti, ed è la loro peculiarità (come anticipato nella lezione precedente).

# Metodi visti in aula: `append`, `insert`, `remove`, `sort`. Negli appunti compare in elenco anche `len`.

# > **⚠️ Correzione:** `len` **non è un metodo**, è una **funzione integrata** (la stessa categoria vista nella prima lezione). Si scrive `len(lista)`, non `lista.len()`.

# ```python
# listaNum = [15, 2, 25, 4, 5, 10]    # la lista viene ridefinita: riparte da zero

# print(len(listaNum))                # 6  → numero di elementi

# listaNum.append(6)                  # aggiunge 6 in fondo
# print(listaNum)                     # [15, 2, 25, 4, 5, 10, 6]

# listaNum.insert(12, 10)             # insert(posizione, valore)
# listaNum.remove(10)                 # rimuove il primo 10 trovato
# print(listaNum)                     # [15, 2, 25, 4, 5, 6, 10]

# listaNum.sort()                     # ordina in modo crescente
# print(listaNum)                     # [2, 4, 5, 6, 10, 15, 25]
# ```

# ### Riepilogo dei metodi

# | Metodo / funzione | Cosa fa | Sintassi |
# |---|---|---|
# | `len()` *(funzione)* | Restituisce quanti elementi ha la lista | `len(lista)` |
# | `append()` | Aggiunge un elemento **alla fine** | `lista.append(valore)` |
# | `insert()` | Inserisce un elemento in una **posizione scelta** | `lista.insert(posizione, valore)` |
# | `remove()` | Elimina la **prima** occorrenza del valore indicato | `lista.remove(valore)` |
# | `sort()` | Ordina la lista **modificandola direttamente** | `lista.sort()` |

# ### Cosa succede passo per passo

# | Istruzione | Lista dopo l'istruzione |
# |---|---|
# | `[15, 2, 25, 4, 5, 10]` | `[15, 2, 25, 4, 5, 10]` |
# | `append(6)` | `[15, 2, 25, 4, 5, 10, 6]` |
# | `insert(12, 10)` | `[15, 2, 25, 4, 5, 10, 6, 10]` |
# | `remove(10)` | `[15, 2, 25, 4, 5, 6, 10]` |
# | `sort()` | `[2, 4, 5, 6, 10, 15, 25]` |

# > **⚠️ Punti da capire bene** (secondo la documentazione ufficiale):
# > - In `insert(12, 10)` il **primo numero è la posizione**, il secondo è il valore. La lista ha solo 7 elementi, quindi la posizione 12 non esiste: in questo caso Python inserisce l'elemento **in fondo**, senza dare errore.
# > - Dopo l'`insert` ci sono **due** `10` nella lista. `remove(10)` elimina solo il **primo** (quello in posizione 5).
# > - `sort()` modifica la lista stessa e non restituisce niente, quindi `print(listaNum.sort())` stamperebbe `None`.

# ---

# ## 6. Un dettaglio sul codice

# La stringa tra `'''...'''` all'inizio del file contiene la teoria e non viene eseguita da Python, quindi funziona come una nota. Per i commenti brevi si usa `#`.

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. `len` è una funzione integrata, non un metodo.
# 2. "Ordinata" non significa "messa in ordine crescente": quello lo fa `sort()`.
# 3. Il commento "riga 16" è fragile: meglio descrivere l'istruzione.

# **Lacune da colmare:**
# - **[⚠️ LACUNA: nel commento "Inserisci in lista i seg valori" non sono scritti i valori da inserire. Il codice usa `insert(12, 10)`, ma non è chiaro se fosse l'esercizio richiesto, né quale posizione e quale valore intendesse il docente.]**
# - **[⚠️ LACUNA: mancano le spiegazioni scritte di `append`, `insert`, `remove`, `sort`. Nei commenti c'è solo l'ordine di utilizzo.]**
# - **[⚠️ LACUNA: non è spiegata la differenza tra funzione e metodo, né la notazione con il punto.]**
# - **[⚠️ LACUNA: nelle spiegazioni della lezione precedente restava da capire cosa intendesse il docente con "definire i singoli metodi specifici": non risulta ancora chiaro.]**

# Quando vuoi, incolla il prossimo blocco.