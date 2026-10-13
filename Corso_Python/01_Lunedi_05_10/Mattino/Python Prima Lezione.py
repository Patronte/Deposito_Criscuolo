# # 📘 Python: Prima Lezione (appunti riordinati)

# ---

# ## 1. Cos'è Python

# **Concetto:** Python è un linguaggio di programmazione con queste caratteristiche principali.

# | Caratteristica | Significato |
# |---|---|
# | **Interpretato** | Il codice che scrivi viene tradotto ed eseguito dall'interprete, senza che tu debba compilarlo a mano prima. |
# | **Orientato agli oggetti (OOP)** | Supporta la programmazione a oggetti (vedi sezione 2). |
# | **Dinamico** | Il tipo è legato al valore, non alla variabile: una variabile può cambiare tipo. |
# | **Ad alto livello** | Alto livello di astrazione: vicino al linguaggio umano, lontano dalla macchina. Basso livello = più vicino alla macchina. |
# | **Sicuro ma più lento** | Più lento di altri linguaggi (es. C). |

# > **⚠️ Correzione 1:** negli appunti c'è scritto che il linguaggio "viene convertito in C". Non è esatto. L'implementazione standard (CPython) è *scritta* in C. Il tuo codice viene tradotto in *bytecode*, che una macchina virtuale esegue. Chiedi conferma al docente su cosa intendesse.

# **Sintassi ed esempio (tipizzazione dinamica):**

# ```python
# x = 5          # x punta a un numero intero
# x = "Mirko"    # ora x punta a una stringa: il tipo è cambiato
# ```

# Il tipo cambia, ma una variabile non può mai esistere "senza tipo": ogni valore ha sempre un tipo. Per questo Python è dinamico e allo stesso tempo *fortemente tipizzato*. Nei tuoi appunti l'esempio aveva le virgolette di chiusura mancanti (`"Mirko`): qui l'ho corretto.

# **I 3 elementi fondamentali di un linguaggio di programmazione** (secondo il corso):
# 1. Variabili
# 2. Condizioni e Cicli
# 3. Funzioni

# ---

# ## 2. OOP: Object Oriented Programming

# **Concetto:** paradigma di programmazione molto importante in ambito lavorativo. Secondo gli appunti "ci aiuta a saltare calcoli".

# Essere OOP vuol dire rispettare dei principi:
# - **Regola base:** Astrazione
# - **Le 3 regole fondamentali:** Ereditarietà, Incapsulamento, Polimorfismo

# > **[⚠️ LACUNA: gli appunti dicono che le regole da imparare sono 7, ma ne risultano elencate solo 4 (Astrazione, Ereditarietà, Incapsulamento, Polimorfismo). Mancano le altre 3.]**
# >
# > **[⚠️ LACUNA: manca la spiegazione di ciascun principio, e non è chiaro cosa significhi "saltare calcoli". Va riascoltato o riscritto dalla lezione.]**

# ---

# ## 3. Indentazione

# **Concetto:** lo spazio a sinistra prima del codice. Python lo usa per capire a quale blocco appartiene ogni riga. Se è sbagliata, il codice si rompe (errore o comportamento diverso).

# **Esempio** (esempio mio, a scopo illustrativo):

# ```python
# if True:
#     print("Questa riga è dentro l'if")   # 4 spazi di indentazione
# print("Questa è fuori")                   # nessuna indentazione
# ```

# > **⚠️ Correzione 2:** negli appunti c'è scritto che virgole e punti e virgola "non contano quasi nulla". Per il punto e virgola è vero: in Python è facoltativo e quasi mai usato. Le **virgole invece contano molto**: separano gli argomenti di una funzione e gli elementi di liste e tuple (`print("a", "b")`, `[1, 2, 3]`). Se le togli, il codice non funziona.

# ---

# ## 4. Funzioni integrate (built-in)

# **Concetto:** una funzione integrata (*built-in*) è già presente nel linguaggio, quindi non devi scriverla tu. Si riconosce da un nome seguito da parentesi tonde `()`.

# > **⚠️ Precisazione:** la regola "dove vedi `()` c'è una funzione" è una semplificazione utile all'inizio, ma non vale sempre. Le parentesi tonde si usano anche per raggruppare calcoli (`(2 + 3) * 4`) e per definire le tuple. Funziona bene come primo indizio, non come regola assoluta.

# **Esempi** (dal tuo appunto: da verificare quali sono stati davvero usati in aula): `print()`, `len()`, `type()`, `input()`, `float()`.

# ```python
# print("Ciao")         # mostra un testo a schermo
# len("ciao")           # restituisce 4 (la lunghezza)
# type(5)               # restituisce <class 'int'>
# ```

# > **[⚠️ LACUNA: negli appunti l'elenco delle funzioni viste in aula è marcato "DA COMPLETARE". Confermare quali sono state usate davvero.]**
# >
# > *Nota:* nella documentazione ufficiale `float` compare nella pagina delle funzioni integrate, ma tecnicamente è un tipo (una classe), non una funzione classica.

# ---

# ## 5. Le 3 capacità del programmatore

# In ordine di importanza (1 = più importante):

# 1. **Leggere il codice**
# 2. **Metodologia**
# 3. **Scrivere**

# ---

# ## 6. Esplorazione delle librerie

# **Concetto:** cercare le informazioni direttamente davanti a noi, senza uscire dall'editor. Esempio dagli appunti: scrivo `float` e ne leggo lo scopo direttamente da VS Code.

