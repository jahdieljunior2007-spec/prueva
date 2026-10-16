from abc import ABC, abstractmethod

class Pagable(ABC):
    @abstractmethod
    def valor(self,valor):
        pass

class Nequi(Pagable):
    def valor(self,valor):
        print(f"se pago con nequi {valor}")
        pass

class Targeta(Pagable):
    def valor(self,valor):
        print(f"se pago con targeta {valor}")
        pass

targeta = Targeta()
nequi = Nequi()

targeta.valor(10000)
nequi.valor(30000)



        