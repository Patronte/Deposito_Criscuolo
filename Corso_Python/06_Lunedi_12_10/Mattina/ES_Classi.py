# Esercizio 1 (Facile):
# Crea una classe chiamata Punto.
# Questa classe dovrebbe avere:
# • Due attributi: x e y, per rappresentare le coordinate del punto nel piano.
# • Un metodo muovi che prenda in input un valore per dx e un valore per dy e modifichi le coordinate del punto di questi valori.
# • Un metodo distanza_da_origine che restituisca la distanza del punto dall'origine (0,0) del piano.







# Esercizio 2 (Facile):
# Crea una classe chiamata Libro.
# Questa classe dovrebbe avere:
# • Tre attributi: titolo, autore e pagine.
# • Un metodo descrizione che restituisca una stringa del tipo "Il libro 'titolo' è stato scritto da 'autore' e ha 'pagine' pagine.".
# Extra: permetti di creare quanti libri vuole l'utente 
'''

class Libro:
    def __init__(self, titolo, autore,pagine):
        self.titolo=titolo
        self.autore=autore
        self.pagine=pagine
    def descrizione(self):
        return("Il libro ",self.titolo ,"è stato scritto da: ", self.autore, "ed ha :", self.pagine)

Libri=[]
Libro1 = Libro("Il pianto di Mirko", "Patronte",5) 
Libro2 = Libro("Papa costoso papa non costoso","Ciarlatano",350)
Libro3 = Libro("Prosopagnosia","Caparezza",400)

while True:
    sel = input("Crea libro (c) / Vedi tutti (v) / Esci (x): ")
    
    match sel.lower():
        case 'c':
            titolo
            autore
            pagine
            Libri.append(Libro)

'''


#spiegazione
#ho definito una classe 
'''
class punto:
    pass
#sicuramente mi servirà un costruttore quindi faccio init dentro la classe

class punto:
    def  __init__(self):
        pass
    
#vogliono x e y

#quindi
class punto:
    def  __init__(self, x,y):
        self.x = x
        self.y = y

#ora mi serve muovi punti e distanza origine

class punto:
    def  __init__(self, x,y):
        self.x = x
        self.y = y
    def muovi_punti(self, dx,dy):
        self.x= dx
        self.y= dy
    def distanza_origine(self):
        return self.x, self.y
    
punto_mio = punto (x,y)
print
'''
#MIRKO CI MOSTRA L'ES LIBRO
#la creo

'''
class libro:
    def __init__(self, pagine, autore, titolo):
        self.pagine = pagine
        self.autore = autore
        self.titolo = titolo
    def stampa_libro(self):
        return self.autore, self.pagine, self.titolo

scelta = "" 
while scelta != "end":
    in1 = input("pagine?")
    in2 = input("autore?")
    in3 = input("titolo?")
    
    Obj = libro(in1,in2,in3)
    print(Obj.stampa_libro())
    scelta = input("vuoi continuare?")

'''