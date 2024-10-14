class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura / 100  # Converte altura para metros

    def crescer(self, cm):
        # Adiciona o crescimento em metros
        self.altura += cm / 100

    def envelhecer(self, anos):
        for _ in range(anos):
            if self.idade < 21:
                self.crescer(0.5)  # Cresce 0.5 cm até os 21 anos
            self.idade += 1

    def engordar(self, kilos):
        self.peso += kilos

    def emagrecer(self, kilos):
        self.peso -= kilos

    def exibeResult(self):
        print("\n\n")
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso} kg')
        print(f'Altura: {self.altura * 100:.2f} cm')  # Converte para centímetros para exibir
        print(f'IMC: {self.calcular_imc():.2f}')
        print(f'Classificação IMC: {self.classificar_imc()}')

    def calcular_imc(self):
        # Fórmula do IMC: peso / (altura * altura)
        return self.peso / (self.altura ** 2)

    def classificar_imc(self):
        imc = self.calcular_imc()
        if imc < 18.5:
            return "Abaixo do peso"
        elif 18.5 <= imc < 24.9:
            return "Peso normal"
        elif 25 <= imc < 29.9:
            return "Sobrepeso"
        elif 30 <= imc < 34.9:
            return "Obesidade grau I"
        elif 35 <= imc < 39.9:
            return "Obesidade grau II"
        else:
            return "Obesidade grau III"

def main():
    p1 = Pessoa("Lucas", 15, 81, 178)
    
    p1.envelhecer(3)  # Envelhecer por 3 anos, crescendo 0.5 cm por ano até os 21 anos
    p1.exibeResult()

if __name__ == "__main__":
    main()
