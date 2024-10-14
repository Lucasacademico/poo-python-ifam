class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Meu nome é {self.nome} e eu tenho {self.idade} anos")

# Criando uma instancia da classe Pessoa
pessoa1 = Pessoa("Lucas", 31)
pessoa2 = Pessoa("Nagila", 27)

# Chamando o método de instância 
pessoa1.apresentar()
pessoa2.apresentar()
