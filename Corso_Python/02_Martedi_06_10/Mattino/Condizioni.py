'''Abbiamo due tipi di controllo del flusso,
Ripetitivo, ed Esclusivo
All'interno della famiglia Esclusivo delle condizioni abbiamo l'if, l'esle, e il match
La famiglia Ripetitiva si chiama Cicli/Iterazioni, servono a ripetere un blocco di codice finché qualcosa è True, Come famiglie all'interno abbiamo solo il FOR ed il WHILE 
Controllo del flusso è la capacità di alterare ciò che viene letto in esecuzione del codice, escludendo o ripetendo'''

#IF primo esempio di indentazione (intrinseca all'if) e proprietarietà)
x = 1
if x > 9:
    print("Eccellente")
    #Else aggiunge un altrimenti alla condizione
else:
    print("Sub-Eccellente")    
    
#ELIF può stare solo dopo l'IF e mai dopo l'ELSE, se ne possono avere infiniti, ma sempre un solo IF ed un ELSE
if x > 0:
    print("va bene e' maggiore di 0")
elif x > 10:
    print("UAU è maggiore di 10")
elif x == 1:
    print("wa è popio uguale")
else:
    print("niente chicco")
        
    #IF (annidati)DENTRO L'IF
    
if x > 0 : 
    print("Il numero è positivo")
    if x == 100:
        print("wow è popio 100")
else:
    print("Il numero è zero")