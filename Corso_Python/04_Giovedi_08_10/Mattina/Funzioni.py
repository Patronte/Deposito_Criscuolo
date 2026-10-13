# # 📘 Python: Le funzioni (appunti riordinati)

# ---

# ## 1. Cos'è una funzione

# **Concetto:** una funzione è un **blocco di codice autonomo** che esegue una determinata operazione e può essere richiamato (chiamato) quando serve. È un modo di organizzare il codice in **unità modulari**: se la scrivi bene e in modo generico, non devi riscriverla ogni volta.

# Gli appunti la definiscono la "comprova pratica dell'astrazione": nascondi *come* si fa un'operazione e usi solo il nome della funzione.

# > **⚠️ Precisazioni:**
# > 1. Una funzione si può chiamare in qualsiasi punto del codice, ma **solo dopo che è stata definita**. Se la chiami prima del `def`, Python dà `NameError`.
# > 2. Negli appunti si dice che si può "copia incollare in un altro file modificando le variabili". Funziona, ma il metodo usuale è mettere le funzioni in un **modulo** e importarlo.
# >
# > **[⚠️ LACUNA: moduli e `import` non sono nei tuoi appunti. Chiedi se verranno spiegati più avanti.]**

# ---

# ## 2. Come si scrive una funzione

# **Sintassi:**

# ```python
# def nome_funzione(parametri):
#     # corpo della funzione (indentato)
# ```

# | Elemento | Significato |
# |---|---|
# | `def` | Parola chiave che **definisce** la funzione |
# | `nome_funzione` | Il nome scelto da noi (nell'esempio `MatteoDiceCiao`) |
# | `(parametri)` | I valori che la funzione riceve (anche nessuno) |
# | `:` | Obbligatori alla fine della riga |
# | Corpo | Le righe **indentate**, eseguite a ogni chiamata |

# **Esempio pratico:**

# ```python
# nome = input("Inserisci un nome: ")

# def MatteoDiceCiao(nome):
#     print("Ciao ", nome)

# MatteoDiceCiao(nome)      # chiamata della funzione
# ```

# **Risultato (scrivendo Mirko):** `Ciao  Mirko`

# > **⚠️ Precisazioni:**
# > - Nel risultato ci sono **due spazi** tra `Ciao` e `Mirko`: `print` mette già uno spazio tra gli argomenti e tu ne hai aggiunto un altro dentro `"Ciao "`.
# > - `def` **definisce** la funzione, ma non la esegue. Il codice nel corpo parte solo quando scrivi la **chiamata**, cioè l'ultima riga.
# > - Il nome `nome` è usato sia per la variabile esterna sia per il parametro. Sono due variabili diverse, ma gli appunti non lo spiegano.
# > - La convenzione ufficiale (PEP 8) per i nomi delle funzioni è lo **snake_case** (`matteo_dice_ciao`). Lo stile `MatteoDiceCiao` è usato per le **classi**. Chiedi al docente quale usate nel corso.
# >
# > **[⚠️ LACUNA: la frase "la funzione può avere da 1 a infinite funzioni al suo interno" non è chiara. Forse intendeva *istruzioni* (righe di codice). Non la interpreto. Python permette anche funzioni dentro altre funzioni, ma non so se sia ciò che intendeva il docente.]**
# >
# > **[⚠️ LACUNA: non è spiegato il concetto di *scope* (visibilità delle variabili): una variabile creata dentro una funzione esiste solo lì dentro, ed è importante per capire gli esempi successivi.]**

# ---

# ## 3. I parametri

# **Concetto:** i parametri sono i valori che la funzione riceve per poter lavorare. Possono essere **da 0 a infiniti**.

# ```python
# def saluta():                  # 0 parametri
#     print("Ciao")

# def somma(a, b, c):            # 3 parametri
#     print(a + b + c)
# ```

# > **⚠️ Precisazione sul linguaggio:** per la documentazione ufficiale si distingue tra:
# > - **parametro**: il nome tra parentesi nel `def` (`nome`)
# > - **argomento**: il valore che passi nella chiamata (`MatteoDiceCiao("Mirko")`)
# >
# > Negli appunti usi "parametri" per entrambi.
# >
# > **[⚠️ LACUNA: non è spiegato che gli argomenti vengono associati ai parametri in ordine (argomenti posizionali) né che si possono passare per nome.]**

# ### Esempio con due parametri e valori di default

# ```python
# addendo1 = int(input("Seleziona un numero: "))
# addendo2 = int(input("Seleziona un numero: "))
# risultato = 0

# def addizione(addendo1=0, addendo2=0):
#     risultato = addendo1 + addendo2
#     print("La somma dei due addendi è: ", risultato)

# addizione(addendo1, addendo2)
# ```

# **Risultato (scrivendo 3 e 4):** `La somma dei due addendi è:  7`

# > **⚠️ Precisazioni:**
# > - `risultato = 0` fuori dalla funzione **non serve a niente**: dentro la funzione si crea un'altra variabile `risultato`, locale e distinta. Quella esterna resta a `0`.
# > - Questa funzione **stampa** il risultato ma **non lo restituisce**: non puoi riusarlo altrove (vedi sezione 5).