# > **[⚠️ LACUNA: non è scritto *come* si fa in VS Code (ad esempio passando il mouse sopra il nome). Non lo aggiungo finché non conferma il docente.]**

# ---

# ## 7. VS Code: le barre

# | Barra | Dove si trova | Cosa fa (secondo gli appunti) |
# |---|---|---|
# | **Verticale / laterale** | A sinistra (icone: file, ricerca, git, estensioni...) | Lavora sull'intero progetto/workspace, per cambiare ciò che influenza tutto. |
# | **Orizzontale / in alto** | In alto (menu generali) | Lavora sul singolo file/lavoro specifico. |

# > **[⚠️ DA VERIFICARE: negli appunti stessi è scritto che l'associazione "generale/specifica" è dedotta e non confermata in aula. Resta da confermare.]**
# >
# > *Nome ufficiale in VS Code:* la barra verticale a sinistra è la **Activity Bar**, quella in alto è la **menu bar**.

# ---

# ## 8. GitHub

# **Concetto (dagli appunti):** un sistema di versionamento. Immagina i salvataggi di un videogioco, ma per le versioni di un programma scritto.

# > **⚠️ Precisazione:** il sistema di versionamento vero e proprio si chiama **Git**. **GitHub** è un servizio online che ospita progetti Git e permette di collaborare. Nell'uso comune i due nomi si mescolano, ma sono cose diverse.

# **Perché lo usiamo** (ricavato dalla sezione domande dei tuoi appunti):
# - tenere traccia delle modifiche nel tempo
# - poter tornare a una versione precedente se qualcosa si rompe
# - lavorare in team senza sovrascrivere il lavoro degli altri

# ---

# ## 9. Le liste (collezioni)

# **Concetto:** le 4 caratteristiche delle collezioni, nel contesto delle liste.

# | Caratteristica | Dagli appunti |
# |---|---|
# | **Tipo** | È di tipo `list` |
# | **Elementi** | Possono essere misti: numeri, stringhe, booleani |
# | **Definizione** | Si definiscono con le parentesi quadre `[]` |
# | **Ordinamento** | "Sono ordinabili e modificabili" |

# **Sintassi:**

# ```python
# lista = [10, "ciao", True]   # elementi di tipo diverso
# print(type(lista))           # <class 'list'>
# ```

# > **⚠️ Precisazione:** in Python si dice che la lista è *ordinata* (gli elementi mantengono la posizione e si accede con l'indice) e *mutabile* (si può modificare dopo la creazione). "Ordinabili" potrebbe voler dire anche "si possono mettere in ordine" (ad esempio con `sort()`), che è un'altra cosa. Chiedi quale dei due significati intendesse il docente.

# **La peculiarità delle liste: i metodi.**

# > **[⚠️ LACUNA: i metodi sono indicati come la peculiarità delle liste, ma non ne è elencato nemmeno uno.]**
# >
# > **[⚠️ LACUNA: la frase "lo dimostriamo tramite la definizione di singoli elementi che normalmente non si potrebbe, e di definire i singoli metodi specifici" è incompleta e poco chiara. Non so a cosa si riferisca, quindi non la interpreto.]**

# ---

# ## 10. I controllori del flusso

# **Concetto:** sono gli elementi che ci dicono *come vengono lette le righe* del programma.

# Le famiglie citate sono:
# - la famiglia delle **condizioni**
# - la famiglia dei **cicli**
# - la famiglia dei ...

# > **[⚠️ LACUNA: la frase si interrompe e la terza famiglia non è indicata. Mancano anche esempi e sintassi di condizioni e cicli.]**

# ---

# ## ❓ Domande da preparare per la lezione di oggi

# | Domanda | Risposta in sintesi |
# |---|---|
# | Cos'è una funzione integrata, come la riconosco, quali abbiamo visto? | Già presente nel linguaggio, riconoscibile da `nome()`. Esempi da confermare (vedi sez. 4). |
# | Le 3 capacità del programmatore? | Leggere il codice, metodologia, scrivere. |
# | Spiegami VS Code: barra orizzontale e verticale | Vedi sez. 7, associazione ancora da verificare. |
# | Cos'è l'indentazione? | Lo spazio a sinistra del codice che definisce i blocchi; se è sbagliata il codice si rompe. |
# | Cos'è Python, una caratteristica alla volta? | Vedi sez. 1, con la correzione su "convertito in C". |
# | Cos'è GitHub e perché lo usiamo? | Vedi sez. 8, con la precisazione Git/GitHub. |

# ---

# ## ✅ Riepilogo di correzioni e lacune

# **Da correggere:**
# 1. Python non viene "convertito in C": è scritto in C e il codice passa per il bytecode.
# 2. Le virgole in Python contano molto; solo il punto e virgola è quasi irrilevante.
# 3. "Sistema di versionamento" è Git; GitHub è la piattaforma che lo ospita.
# 4. "Ordinabili" per le liste: meglio *ordinate* e *mutabili*.

# **Lacune da colmare:**
# - Le 3 regole OOP mancanti (ne servono 7, ne hai 4) e il significato di ciascuna
# - Funzioni integrate effettivamente usate in aula
# - Come si leggono le informazioni di una funzione in VS Code
# - Conferma sul ruolo delle due barre di VS Code
# - Metodi delle liste e la frase poco chiara sulla "definizione di singoli elementi"
# - La terza famiglia dei controllori del flusso, con esempi di sintassi

# Quando vuoi, incolla il prossimo blocco di appunti.