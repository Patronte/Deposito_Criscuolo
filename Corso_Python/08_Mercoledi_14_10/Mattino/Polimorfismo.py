#stamane è stato fatto recap incapsulamento introduzione a polimorfismo e  vari esercizi in merito
#è la CAPACITA' di far si che se un elemento cambia comportamento o logica, (mod in cui si utilizza o lo chiamiamo) , senza che ciò che lui rappresenta per il sistema non cambia
#noi possiamo solo scegliere di sfruttarlo o subirlo 

# # SLIDE 170 a 158

# ## Incapsulamento

# ### Concetto
# L'**incapsulamento** (in inglese *encapsulation*) consiste nel nascondere i dettagli interni di una **classe** (un modello per creare oggetti) ed esporre all'esterno solo ciò che serve. Analogia: quando guidi un'auto usi volante e pedali, senza toccare direttamente il motore.

# In Python non esistono le parole chiave `private` o `protected` che si trovano in linguaggi come Java o C++. Python usa invece una **convenzione**, basata sul trattino basso (`_`) e sul doppio trattino basso (`__`).

# Strumenti dell'incapsulamento secondo la pagina:
# - **Attributi privati** (`__attributo`): non dovrebbero essere accessibili dall'esterno della classe.
# - **Attributi protetti** (`_attributo`): dovrebbero essere usati solo dentro la classe e le sue sottoclassi.
# - **Metodi getter e setter**: metodi per leggere (*get*) e modificare (*set*) gli attributi privati, con più controllo sui dati.

# **[⚠️ DIFFERENZA: la pagina "Metodi dell'Incapsulamento" dice che un attributo privato "non può essere accesso direttamente dall'esterno". Un'altra pagina (Privati) dice correttamente che il meccanismo non impedisce l'accesso. La documentazione ufficiale conferma la seconda: i membri "privati" non esistono davvero in Python, c'è solo il *name mangling*.]**

# ### Sintassi
# ```python
# self.__attributo      # privato (doppio underscore)
# self._attributo       # protetto (singolo underscore, solo convenzione)

# def get_attributo(self):          # getter
#     return self.__attributo

# def set_attributo(self, valore):  # setter
#     self.__attributo = valore
# ```
# - `self.__attributo`: l'attributo privato, salvato nell'oggetto.
# - `get_...`: restituisce il valore.
# - `set_...`: assegna un nuovo valore (qui si possono aggiungere controlli).

# ### Esempio Pratico
# ```python
# class Computer:
#     def __init__(self, nome_proc):
#         self.__processore = nome_proc # Attributo privato

#     def get_processore(self):
#         return self.__processore

#     def set_processore(self, processore):
#         self.__processore = processore

# pc = Computer("Intel i5")
# print(pc.get_processore())
# # Accede all'attributo privato tramite il getter
# pc.set_processore("AMD Ryzen 5")
# # Modifica l'attributo privato tramite il setter
# print(pc.get_processore())
# ```
# Spiegazione:
# - `class Computer:` definisce la classe.
# - `__init__` è il **costruttore** (metodo che si esegue alla creazione dell'oggetto): salva il nome del processore nell'attributo privato `__processore`.
# - `get_processore` restituisce il valore dell'attributo.
# - `set_processore` lo sostituisce con un nuovo valore.
# - `pc = Computer("Intel i5")` crea l'oggetto.
# - Il primo `print` mostra il processore iniziale, poi il setter lo cambia e il secondo `print` mostra il nuovo valore.

# Output atteso:
# ```
# Intel i5
# AMD Ryzen 5
# ```

# ---

# ## Livelli di visibilità delle variabili (scope)

# ### Concetto
# Lo **scope** (ambito) stabilisce in quali parti del codice una variabile è visibile e utilizzabile. I livelli sono tre:
# - **Globale**: dichiarata fuori da tutte le funzioni, accessibile da qualsiasi punto del modulo (anche dentro le funzioni), a meno che sia oscurata da una variabile locale con lo stesso nome.
# - **Locale**: dichiarata dentro una funzione, visibile solo lì.
# - **Non-locale** (con `nonlocal`): serve nelle **funzioni annidate** (una funzione dentro un'altra) per riferirsi a una variabile della funzione esterna, che non è globale.

