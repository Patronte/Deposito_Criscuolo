#claude mi fa da tutor, io ripasso liste, for ,while, funzioni, e forse altro.
#test per vedere return e cosa succede se lo sostituisco con un print
'''def calcola (a, b=2):
    return(a*b) #se lo sostituisco con print(a*b), il print(x) mi stamperà none
    
x = calcola(5)
print(x)
'''
'''
##funzione per avere il quadrato di un numero
def quadrato(n):
    return n*n
#funzione per avere un giudizio in base al voto
def giudizio(voto):
    if voto >= 27:
        return("Ottimo")
    elif voto >=24 and voto < 27:
        return("Buono")
    elif voto >= 18 and voto < 24:
        return("Sufficiente")
    else:
        return("Pippo, insufficiente")
        
#funzione per calcolare il prezzo finale post sconto detratto        
def prezzo_finale(prezzo,sconto=0):
    return int(prezzo-(prezzo*sconto/100))
#stampa dei 3 esercizi sopra per vedere se il risultato atteso combacia con quello che viene portato a terminale

print(quadrato(6))
print(giudizio(25))
print(giudizio(15))
print(int(prezzo_finale(200)))
print(int(prezzo_finale(200, 10)))
'''

# #Consegna: tre funzioni
# 1. e_pari(n)
# Restituisce True se n è pari, False altrimenti. Non serve l’if: la condizione n % 2 == 0 è già un booleano.
def e_pari(na):
    return na % 2 == 0

# 2. descrivi(n)
# Restituisce una stringa, usando e_pari:
# "zero" se n == 0
# "pari" se è pari
# "dispari" negli altri casi
def descrivi(ni):
    if ni == 0:
        return "zero"
    elif ni %2==0:
        return "pari"
    else:
        return"dispari"
# Attenzione all’ordine: lo 0 è anche pari, quindi va controllato prima.

# 3. bonus(voto, lode=False)
# Restituisce voto + 3 se lode è True, altrimenti voto. Il risultato non può superare 33.
def bonus(voto, lode=False):
    
        if lode==True and voto+3 >33:
            return 33
        elif lode==True:
            return voto+3
        else:
            return voto
        
        
print(e_pari(4))
print(descrivi(0))
print(descrivi(7))
print(bonus(28))
print(bonus(28, True))
print(bonus(32, True))        
print(bonus(30, True))   # 33
print(bonus(20, True))   # 23
