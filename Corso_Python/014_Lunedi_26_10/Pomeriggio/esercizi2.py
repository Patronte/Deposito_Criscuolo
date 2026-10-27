import matplotlib.pyplot as plt
import numpy as np
from sklearn.datasets import load_digits

# 1. Carica il dataset load_digits()
digits = load_digits()

# 2. Stampa la forma di X (i dati delle feature)
X = digits.data
print("Forma di X:", X.shape)

# 3. Visualizza le prime 10 immagini con la cifra corretta come titolo
for i in range(10):
    plt.figure(figsize=(1.5, 1.5)) # Crea una figura per l'immagine
    plt.imshow(digits.images[i], cmap="gray") # Mostra l'immagine in scala di grigi
    plt.title(f"Cifra: {digits.target[i]}") # Aggiunge il titolo con il target reale
    plt.axis('off') # Nasconde i bordi/assi del grafico
    plt.show() # Mostra a schermo

# 4. Crea un grafico a barre con il numero di campioni per ciascuna cifra
cifre, conteggi = np.unique(digits.target, return_counts=True)

plt.figure(figsize=(7, 4))
plt.bar(cifre, conteggi, color="teal", alpha=0.7)
plt.xticks(cifre)
plt.xlabel("Cifra (Target)")
plt.ylabel("Numero di Campioni")
plt.title("Numero di campioni per ciascuna cifra")
plt.show()
