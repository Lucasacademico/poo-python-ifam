class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def crescer(self, cm):
        self.altura = cm

    def envelhecer(self):
        i = 1
        for i in range(i):
            if self.idade < 21:
                self.crescer(0.5)

    def engordar(self, kilos):
        self.peso -= kilos

    def exibeResult(self):
        print("\n\n")
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.nome}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

        

       
    
def main():
    nome = input("Digite seu nome: ")
    idade = input("Digite sua idade: ")
    peso = input("Digite seu peso: ")
    altura = input("Digite sua altura: ")
    pessoa = Pessoa(nome, idade, peso, altura)
    
    pessoa.exibeResult()
    pessoa.envelhecer(3)  # Envelhecer por 3 anos, crescendo 0.5 cm por ano até os 21 anos

if __name__ == "__main__":
    main()
