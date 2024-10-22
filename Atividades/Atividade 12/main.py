from funcionario import FuncionarioHorista, FuncionarioMensalista, FuncionarioComissionado, FuncionarioPorProjeto
from processamento import processar_pagamento, simular_pagamentos_horistas

funcionarios = []

# Adicionando funcionários horistas
funcionarios.append(FuncionarioHorista("Carlos Silva", "001", 160, 15))
funcionarios.append(FuncionarioHorista("Ana Costa", "004", 120, 20))

# Adicionando funcionários mensalistas
funcionarios.append(FuncionarioMensalista("Maria Oliveira", "002", 3000))
funcionarios.append(FuncionarioMensalista("João Lima", "005", 2500))

# Adicionando funcionários comissionados
funcionarios.append(FuncionarioComissionado("Pedro Santos", "003", 2500, 10000, 0.1))
funcionarios.append(FuncionarioComissionado("Luiza Almeida", "006", 2000, 5000, 0.2))

print(f'\n----- Salários -----')
for funcionario in funcionarios:
    processar_pagamento(funcionario)

print(f'\n----- Simulação -----')
simular_pagamentos_horistas(funcionarios)
