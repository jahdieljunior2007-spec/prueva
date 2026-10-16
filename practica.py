from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def hacer_ruido(self):
        pass

class Perro(Animal):
    def hacer_ruido(self):
        print("guau guau")
    
class Gato(Animal):
    def hacer_ruido(self):
        print("miau miau")
    
perro = Perro()
gato = Gato()

perro.hacer_ruido()
gato.hacer_ruido()