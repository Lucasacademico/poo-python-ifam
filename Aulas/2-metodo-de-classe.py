
# --- Código exemplo 1 ----
class Pessoa:
    quantidadePessoas = 0 # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        Pessoa.quantidadePessoas += 1

    @classmethod
    def mostrar_qtd_pessoas(cls):
        print(f"Total de pessoas: {cls.quantidadePessoas}")

# Criando instâncias da classe Pessoa
pessoa1 = Pessoa("Lucas", 31)
pessoa2 = Pessoa("Nagila", 27)
pessoa3 = Pessoa("Jubi", 28)


# Chamando o método de classe
Pessoa.mostrar_qtd_pessoas()

# --------------------------------------------------------------------------------------
# # --- Melhorando o exemplo
# class Pessoa:
#     quantidadePessoas = 0 # Atributo de classe

#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
#         Pessoa.quantidadePessoas += 1

#     def apresentarPessoas(self):
#         print(f"- {self.nome} possui {self.idade} anos")

#     @classmethod
#     def mostrar_qtd_pessoas(cls):
#         print(f"Total de pessoas: {cls.quantidadePessoas}")

# # Criando instâncias da classe Pessoa
# pessoa1 = Pessoa("Lucas", 31)
# pessoa2 = Pessoa("Nagila", 27)

# # Chamando o método de classe para mostrar quantidade
# Pessoa.mostrar_qtd_pessoas()

# # Mostrar as pessoas
# pessoa1.apresentarPessoas()
# pessoa2.apresentarPessoas()

# # --------------------------------------------------------------------------------------
# # # --- Código exemplo 2 ----
# class Exemplo:
#     contador = 0 # Atributo de classe

#     def __init__(self, valor):
#         self.valor = valor # Atributo de instância
#         Exemplo.contador += 1

#     def metodo_instancia(self):
#         # Acessa o atributo da instância
#         print(f"Valor da instância: {self.valor}")

#     @classmethod
#     def metodo_classe(cls):
#         # Acessa o atributo de classe
#         print(f"Contador da classe: {cls.contador}")

# # Criando instâncias da classe Exemplo
# obj1 = Exemplo(10)
# obj2 = Exemplo(20)

# # Chamando métodos de instância
# obj1.metodo_instancia()
# obj2.metodo_instancia()

# # Chamando método de classe
# Exemplo.metodo_classe()