class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # Getter para o nome
    @property
    def nome(self):
        return self._nome

    # Setter para o nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # Getter para o preço
    @property
    def preco(self):
        return self._preco

    # Setter para o preço
    @preco.setter
    def preco(self, valor):
        self._preco = valor

    # Getter para a quantidade
    @property
    def quantidade(self):
        return self._quantidade

    # Setter para a quantidade
    @quantidade.setter
    def quantidade(self, valor):
        self._quantidade = valor

    def exibir_informacoes(self):
        """Exibe as informações do produto."""
        print(f'Nome: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Quantidade: {self.quantidade}')

    def atualizar_informacoes(self, nome=None, preco=None, quantidade=None):
        """Atualiza as informações do produto."""
        if nome is not None:
            self.nome = nome
        if preco is not None:
            self.preco = preco
        if quantidade is not None:
            self.quantidade = quantidade
