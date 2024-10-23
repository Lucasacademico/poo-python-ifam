from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, matricula):
        self.__nome = nome
        self.__matricula = matricula

    @abstractmethod
    def calcular_salario(self):
        pass

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome

    @property
    def matricula(self):
        return self.__matricula
    
    @matricula.setter
    def matricula(self, nova_matricula):
        self.__matricula = nova_matricula


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, matricula, horas_trabalhadas, valor_hora):
        super().__init__(nome, matricula)
        self.__horas_trabalhadas = horas_trabalhadas
        self.__valor_hora = valor_hora

    @property
    def horas_trabalhadas(self):
        return self.__horas_trabalhadas
    
    @horas_trabalhadas.setter
    def horas_trabalhadas(self, nova_horas_trabalhadas):
        self.__horas_trabalhadas = nova_horas_trabalhadas

    @property
    def valor_hora(self):
        return self.__valor_hora
    
    @valor_hora.setter
    def valor_hora(self, novo_valor_hora):
        self.__valor_hora = novo_valor_hora

    def calcular_salario(self):
        return self.__horas_trabalhadas * self.__valor_hora
        

class FuncionarioMensalista(Funcionario):
    def __init__(self, nome, matricula, salario_mensal):
        super().__init__(nome, matricula)
        self.__salario_mensal = salario_mensal

    @property
    def salario_mensal(self):
        return self.__salario_mensal
    
    @salario_mensal.setter
    def salario_mensal(self, novo_salario_mensal):
        self.__salario_mensal = novo_salario_mensal
        
    def calcular_salario(self):
        return self.__salario_mensal


class FuncionarioComissionado(Funcionario):
    def __init__(self, nome, matricula, salario_base, vendas, taxa_comissao):
        super().__init__(nome, matricula)
        self.__salario_base = salario_base
        self.__vendas = vendas
        self.__taxa_comissao = taxa_comissao

    @property
    def salario_base(self):
        return self.__salario_base
    
    @salario_base.setter
    def salario_base(self, novo_salario_base):
        self.__salario_base = novo_salario_base

    @property
    def vendas(self):
        return self.__vendas
    
    @vendas.setter
    def vendas(self, nova_vendas):
        self.__vendas = nova_vendas

    @property
    def taxa_comissao(self):
        return self.__taxa_comissao
    
    @taxa_comissao.setter
    def taxa_comissao(self, nova_taxa_comissao):
        self.__taxa_comissao = nova_taxa_comissao

    def calcular_salario(self):
        return self.__salario_base + (self.__vendas * self.__taxa_comissao)


class FuncionarioPorProjeto(Funcionario):
    def __init__(self, nome, matricula, valor_por_projeto, projetos_realizados):
        super().__init__(nome, matricula)
        self.__valor_por_projeto = valor_por_projeto
        self.__projetos_realizados = projetos_realizados

    @property
    def valor_por_projeto(self):
        return self.__valor_por_projeto
    
    @valor_por_projeto.setter
    def valor_por_projeto(self, novo_valor):
        self.__valor_por_projeto = novo_valor

    @property
    def projetos_realizados(self):
        return self.__projetos_realizados
    
    @projetos_realizados.setter
    def projetos_realizados(self, novos_projetos):
        self.__projetos_realizados = novos_projetos

    def calcular_salario(self):
        return self.valor_por_projeto * self.projetos_realizados
