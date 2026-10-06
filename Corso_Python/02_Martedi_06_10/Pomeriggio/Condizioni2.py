#match è l'esecuzione di un'uguaglianza su più casi
#match ha senso in un menù, si usa sempre con le stringhe, se voglio usare altre variabili ho l'if in genere

comando = input("Inserisci un comando: ")

match comando:
    case "start":
        print("Avvio del programma.")
    case "stop":
        print("Chiusura del programma.")
    case "pausa":
        print("Programma in pausa.")
    case _:
        print("Comando non riconosciuto.")
        
        