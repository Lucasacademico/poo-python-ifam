from funcionario import FuncionarioHorista


def processar_pagamento(funcionario):
    print(f'Funcionário: {funcionario.nome} - Salário: {funcionario.calcular_salario()}')

def simular_pagamentos_horistas(funcionarios):
    for funcionario in funcionarios:
        if isinstance(funcionario, FuncionarioHorista):
            dias_nao_trabalhados = 8
            horas_trabalhadas = funcionario.horas_trabalhadas - (dias_nao_trabalhados * 8)
            funcionario.horas_trabalhadas = max(horas_trabalhadas, 0)  
            print(f'Funcionário: {funcionario.nome} - Salário após simulação: {funcionario.calcular_salario()}')
