class Produto:
    def __init__(self, preco):
        self._preco = preco

    @property
    def preco(self):
        return self._preco

    @preco.setter
    def preco(self, valor):
        if valor < 0:
            raise ValueError("O preço não pode ser negativo!")
        self._preco = valor

# Criando uma instância
p = Produto(50)

# Usando a propriedade
print(p.preco)  # Saída: 50

# Atualizando o preço com o setter
p.preco = 100
print(p.preco)  # Saída: 100

# Tenta definir um preço inválido
# p.preco = -10  # Isso gera um erro: ValueError: O preço não pode ser negativo!
