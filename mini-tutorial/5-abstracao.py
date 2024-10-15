from abc import ABC, abstractmethod

class Forma(ABC):  # Forma é uma classe abstrata
    @abstractmethod
    def area(self):
        pass

class Retangulo(Forma):
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

# Não podemos instanciar Forma diretamente porque é abstrata
# forma = Forma()  # Isso gera um erro

retangulo = Retangulo(10, 20)
print(retangulo.area())  # Saída: 200
