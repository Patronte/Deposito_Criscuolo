""" #importo neighborsclassifier dalla libreria sklearn.neighbors
from sklearn.neighbors import KNeighborsClassifier

#creo il dataset di X e y
X=[
    [3.5,23.0] ,[4.0,25.0],[5.2,24.0],[4.5,26.0], #Gatti
    [12.0,45.0],[25.0,55.0],[8.0,38.0],[30.0,60.0] #Cani
   ]

y= ["Gatto","Gatto","Gatto","Gatto","Cane","Cane","Cane","Cane"]

#inizializzazione modello
modello = KNeighborsClassifier(n_neighbors=3)   # 1) istanza con iperparametro
#addestramento 
modello.fit(X, y)                               # 2) addestramento

print("Le classi sono: " , modello.classes_) 
#nuovi dati in formato lista 
print(modello.predict([[3.8,22.0],[20.0,50.0]]))  
 """


""" from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

X,y=load_breast_cancer(return_X_y=True) 
X_train, X_test, y_train, y_test= train_test_split(X,y,test_size=0.25, random_state=0)

modello=KNeighborsClassifier(n_neighbors=3)
modello.fit(X_train,y_train)
y_pred=modello.predict(X_test)

print("Accuracy_score: ",accuracy_score(y_test,y_pred))
print("Score: " , modello.score(X_test,y_test))
print("Le classi sono: " , modello.classes_) 
print("NFeatures: ", modello.n_features_in_) """




"""
# Obiettivo: su `load_digits()` confronta `KNeighborsClassifier`, `DecisionTreeClassifier` e `RandomForestClassifier`
# con un ciclo. Poi ripeti il confronto con tre valori diversi di `random_state` nello split e stampa una tabella (DataFrame pandas)
# con modello × random_state. La classifica dei modelli cambia?

## Scrivi qui la tua soluzione
from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import pandas as pd

X, y = load_digits(return_X_y=True)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=0)   

modelli = {                                         
    "KNN": KNeighborsClassifier(n_neighbors=3),
    "Albero": DecisionTreeClassifier(random_state=0),
    "Foresta": RandomForestClassifier(random_state=0),
}

random_states = [12, 40, 81]
risultati = {
    "KNN": {},
    "Albero": {},
    "Foresta": {}
}

for rs in random_states:
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=rs
    )
    
    for nome, modello in modelli.items():
        modello.fit(X_train, y_train)
        y_pred = modello.predict(X_test)
        acc = accuracy_score(y_test, y_pred)

        risultati[nome][rs] = acc
        
df = pd.DataFrame(risultati)
print(df)

for rs in random_states:
    print("\nRandom state:", rs)
    print(df.loc[rs].sort_values(ascending=False))
    """
    
    #-----------------------------
    
""" from sklearn.datasets import load_digits
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

X, y = load_digits(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

modello=KNeighborsClassifier(n_neighbors=1)
modello.fit(X_train,y_train)

accuratezza_training=modello.score(X_train,y_train)
accuratezza_test= modello.score(X_test,y_test)

print(accuratezza_training)
print(accuratezza_test) """

#---------------------------------------

### Medio
# Obiettivo: su `make_circles(n_samples=500, noise=0.25, factor=0.5, random_state=0)`
# crea una divisione 60/20/20 in training/validation/test, scegli il miglior k tra 1 e 50 
# sul validation set e riporta l'accuratezza finale sul test.

from sklearn.datasets import make_circles
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split 

X,y= make_circles(n_samples=500, noise=0.25, factor=0.5, random_state=0)

# 1° split: 80% (train+validation) / 20% test
X_temp, X_test, y_temp, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# 2° split: dal restante 80%, il 25% va in validation -> 60/20/20 sul totale
X_train, X_val, y_train, y_val = train_test_split(X_temp, y_temp, test_size=0.25, random_state=42)


miglior_k=0

miglior_score=0

for k in range(1,51,2):
    
    modello= KNeighborsClassifier(n_neighbors=k)
    
    modello.fit(X_train,y_train)
    
    score_val=modello.score(X_val,y_val)
    
    if score_val>miglior_score:
        
        miglior_score=score_val
        
        miglior_k=k
        
miglior_modello=KNeighborsClassifier(n_neighbors=miglior_k)

miglior_modello.fit(X_train,y_train)

accuratezza_test= miglior_modello.score(X_test,y_test)
print("Miglior K trovato: ", miglior_k)
print("Accuratezza finale sul Test Set: " ,accuratezza_test)

# Stampa a schermo la precisione finale ottenuta sul Test Set 
print("Accuratezza finale sul Test Set: ", accuratezza_test)

#----------------------------------------------------
