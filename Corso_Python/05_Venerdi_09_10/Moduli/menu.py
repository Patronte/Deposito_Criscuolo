import utility as ut


while True:
   
    print("1 Somma")
    print("2 Sottrazione")
    print("3 Moltiplicazione")
    print("4 Divisione")
    print("5 Esci")
    scelta = int(input("seleziona un'operazione "))
    if scelta == 5:
        print("Chiusura in corso ")
        break
    
    elif scelta == 1:
        a =  int(input("Seleziona il primo numero: "))
        b = int(input("Seleziona il secondo numero: "))
        c = ut.somma(a,b)
        print(c)
        break
        
    elif scelta == 2:
        a =  int(input("Seleziona il primo numero: "))
        b = int(input("Seleziona il secondo numero: "))
        c = ut.sottrazione(a,b)
        print(c)
        break       
    elif scelta == 3:
        a =  int(input("Seleziona il primo numero: "))
        b = int(input("Seleziona il secondo numero: "))
        c = ut.moltiplicazione(a,b)
        print(c)
        break
    
    elif scelta == 4:
        a =  int(input("Seleziona il primo numero: "))
        b = int(input("Seleziona il secondo numero: "))
        c = ut.divisione(a,b)
        print(c)
        break
    
    else:
        print("Scelta non valida")