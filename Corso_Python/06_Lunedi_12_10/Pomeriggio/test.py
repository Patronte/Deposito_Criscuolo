class Moltiplicatore:
    def __init__(self,numero):
        self.numero=numero
    def __call__ (self, valore):
        return valore * self.numero

doppio=Moltiplicatore(2)

print(doppio(10))