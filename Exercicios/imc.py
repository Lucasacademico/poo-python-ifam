class Pessoa:
    def __init__(self, peso, altura): 
        self.peso = peso
        self.altura = altura

    def calculaImc(self):
        imc = self.peso / (self.altura ** 2)
        return imc

    def verificaImc(self):
        imc = self.calculaImc()
        if imc < 18:
            return "Abaixo do peso"
        elif imc > 18 and imc < 24.9:
            return "Pesom normal"
        elif imc > 25 and imc < 29.9:
            return "Sobrepeso"
        else:
            return "Gordão"
        
    def exibeResult(self):
        imc = self.calculaImc()
        classificacao = self.verificaImc()
        print(f"Seu IMC é: {imc:.2f}")
        print(f"Faixa de IMC: {classificacao}")
        

def main():
    peso = float(input("Digite o seu peso em kg: "))
    altura = float(input("Digite a sua altura em metros: "))
    pessoa = Pessoa(peso, altura)
    pessoa.exibeResult()

if __name__ == "__main__":
    main()