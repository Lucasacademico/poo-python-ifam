class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def descrever(self):
        return f"{self.marca} {self.modelo}"

# A classe Carro herda de Veiculo
class Carro(Veiculo):
    def __init__(self, marca, modelo, ano):
        super().__init__(marca, modelo)  # chama o construtor da classe pai
        self.ano = ano

    def descrever_completo(self):
        return f"{self.ano} {self.marca} {self.modelo}"

# Criando um objeto da classe Carro
carro_novo = Carro("Honda", "Civic", 2021)
print(carro_novo.descrever_completo())  # Saída: 2021 Honda Civic
