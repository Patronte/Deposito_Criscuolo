# Medio

# Obiettivo: crea un DataFrame di 6 auto usate con colonne km, anni, cilindrata, prezzo, incidentata (sì/no). Ricava X e y per due domande diverse: "quanto costerà?" e "è stata incidentata?". Stampa la shape di X e y in entrambi i casi e indica il tipo di problema.

import pandas as pd

auto = pd.DataFrame({
    "km":           [120_000, 45_000, 80_000, 150_000, 30_000, 95_000],
    "anni":             [10,3,6,12,2,7],
    "cilindrata":       [1600,1400,200,1600,1200,1800],
    "prezzo":       [4_500, 13_000, 9_000, 3_000, 15_000, 8_000],
    "incidentata":  ["sì", "no", "no", "sì", "no", "sì"],
})
feature = ["km", "anni", "cilindrata"]

# Domanda 1: "quanto costerà?" -> REGRESSIONE (prezzo numerico)
X_prezzo, y_prezzo = auto[feature], auto["prezzo"]
print("Prezzo:      X", X_prezzo.shape, "y", y_prezzo.shape)

# Domanda 2: "è stata incidentata?" -> CLASSIFICAZIONE (sì/no)
X_inc, y_inc = auto[feature], auto["incidentata"]
print("Incidentata: X", X_inc.shape, "y", y_inc.shape)


# Prezzo:      X (6, 3) y (6,)
# Incidentata: X (6, 3) y (6,)





-------------------

Obiettivo: carica load_wine() e load_diabetes(). Per ciascuno scrivi codice che stampi numero di campioni, numero di feature, e decida automaticamente se il problema è di classificazione o di regressione analizzando y (suggerimento: quanti valori unici contiene? sono interi o decimali?).


import numpy as np
from sklearn.datasets import load_wine, load_diabetes

def tipo_problema(y):
    valori = np.unique(y)
    # Pochi valori interi -> classi; altrimenti -> numero continuo.
    # Si conta il numero di valori unici: il tipo float non basta,
    # perché il target di load_diabetes() contiene interi salvati come float.
    if len(valori) <= 20 and np.all(valori == valori.astype(int)):
        return "classificazione"
    return "regressione"

for nome, loader in [("wine", load_wine), ("diabetes", load_diabetes)]:
    d = loader()
    n_campioni, n_feature = d.data.shape
    print(f"{nome}: campioni={n_campioni}, feature={n_feature}, "
          f"valori unici di y={len(np.unique(d.target))}, "
          f"problema={tipo_problema(d.target)}")


wine: campioni=178, feature=13, valori unici di y=3, problema=classificazione
diabetes: campioni=442, feature=10, valori unici di y=214, problema=regressione
