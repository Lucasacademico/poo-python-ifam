class Aluno:
    def __init__(self, nome: str, matricula: int):
        self.nome = nome  
        self.matricula = matricula  

    def mostrar_info(self):
        print(f"Nome: {self.nome}, Matrícula: {self.matricula}")  


class Curso:
    def __init__(self, nome: str, codigo: int):
        self.nome = nome  
        self.codigo = codigo 
        self.lista_alunos = []  

    def adicionar_aluno(self, aluno: Aluno):
        self.lista_alunos.append(aluno) 
        print(f"Aluno {aluno.nome} adicionado ao curso {self.nome}!") 

    def mostrar_alunos(self):
        if not self.lista_alunos:
            print(f"Não há alunos cadastrados no curso {self.nome}.")  
        else:
            print(f"Alunos cadastrados no curso {self.nome}:")
            for aluno in self.lista_alunos:
                aluno.mostrar_info() 


class Escola:
    def __init__(self, nome_escola: str):
        self.nome = nome_escola  
        self.lista_cursos = [] 

    def adicionar_curso(self, curso: Curso):
        self.lista_cursos.append(curso)  
        print(f"Curso {curso.nome} adicionado à escola {self.nome}!")

    def mostrar_cursos(self):
        if not self.lista_cursos:
            print("Não há cursos cadastrados.")  
        else:
            print("Cursos cadastrados:")
            for curso in self.lista_cursos:
                print(f"- {curso.nome}")  
                curso.mostrar_alunos() 


# Criando alguns alunos
aluno1 = Aluno("Son Goku", 12345)
aluno2 = Aluno("Uzumaki Naruto", 67890)
aluno3 = Aluno("Light Yagami", 54321)

# Criando cursos e adicionando alunos a esses cursos
curso_python = Curso("Python Avançado", 101)
curso_java = Curso("Java Básico", 102)
curso_python.adicionar_aluno(aluno1)
curso_java.adicionar_aluno(aluno2)

# Criando uma escola e adicionando os cursos
escola_ti = Escola("Escola de Tecnologia")
escola_ti.adicionar_curso(curso_python)
escola_ti.adicionar_curso(curso_java)

# Mostrando informações da escola, cursos e alunos
escola_ti.mostrar_cursos()