# **[⚠️ LACUNA: la pagina dice che il livello non-locale serve quando una variabile "deve essere accessibile in più di una funzione interna". Non spiega che `nonlocal` serve soprattutto per *modificare* la variabile della funzione esterna: senza `nonlocal`, un'assegnazione crea una nuova variabile locale. Inoltre non viene mostrata la parola chiave `global`, che serve per modificare una variabile globale da dentro una funzione.]**

# ### Sintassi
# ```python
# nonlocal nome_variabile
# ```
# - `nonlocal`: parola chiave che dice "usa la variabile con questo nome della funzione esterna più vicina".
# - `nome_variabile`: deve già esistere in una funzione che racchiude quella corrente.

# ### Esempio Pratico
# ```python
# # Variabile globale
# numero = 10

# def funzione_esterna():
#     # Variabile locale nella funzione esterna
#     numero = 5
#     print("Numero dentro funzione_esterna (locale):", numero)

#     def funzione_interna():
#         # Utilizzo nonlocal per modificare la variabile locale della funzione esterna
#         nonlocal numero
#         numero = 3
#         print("Numero dentro funzione_interna (nonlocal):", numero)

#     funzione_interna()

# print("Numero nel main (globale):", numero)
# funzione_esterna()
# print("Numero nel main dopo chiamata (globale non cambiato):", numero)
# ```
# Spiegazione:
# - `numero = 10`: variabile globale.
# - `def funzione_esterna():` definisce la funzione esterna.
# - `numero = 5`: variabile locale della funzione esterna, distinta da quella globale.
# - Il `print` successivo mostra 5.
# - `def funzione_interna():` definisce una funzione annidata.
# - `nonlocal numero`: indica che `numero` è quello della funzione esterna.
# - `numero = 3`: modifica la variabile della funzione esterna (non crea una nuova variabile).
# - Il `print` interno mostra 3.
# - `funzione_interna()` esegue la funzione interna.
# - Il primo `print` esterno mostra la globale (10).
# - `funzione_esterna()` viene eseguita.
# - L'ultimo `print` mostra che la globale è ancora 10.

# Output atteso:
# ```
# Numero nel main (globale): 10
# Numero dentro funzione_esterna (locale): 5
# Numero dentro funzione_interna (nonlocal): 3
# Numero nel main dopo chiamata (globale non cambiato): 10
# ```

# ---

# ## Attributi e metodi privati (name mangling)

# ### Concetto
# Le variabili e i metodi privati si definiscono con due trattini bassi (`__`) all'inizio del nome. Python attiva il **name mangling** (alterazione del nome): internamente il nome viene trasformato includendo il nome della classe, così è meno accessibile da fuori. Questo **non impedisce** l'accesso, ma segnala che non va usato dall'esterno.

# ### Sintassi
# ```python
# self.__nome          # attributo privato
# def __metodo(self):  # metodo privato
# ```
# Dall'esterno il nome diventa `_NomeClasse__nome`.

# ### Esempio Pratico
# ```python
# class MiaClasse:
#     def __init__(self):
#         self.__variabile_privata = "Sono privata"

#     def __metodo_privato(self):
#         return "Questo è un metodo privato"

# obj = MiaClasse()
# # Stampando direttamente la variabile privata solleverà un'eccezione
# # print(obj.__variabile_privata)  # AttributeError
# # L'accesso corretto (che dovrebbe essere evitato) sarebbe:
# print(obj._MiaClasse__variabile_privata)  # Funzionerà, ma non è buona prassi
# ```
# Spiegazione:
# - La classe ha un attributo privato e un metodo privato.
# - `obj = MiaClasse()` crea l'oggetto.
# - La riga commentata `print(obj.__variabile_privata)` darebbe `AttributeError`, perché il nome reale è stato alterato.
# - `obj._MiaClasse__variabile_privata` usa il nome alterato e funziona, ma è sconsigliato.

# Output atteso:
# ```
# Sono privata
# ```

# **[⚠️ LACUNA: la riga 12 della pagina è tagliata nello screenshot ("non è buona prassi"): il commento è stato completato in base al senso, ma controlla il testo originale.]**

# ---

# ## Attributi e metodi protetti