# ---

# ## 4. Parametri di default e parametri tipizzati

# ### Valori di default

# **Concetto:** un parametro di default ha un valore già assegnato, che viene usato **se non passi nessun argomento** per quel parametro.

# ```python
# def addizione(addendo1=0, addendo2=0):
#     print(addendo1 + addendo2)

# addizione(3, 4)    # 7
# addizione(3)       # 3  → addendo2 vale 0
# addizione()        # 0  → entrambi valgono 0
# ```

# > **⚠️ Precisazioni:**
# > 1. Gli appunti dicono che servono "come placeholder". Più precisamente sono **valori predefiniti**.
# > 2. I parametri con default devono stare **dopo** quelli senza default: `def f(a, b=0)` va bene, `def f(a=0, b)` dà errore.

# ### Parametri "tipizzati"

# ```python
# def saluta(nome: str):
#     print("Ciao", nome)
# ```

# > **⚠️ Correzione importante:** `nome: str` è una **annotazione di tipo** (*type hint*): indica a chi legge che ci si aspetta una stringa, ma **Python non controlla nulla**. Se chiami `saluta(5)` non dà errore. Quindi "tipizzati" non vuol dire "obbligati" a quel tipo.
# >
# > **[⚠️ LACUNA: negli appunti c'è scritto "i parametri sono modificabili", senza spiegare cosa significhi (modificare il valore passato? cambiare i parametri della funzione?).]**

# ---

# ## 5. `return`

# **Concetto:** `return` **restituisce un valore** a chi ha chiamato la funzione e **termina** la funzione. Nel punto della chiamata, il valore restituito prende il posto della chiamata stessa. Si usa quando ti serve riutilizzare quel dato (metterlo in una variabile, in una lista, ecc.).

# **Sintassi:**

# ```python
# def nome_funzione(parametri):
#     return valore
# ```

# ### `print` e `return` sono diversi

# ```python
# def somma_print(a, b):
#     print(a + b)        # mostra a schermo, ma restituisce None

# def somma_return(a, b):
#     return a + b        # restituisce il valore

# x = somma_return(2, 3)  # x vale 5
# ```

# ### L'esempio degli appunti (con un errore)

# ```python
# n1 = int(input("Seleziona un numero: "))
# n2 = int(input("Seleziona un numero: "))

# def moltiplicazione(n1=0, n2=0):
#     return n1 * n2

# risultatoM = n1 * n2

# moltiplicazione(10, 15)
# print(risultatoM)
# ```

# > **⚠️ Errore da correggere:**
# > - `risultatoM = n1 * n2` calcola la moltiplicazione **direttamente**, senza usare la funzione.
# > - `moltiplicazione(10, 15)` restituisce `150`, ma il valore **non viene salvato né stampato**: viene scartato.
# > - `print(risultatoM)` stampa quindi il prodotto dei numeri inseriti dall'utente, non il risultato della funzione.

# **Versione corretta:**

# ```python
# n1 = int(input("Seleziona un numero: "))
# n2 = int(input("Seleziona un numero: "))

# def moltiplicazione(n1=0, n2=0):
#     return n1 * n2

# risultatoM = moltiplicazione(n1, n2)   # il return finisce in risultatoM
# print(risultatoM)
# ```

# Con `2` e `3` stampa `6`.

# > **[⚠️ LACUNA: non è spiegato cosa succede quando una funzione non ha `return` (restituisce `None`). Mancano anche restituire più valori insieme e il fatto che dopo un `return` il codice nella funzione non viene eseguito.]**

# ---

# ## 6. Un dettaglio sul codice

# Tutti gli esempi sono racchiusi tra `'''...'''`, quindi **Python non li esegue**. Per provarli devi togliere le triple virgolette.

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. `risultatoM = n1 * n2` non usa la funzione: va scritto `risultatoM = moltiplicazione(n1, n2)`.
# 2. I parametri "tipizzati" sono solo annotazioni: Python non verifica il tipo.
# 3. Il `risultato = 0` esterno nell'addizione non serve: dentro la funzione si crea una variabile separata.
# 4. `def` definisce soltanto: la funzione parte con la chiamata, e va definita **prima** di chiamarla.
# 5. Parametro (nel `def`) e argomento (nella chiamata) sono due termini distinti.
# 6. I parametri di default sono valori predefiniti e vanno dopo quelli senza default.
# 7. Doppio spazio nel `print("Ciao ", nome)`.
# 8. Il nome `MatteoDiceCiao` segue lo stile delle classi: per le funzioni si usa lo snake_case.

# **Lacune da colmare:**
# - Significato di "da 1 a infinite funzioni al suo interno"
# - Significato di "i parametri sono modificabili"
# - Scope delle variabili (locali e globali)
# - Argomenti posizionali e per nome
# - Funzione senza `return` (restituisce `None`) e `return` multipli
# - Moduli e `import` per riutilizzare le funzioni
# - Il legame con l'astrazione dell'OOP

# Quando vuoi, incolla il prossimo blocco.