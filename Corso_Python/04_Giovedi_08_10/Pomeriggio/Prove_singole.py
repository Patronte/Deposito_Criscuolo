'''
listaN=[1,2,3,4,5,6,7,8,9]

for n in listaN:
    if n % 2 != 0:
        print(n)
        '''
        
        



#funzione   5. Utilizza un ciclo per determinare se un numero è pari. La funzione deve restituire True se il numero è pari, altrimenti False.
# se non voglio usare il numero primo uso il pari o dispari se faccio pari e dispari mi servono due funzioni
 

     
chiedoN = int(input("Inserisci un numero, ti dico se è pari o dispari: ")) 


def pari_dispari (chiedoN):
    if chiedoN % 2==0:
        print("Il nummero è Pari")
    else:
        print("Il numero è dispari")
        
pari_dispari(chiedoN) 
if chiedoN % 2==0:
    chiedoN=True
else:
    chiedoN=False 
    