# ### Concetto
# Si indicano con **un solo trattino basso** (`_`) all'inizio del nome. È meno restrittivo del doppio trattino e funziona come **suggerimento** per gli sviluppatori: il membro andrebbe usato solo dentro la classe e nelle sue **sottoclassi** (classi che ereditano da un'altra). Non esistono meccanismi tecnici che impediscano l'accesso da fuori.

# ### Sintassi
# ```python
# self._nome          # attributo protetto
# def _metodo(self):  # metodo protetto
# ```

# ### Esempio Pratico
# ```python
# class ClasseBase:
#     def __init__(self):
#         self._variabile_protetta = "Sono protetta"

# class SottoClasse(ClasseBase):
#     def __init__(self):
#         super().__init__()
#         print(self._variabile_protetta)  # Accesso consentito

# obj = SottoClasse()
# # Accesso da fuori la classe (non consigliato, ma possibile)
# print(obj._variabile_protetta)
# ```
# Spiegazione:
# - `ClasseBase` crea l'attributo protetto `_variabile_protetta`.
# - `SottoClasse(ClasseBase)` eredita da `ClasseBase`.
# - `super().__init__()` chiama il costruttore della classe base, così l'attributo viene creato.
# - Il `print` interno lo legge (uso previsto).
# - `obj = SottoClasse()` crea l'oggetto, quindi stampa la prima volta.
# - L'ultimo `print` lo legge da fuori: funziona, ma è sconsigliato.

# Output atteso:
# ```
# Sono protetta
# Sono protetta
# ```

# **[⚠️ LACUNA: la pagina non spiega cosa sia `super()`, che compare nell'esempio.]**

# ---

# ## Property

# ### Concetto
# Una **property** permette di controllare l'accesso agli attributi di una classe: si legge e si scrive come un normale attributo, ma dietro le quinte vengono eseguiti metodi che possono fare controlli. Un **decoratore** (riga che inizia con `@`, posta sopra una funzione per modificarne il comportamento) definisce i tre metodi:
# - `@property`: definisce il **getter**, per leggere il valore come se fosse un normale attributo.
# - `@nome_property.setter`: definisce il **setter**, che controlla come viene modificato il valore (utile per validazioni).
# - `@nome_property.deleter`: definisce cosa succede quando si elimina la property con `del` (può liberare risorse o bloccare l'eliminazione).

# **[⚠️ LACUNA: la pagina non mostra alcun esempio per `@nome_property.deleter`.]**

# ### Sintassi
# ```python
# @property
# def nome(self):
#     return self._nome

# @nome.setter
# def nome(self, valore):
#     self._nome = valore

# @nome.deleter
# def nome(self):
#     del self._nome
# ```
# **[⚠️ LACUNA: la sintassi del deleter non è sulle pagine. Lo schema qui sopra, per il deleter, è un mio esempio generico.]**

# ### Esempio Pratico
# ```python
# class Studente:
#     def __init__(self, nome, voto):
#         self.nome = nome
#         self._voto = voto   # variabile privata (convenzione)

#     @property
#     def voto(self):
#         return self._voto

#     @voto.setter
#     def voto(self, nuovo_voto):
#         if 0 <= nuovo_voto <= 30:
#             self._voto = nuovo_voto
#         else:
#             print("Voto non valido")
# ```
# Spiegazione:
# - `__init__` salva `nome` e `_voto` (protetto per convenzione).
# - `@property` sul metodo `voto`: permette di scrivere `studente.voto` per leggere il valore.
# - `@voto.setter`: quando si scrive `studente.voto = ...` viene eseguito questo metodo.
# - Se il valore è tra 0 e 30 viene accettato, altrimenti stampa "Voto non valido".

# **[⚠️ LACUNA: lo screenshot si interrompe alla riga 15, senza codice che usi la classe, quindi manca l'output atteso. Un esempio d'uso (mio, non della pagina) sarebbe: `s = Studente("Anna", 25)`, poi `s.voto = 40` stamperebbe `Voto non valido`.]**

# **[⚠️ DIFFERENZA: il commento della pagina "variabile privata (convenzione)" riferito a `_voto` non è corretto: un solo underscore indica un attributo *protetto*, come spiegato nelle pagine precedenti.]**

# ---

# ## Polimorfismo

