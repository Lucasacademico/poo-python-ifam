class Animal:
    def som(self):
        pass  # método abstrato

class Cachorro(Animal):
    def som(self):
        return "Latido"

class Gato(Animal):
    def som(self):
        return "Miau"


# Criando uma lista de animais
animais = [Cachorro(), Gato()]

for animal in animais:
    print(animal.som())  # Saída: Latido Miau
