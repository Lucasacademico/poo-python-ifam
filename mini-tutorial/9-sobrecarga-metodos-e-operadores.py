
# Ex 1
class Calculadora:
    def soma(self, a, b=0, c=0):
        return a + b + c

calc = Calculadora()

# Chamando o método com diferentes números de parâmetros
print(calc.soma(2))        # Saída: 2
print(calc.soma(2, 3))     # Saída: 5
print(calc.soma(2, 3, 4))  # Saída: 9

# Ex 2 - ARGS
class Calculadora:
    def soma(self, *args):
        return sum(args)

calc = Calculadora()

print(calc.soma(1, 2))          # Saída: 3
print(calc.soma(1, 2, 3, 4))    # Saída: 10

# Ex3 -kwargs
class Pessoa:
    def __init__(self, **kwargs):
        self.nome = kwargs.get('nome', 'Desconhecido')
        self.idade = kwargs.get('idade', 0)

    def mostrar_info(self):
        print(f'Nome: {self.nome}, Idade: {self.idade}')

# Exemplo de uso:
pessoa1 = Pessoa(nome='João', idade=25)
pessoa2 = Pessoa(nome='Maria')
pessoa3 = Pessoa()

pessoa1.mostrar_info()  # Saída: Nome: João, Idade: 25
pessoa2.mostrar_info()  # Saída: Nome: Maria, Idade: 0
pessoa3.mostrar_info()  # Saída: Nome: Desconhecido, Idade: 0