# ### Concetto
# Il **polimorfismo** (dal greco "molte forme") permette di trattare oggetti di classi diverse attraverso un'**interfaccia comune** (stessi nomi di metodi). In Python si manifesta soprattutto con l'**overriding** (sovrascrittura) dei metodi. Python non supporta l'**overloading** (più metodi con lo stesso nome ma parametri diversi) in senso tradizionale, ma si ottengono risultati simili con argomenti predefiniti e variadici (che accettano un numero variabile di valori).

# **[⚠️ LACUNA: la pagina non spiega cosa siano gli "argomenti variadici" (`*args`, `**kwargs`) e non ne mostra esempi.]**

# ### Sintassi
# Il polimorfismo non ha una sintassi propria: si ottiene usando lo stesso nome di metodo in classi diverse.

# **[⚠️ LACUNA: la pagina non fornisce una sintassi generale; le sintassi sono nelle sezioni seguenti.]**

# ### Esempio Pratico
# Vedi le sezioni seguenti (Overriding, Overloading, Duck typing, `len()`).

# ---

# ## Overriding dei metodi (sovrascrittura)

# ### Concetto
# L'overriding avviene quando una sottoclasse fornisce una propria implementazione di un metodo già definito nella **superclasse** (la classe da cui si eredita). Così il comportamento si specializza in base alla sottoclasse.

# ### Sintassi
# ```python
# class Sottoclasse(Superclasse):
#     def nome_metodo(self):
#         ...  # nuova implementazione
# ```
# - La sottoclasse si dichiara con la superclasse tra parentesi.
# - Il metodo ha lo **stesso nome** di quello della superclasse.

# ### Esempio Pratico
# ```python
# class Animale:
#     def emetti_suono(self):
#         print("Questo animale fa un suono")

# class Cane(Animale):
#     def emetti_suono(self):
#         print("Bau")

# class Gatto(Animale):
#     def emetti_suono(self):
#         print("Miao")
# ```
# Spiegazione:
# - `Animale` ha il metodo `emetti_suono` generico.
# - `Cane` e `Gatto` ereditano da `Animale` e sovrascrivono il metodo con il proprio suono.

# **[⚠️ LACUNA: lo screenshot finisce senza righe che usino le classi, quindi non c'è un output. Un esempio d'uso (mio, non della pagina): `Cane().emetti_suono()` stampa `Bau`; `Gatto().emetti_suono()` stampa `Miao`.]**

# ---

# ## Simulazione dell'overloading

# ### Concetto
# L'overloading (più metodi con lo stesso nome ma parametri diversi nella stessa classe) non è supportato direttamente in Python. Si può simulare con **argomenti opzionali** (con un valore predefinito) o variadici.

# ### Sintassi
# ```python
# def metodo(self, a=None, b=None):
# ```
# - `a=None, b=None`: parametri opzionali; se non vengono passati valgono `None` (cioè "nessun valore").

# ### Esempio Pratico
# ```python
# class Stampa:
#     def mostra(self, a=None, b=None):
#         if a is not None and b is not None:
#             print(a + b)
#         elif a is not None:
#             print(a)
#         else:
#             print("Niente da mostrare")
# ```
# Spiegazione:
# - Se `a` e `b` sono entrambi passati, stampa la loro somma.
# - Se è passato solo `a`, stampa `a`.
# - Se non è passato nulla, stampa "Niente da mostrare".

# **[⚠️ LACUNA: la pagina non mostra chiamate di esempio né output. Un esempio d'uso (mio): `Stampa().mostra(2, 3)` stampa `5`, `Stampa().mostra(7)` stampa `7`, `Stampa().mostra()` stampa `Niente da mostrare`.]**

# ---

# ## Polimorfismo passivo e duck typing

# ### Concetto
# Il polimorfismo passivo si basa sul **duck typing** (tipizzazione "a papera"). In Python non serve che un oggetto appartenga a una gerarchia di classi specifica o implementi un'interfaccia esplicita: basta che abbia i metodi o gli attributi necessari. Se "cammina come un anatroccolo e starnazza come un anatroccolo", può essere trattato come tale, indipendentemente dal suo tipo.

# **[⚠️ LACUNA: "polimorfismo passivo" non è un termine della documentazione ufficiale di Python, che parla di *duck typing*. Il termine "passivo" non è spiegato nella pagina.]**

