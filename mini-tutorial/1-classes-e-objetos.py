# Definindo uma classe
class Cachorro:
    # Método construtor
    def __init__(self, nome, idade):
        self.nome = nome  # Atributo da classe
        self.idade = idade

    # Método da classe
    def latir(self):
        return f"{self.nome} está latindo!"

# Criando um objeto (instância) da classe Cachorro
meu_cachorro = Cachorro("Rex", 5)

# Acessando atributos e métodos
print(meu_cachorro.nome)  # Output: Rex
print(meu_cachorro.latir())  # Output: Rex está latindo!
