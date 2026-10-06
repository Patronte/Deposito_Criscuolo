""" eta = int(input("Quanti anni hai?"))

if eta >= 18:
    eta="MAGGIORENNE"
else: 
    eta="MINORENNE"
    
#controllo eta
match eta:
    case "MAGGIORENNE" :
        print("Puoi vedere il film")
    case "MINORENNE" :
        print("Non puoi vedere questo film")
    case _:
        print("Errore sconosciuto, riprova")
        
         """
         
listaUtenti = []

selezioneNome = input("Inserisci il tuo nome ")
listaUtenti.append(selezioneNome)

selezioneEta = int(input("Inserisci la tua eta "))
listaUtenti.append(selezioneEta)

selezioneSesso = input("Sei Maschio/Femmina? ")
listaUtenti.append(selezioneSesso[0])

selezionePremium = bool(input("Sei un utente premium? SI/NO "))
if selezionePremium == "SI": selezionePremium = True
else: selezionePremium = False
listaUtenti.append(selezionePremium)
print(listaUtenti)