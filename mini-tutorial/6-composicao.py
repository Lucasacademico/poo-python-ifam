class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def ligar(self):
        return "Motor ligado"

class Carro:
    def __init__(self, marca, modelo, motor):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor  # O carro contém um motor

    def ligar_carro(self):
        return f"{self.motor.ligar()} no carro {self.marca} {self.modelo}"

# Criando objetos
motor_v8 = Motor(500)
carro_esportivo = Carro("Ferrari", "F8", motor_v8)

print(carro_esportivo.ligar_carro())  # Saída: Motor ligado no carro Ferrari F8
