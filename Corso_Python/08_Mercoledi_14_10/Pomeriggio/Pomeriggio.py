#La simulazione di overloading è uno dei tanti modi che possiamo usare per sfruttare il polimorfismo a nostro vanaggio perché

#se passiamo i valori alla funzione, cambierà il modo in cui si comporta la funzione 

#Il polimorfismo passivo esiste a prescindere di ciò che facciamo, si basa sul concetto di duck typing 
#se io ho l'oggetto papera e poi ho l'oggetto macchina
#ma sia macchina che papera(non imparentate) camminano come una papera, hanno i metodi della papera, basta che l'oggetto si comporti come una papera, 
#(possegga i metodi e attributi necessari) per dire che qualsiasi oggetto funzioni come una papera 

#la funzione che richiama gli oggetti, non può essere dentro uno degli oggetti che richiama il metodo al suo interno, deve essere all'esterno di essi

#Duck TYPING 


# Funzione built-in len()

# len accetta tutto, liste oggetti dizionari, perché usa il polimorfismo
# non importa che elemento mi mandi, se ha la lunghezza (+ elementi dentro se stesso) io ti risponderò con la lunghezza

