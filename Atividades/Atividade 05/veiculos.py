class Veiculos:
    
    def __init__(self, nome, ano, diaria):
        self.__nome = nome
        self.__ano = ano
        self.__diaria = diaria

    # Gets e Sets
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nova_marca):
        self.__nome = nova_marca

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def diaria(self):
        return self.__diaria
    
    @diaria.setter
    def diaria(self, nova_diaria):
        self.__diaria = nova_diaria

    def calculoDiaria(self, dias):
        return dias * self.__diaria
    
    def
    
