class Livro:    
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def emprestar(self):
        if self.disponivel:
            print(f'Livro {self.titulo} - Emprestado com sucesso')
            self.disponivel = False
        else:
            print(f"Livro '{self.titulo}' - já está emprestado.")

    def devolver(self):
        if not self.disponivel:
            print(f'Livro {self.titulo} devolvido com sucesso')
            self.disponivel = True
        else:
            print(f'O livro já está disponível na livraria')

    def mostrar_info(self):
        status = 'Disponível' if self.disponivel else 'Emprestado'
        print(f'Título: {self.titulo}, Autor: {self.autor}, Status: {status}')
            

class Livraria:
    def __init__(self):
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O título {livro.titulo} foi adicionado na livraria')

    def emprestar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                livro.emprestar()
                return
        print(f'O livro "{titulo}" não existe na livraria.')

    def mostrar_inventario(self):
        if not self.livros:
            print('A livraria está vazia.')
        else:
            print('Inventário de livros:')
            for livro in self.livros:
                livro.mostrar_info()


# Livros disponíveis
livro1 = Livro('O Silmarillion', 'J.R.R Tolkien')
livro2 = Livro('Prince of Thorns', 'Mark Lawrence')

# Instância da livraria
livraria = Livraria()

# Adicionar livros
livraria.adicionar_livro(livro1)
livraria.adicionar_livro(livro2)

# Mostrar inventário
livraria.mostrar_inventario()
livraria.emprestar_livro('Prince of Thorns')
livraria.emprestar_livro('Prince of Thorns')



livro1.devolver()
livro2.devolver()
livro1.mostrar_info()























# class Livraria:
#     def __init__(self):
#         self.livros = []  # Lista de livros na livraria

#     def adicionar_livro(self, livro):
#         self.livros.append(livro)
#         print(f"O livro '{livro.titulo}' foi adicionado ao inventário.")

#     def emprestar_livro(self, titulo):
#         for livro in self.livros:
#             if livro.titulo == titulo:
#                 livro.emprestar()
#                 return
#         print(f"O livro '{titulo}' não foi encontrado no inventário.")

#     def mostrar_inventario(self):
#         if not self.livros:
#             print("O inventário está vazio.")
#         else:
#             print("Inventário da Livraria:")
#             for livro in self.livros:
#                 livro.mostrar_info()


# # Exemplo de uso:
# livraria = Livraria()

# # Adicionando livros à livraria
# livro1 = Livro("1984", "George Orwell")
# livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien")

# livraria.adicionar_livro(livro1)
# livraria.adicionar_livro(livro2)

# # Mostrar o inventário
# livraria.mostrar_inventario()

# # Emprestar e devolver livros
# livraria.emprestar_livro("1984")
# livraria.mostrar_inventario()

# livraria.emprestar_livro("1984")  # Tentando emprestar um livro já emprestado
# livro1.devolver()
# livraria.mostrar_inventario()
