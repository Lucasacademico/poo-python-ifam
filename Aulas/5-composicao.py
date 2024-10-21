class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def ligar(self):
        print(f"Veículo {self.marca} {self.modelo} ligado")

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def ligar(self):
        super().ligar()
        print(f"Carro {self.marca} {self.modelo} com {self.portas} portas ligado.")

meu_carro = Carro("Toyota", "Corolla", 4)
meu_carro.ligar()