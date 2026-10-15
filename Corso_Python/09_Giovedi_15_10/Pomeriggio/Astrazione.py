#la libreria abc è un meccanismo per definire classi astratte 
#va fatto ogni volta che usi metodi astratti
from abc import ABC, abstractmethod
#stiamo importando una classe(ABC) e un decoratore(abstractmethod)

#il padre non può diventare un oggetto, serve solo per creare i figli, 
# già prima potevo fare figli ma non potevo obbligarli ad ereditare un metodo
class Pippo_Astratto(ABC):
    
   @abstractmethod #ti permette di lasciare metodi vuoti e costringere i figli a sovrascriverli
   def Metodo_obbligatorio(self):
       pass
   
class Pippo_reale(Pippo_Astratto):
    
    pass
#il figlio dovrà quindi andare a prendere il metodo_obbligatorio, modificarlo, e solo allora potrà diventare un oggetto, prima di fare ciò se crei un oggetto, non te lo crea
#non si può creare, è la classe padre
P_a=Pippo_Astratto()
#non si può creare, non hai ereditato al figlio il metodo_obbligatorio
P_a=Pippo_reale()
#dichiari al figlio il metodo del padre
class Pippo_reale(Pippo_Astratto):
    def Metodo_obbligatorio(self):
        pass

#si può creare l'oggetto, perchè hai ereditato il metodo obb
P_a=Pippo_reale()

#ogni metodo astratto deve essere implementato nella classe figlio altrimenti non funzionerà
#l'astrazione può contenere anche 