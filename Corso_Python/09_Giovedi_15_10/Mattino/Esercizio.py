# • ESERCIZIO - Gestione produzione di una fabbrica
# Scrivi un programma in che simula una piccola gestione della produzione di una fabbrica.
# La fabbrica produce pezzi e il programma deve permettere all'utente di registrare i prodotti realizzati durante la giornata.
# Ogni prodotto sarà rappresentato solo dal nome del prodotto e dalla quantità prodotta.
# Il programma deve mostrare un menu continuo che si ripete fino a quando l'utente decide di uscire.
# • Menu richiesto
# 1 - Aggiungi prodotto
# 2 - Visualizza produzione
# 3 - Cerca prodotto
# 4 - Modifica quantità
# 5 - Rimuovi prodotto
# 6 - Calcola totale pezzi prodotti
# 7 - Esci


#Creo la classe fabbrica        
class Fabbrica:
    #al costruttore do self, e a self assegno un dizionario
    def __init__(self):
        
        self.inventario={}
    #creo la funzione aggiungi prodotto, con parametri self, nome e quantità  
    def aggiungi_prodotto(self, nome, quantita):
        
        #ciclo if se il nome è già presente in inventario, somma la quantità
        if nome in self.inventario:
        
            self.inventario[nome]+=quantita
        #altrimenti sostituisci il valore di quantità
        
        else:
        
            self.inventario[nome]=quantita
    #funzione visualizza i prod   
    def visualizza_produzione(self):
        #ciclo for, per ogni prodotto in inventario,
        for prodotto in self.inventario:
        #printami il prodotto, quantità e la stringa pezzi
            print(f"{prodotto}: {self.inventario[prodotto]} pezzi")
    
    def cerca_prodotto():
        
        pass
    
    def  Modifica_quantità():
        
        pass
    
    def Rimuovi_prodotto():
        
        pass
    
    def Calcola_totale_pezzi_prodotti():
        
        pass
    
    def Esci():
        
        pass

#creo OBJ fabbrica1
Fabbrica1=Fabbrica()
#uso la funzione agg prod, con parametri del dizionario nome, quantita
Fabbrica1.aggiungi_prodotto("Vite", 20)
Fabbrica1.aggiungi_prodotto("Bullone", 50)
Fabbrica1.aggiungi_prodotto("Bullone", 20)
#chiamo la funzione di visualizza, mi restituisce l'intero inventario
Fabbrica1.visualizza_produzione()










'''
def main():
    oggetti = []
    scelta = -1

    while scelta != 0:
        print("--- MENU ---")
        print("1. Avviare il menu")
        print("2. Aggiungere oggetto")
        print("3. Rimuovere un oggetto")
        print("0. Uscire dal menu")
        
        scelta_str = input("Scegli un'opzione: ")
        
        if scelta_str.isdigit():
            scelta = int(scelta_str)
            
            if scelta == 1:
                # Esempio di codice utilizzabile qui dentro:
                # print("Elementi attualmente in memoria:", oggetti)
                # print("Totale oggetti:", len(oggetti))
                print("Menu avviato correttamente!\n")
            elif scelta == 2:
                # Esempio di codice utilizzabile qui dentro:
                # nuovo_item = "Pozione Magica"
                # oggetti.append(nuovo_item)
                # print(f"Aggiunto automaticamente: {nuovo_item}")
                oggetto_aggiunto = input("Inserisci il nome dell'oggetto da aggiungere: ")
                oggetti.append(oggetto_aggiunto)
                print(f"Oggetto '{oggetto_aggiunto}' aggiunto.\n")
            elif scelta == 3:
                # Esempio di codice utilizzabile qui dentro:
                # target = "Spada di Legno"
                # if target in oggetti:
                #     oggetti.remove(target)
                #     print(f"Rimosso l'oggetto predefinito: {target}")
                oggetto_rimosso = input("Inserisci il nome dell'oggetto da rimuovere: ")
                if oggetto_rimosso in oggetti:
                    oggetti.remove(oggetto_rimosso)
                    print(f"Oggetto '{oggetto_rimosso}' rimosso.\n")
                else:
                    print("Oggetto non trovato nella lista.\n")
            elif scelta == 0:
                # Esempio di codice utilizzabile qui dentro:
                # file_output = open("dati.txt", "w")
                # file_output.write(str(oggetti))
                # file_output.close()
                print("Uscita dal programma in corso...")
            else:
                print("Opzione non valida. Riprova.\n")
        else:
            print("Inserisci un numero valido.\n")

if __name__ == "__main__":
    main()

'''
