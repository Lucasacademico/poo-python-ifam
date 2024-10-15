# Definindo a classe
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca  # atributo de instância
        self.modelo = modelo
        self.ano = ano

    def descrever(self):  # método da classe
        return f"{self.ano} {self.marca} {self.modelo}"

# Criando um objeto da classe Carro
meu_carro = Carro("Toyota", "Corolla", 2020)

# Usando um método do objeto
print(meu_carro.descrever())  # Saída: 2020 Toyota Corolla
