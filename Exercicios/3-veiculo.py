class Veiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    @property
    def marca(self):
        return self._marca
    
    # Setter para o marca
    @marca.setter
    def marca(self, valor):
        self._marca = valor

    @property
    def modelo(self):
        return self._modelo
    
    # Setter para o modelo
    @modelo.setter
    def modelo(self, valor):
        self._modelo = valor

    def informacao(self):
        print(f'Marca: {self.marca}, Modelo: {self.modelo}')

class Carro(Veiculo):
    def __init__(self, marca, modelo, numero_portas):
        super().__init__(marca, modelo)
        self.numero_portas = numero_portas
    
    def informacao(self):
        return f"{super().informacao()} com {self.numero_portas} portas"

carro = Carro("Mitsubishi", "Triton", 4)
print(carro.informacao())