# ### Sintassi
# Non c'è sintassi dedicata: si chiama lo stesso metodo su oggetti diversi.
# ```python
# oggetto.nome_metodo()
# ```

# ### Esempio Pratico
# ```python
# class Cerchio:
#     def disegna(self):
#         print("Disegno un cerchio")

# class Rettangolo:
#     def disegna(self):
#         print("Disegno un rettangolo")

# def disegna_figura(figura):
#     # Anche qui, basta che 'figura' abbia il metodo 'disegna'
#     figura.disegna()

# figure = [Cerchio(), Rettangolo()]     # figure[0]=Cerchio() / figure[1]=Rettangolo()

# # Iteriamo e disegniamo ogni figura
# for figura in figure:
#     disegna_figura(figura)
# ```
# Spiegazione:
# - `Cerchio` e `Rettangolo` sono classi **non collegate** tra loro, ma entrambe hanno `disegna()`.
# - `disegna_figura(figura)` chiama `figura.disegna()` senza controllare il tipo.
# - `figure` è una lista con un oggetto di ciascuna classe.
# - Il ciclo `for` passa ogni oggetto alla funzione.

# Output atteso:
# ```
# Disegno un cerchio
# Disegno un rettangolo
# ```

# ---

# ## Funzione built-in `len()`

# ### Concetto
# `len()` è un esempio classico di polimorfismo: funziona con tipi diversi (liste, stringhe, dizionari) purché implementino il **metodo speciale** `__len__()` (metodo con doppio underscore che Python chiama automaticamente).

# **[⚠️ LACUNA: la pagina non mostra come implementare `__len__()` in una classe propria.]**

# ### Sintassi
# ```python
# len(oggetto)
# ```
# - `oggetto`: lista, stringa, dizionario o qualsiasi oggetto con `__len__()`.
# - Restituisce il numero di elementi.

# ### Esempio Pratico
# ```python
# # Lista
# print(len([1, 2, 3]))  # Output: 3

# # Stringa
# print(len("Ciao"))     # Output: 4

# # Dizionario
# print(len({"a": 1, "b": 2}))  # Output: 2
# ```
# Spiegazione:
# - Lista: 3 elementi.
# - Stringa: 4 caratteri.
# - Dizionario: 2 coppie chiave-valore.

# Output atteso:
# ```
# 3
# 4
# 2
# ```

# ---

# ## `if __name__ == "__main__":`

# ### Concetto
# Questa condizione verifica se il file viene eseguito **direttamente** (e non importato da un altro script). Se è vera, il blocco al suo interno viene eseguito. È una convenzione comune per distinguere il codice eseguibile direttamente da quello importato come **modulo** (un file Python riutilizzabile da altri file).

# **[⚠️ LACUNA: la pagina non spiega cosa sia `__name__`: una variabile speciale che vale `"__main__"` quando il file è eseguito direttamente, altrimenti il nome del modulo. Questa spiegazione viene dalla documentazione ufficiale, non dalla pagina.]**

# ### Sintassi
# ```python
# if __name__ == "__main__":
#     # codice eseguito solo se il file è lanciato direttamente
# ```

# ### Esempio Pratico
# ```python
# if __name__ == "__main__":
#     print("main")
# else:
#     print("import")
# ```
# Spiegazione:
# - Se il file è eseguito direttamente, `__name__` vale `"__main__"` e stampa `main`.
# - Se il file è importato da un altro, entra nell'`else` e stampa `import`.

# Output atteso (file eseguito direttamente):
# ```
# main
# ```
# Output atteso (file importato):
# ```
# import
# ```

# ---

# ## Riepilogo
# - L'incapsulamento nasconde i dettagli interni di una classe; in Python si usa la convenzione `_attributo` (protetto) e `__attributo` (privato, con name mangling), senza vera protezione.
# - Getter, setter e `@property` permettono di leggere e modificare gli attributi con controlli e validazioni.
# - Gli scope sono tre: globale, locale e non-locale (`nonlocal`, per le funzioni annidate).
# - Il polimorfismo permette di usare oggetti diversi con la stessa interfaccia: overriding, duck typing e funzioni come `len()`; l'overloading si simula con argomenti opzionali.
# - `if __name__ == "__main__":` esegue il codice solo se il file è lanciato direttamente e non importato.