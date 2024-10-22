from tkinter import *
from tkinter import ttk
from tkinter import messagebox

# Lista para armazenar os funcionários cadastrados
funcionarios = []

# Função para cadastrar funcionário
def cadastrar_funcionario():
    nome = entry_nome.get()
    matricula = entry_matricula.get()
    tipo_funcionario = combo_tipo.get()
    salario = entry_salario.get()
    
    # Validações simples
    if not nome or not matricula or not tipo_funcionario or not salario:
        messagebox.showwarning("Atenção", "Por favor, preencha todos os campos.")
        return
    
    # Adiciona o funcionário à lista
    funcionario = {
        "nome": nome,
        "matricula": matricula,
        "tipo": tipo_funcionario,
        "salario": salario
    }
    funcionarios.append(funcionario)
    
    # Limpa os campos após cadastro
    entry_nome.delete(0, END)
    entry_matricula.delete(0, END)
    combo_tipo.set('')
    entry_salario.delete(0, END)

    messagebox.showinfo("Cadastro de Funcionário", f'Funcionário Cadastrado:\nNome: {nome}\nMatrícula: {matricula}\nTipo: {tipo_funcionario}\nSalário: {salario}')

# Função para listar funcionários cadastrados
def listar_funcionarios():
    # Limpa a árvore antes de listar
    for i in tree.get_children():
        tree.delete(i)
    
    # Adiciona funcionários à árvore
    for funcionario in funcionarios:
        tree.insert("", "end", values=(funcionario["nome"], funcionario["matricula"], funcionario["tipo"], funcionario["salario"]))

# Criação da janela principal
root = Tk()
root.title("Cadastro de Funcionário")

# Frame para organizar os widgets
frm = ttk.Frame(root, padding=10)
frm.grid()

# Labels e Entradas
ttk.Label(frm, text="Nome:").grid(column=0, row=0, sticky=W)
entry_nome = ttk.Entry(frm)
entry_nome.grid(column=1, row=0)

ttk.Label(frm, text="Matrícula:").grid(column=0, row=1, sticky=W)
entry_matricula = ttk.Entry(frm)
entry_matricula.grid(column=1, row=1)

ttk.Label(frm, text="Tipo de Funcionário:").grid(column=0, row=2, sticky=W)
combo_tipo = ttk.Combobox(frm, values=["Horista", "Mensalista", "Comissionado", "Por Projeto"])
combo_tipo.grid(column=1, row=2)

ttk.Label(frm, text="Salário:").grid(column=0, row=3, sticky=W)
entry_salario = ttk.Entry(frm)
entry_salario.grid(column=1, row=3)

# Botão para cadastrar funcionário
ttk.Button(frm, text="Cadastrar", command=cadastrar_funcionario).grid(column=0, row=4, columnspan=2)

# Botão para listar funcionários
ttk.Button(frm, text="Listar Funcionários", command=listar_funcionarios).grid(column=0, row=5, columnspan=2)

# Árvore para exibir a lista de funcionários
tree = ttk.Treeview(frm, columns=("Nome", "Matrícula", "Tipo", "Salário"), show='headings')
tree.heading("Nome", text="Nome")
tree.heading("Matrícula", text="Matrícula")
tree.heading("Tipo", text="Tipo")
tree.heading("Salário", text="Salário")
tree.grid(column=0, row=6, columnspan=2)

# Inicia o loop da interface
root.mainloop()
