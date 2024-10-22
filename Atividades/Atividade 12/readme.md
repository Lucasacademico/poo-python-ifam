# Sistema de Pagamento de Funcionários

Você foi encarregado de desenvolver um sistema de pagamento para uma empresa que possui diferentes tipos de funcionários. Cada tipo de funcionário tem uma forma diferente de calcular o salário, e o sistema deve ser flexível o suficiente para acomodar novos tipos de funcionários no futuro. O sistema também deve encapsular as propriedades dos funcionários e usar **getters** e **setters** para acessar essas propriedades.

## Instruções

### Classe `Funcionario` (Classe Abstrata):
- Esta classe deve ter os seguintes atributos (encapsulados):
  - `nome`: Nome do funcionário.
  - `matricula`: Número de matrícula do funcionário.
  
- Deve ter um método abstrato `calcular_salario(self)` que será implementado nas subclasses para calcular o salário de diferentes tipos de funcionários.
  
- Implemente **getters** e **setters** para os atributos encapsulados.

## Tipos de Funcionários:

### 1. `FuncionarioHorista`: 
   - Um funcionário que é pago por hora.
   - **Atributos:**
     - `horas_trabalhadas`: Número de horas trabalhadas.
     - `valor_hora`: Valor pago por hora.
     
   - Implemente o método `calcular_salario(self)` para retornar o salário total (`horas_trabalhadas * valor_hora`).

### 2. `FuncionarioMensalista`:
   - Um funcionário que recebe um salário fixo mensal.
   - **Atributos:**
     - `salario_mensal`: Valor do salário mensal fixo.
     
   - Implemente o método `calcular_salario(self)` para retornar o valor do salário mensal.

### 3. `FuncionarioComissionado`:
   - Um funcionário que recebe uma comissão baseada em vendas.
   - **Atributos:**
     - `salario_base`: Salário base.
     - `vendas`: Valor total de vendas realizadas.
     - `taxa_comissao`: Percentual de comissão sobre as vendas.
     
   - Implemente o método `calcular_salario(self)` para retornar o salário total (`salario_base + (vendas * taxa_comissao)`).

## Função `processar_pagamento`:
- Crie uma função `processar_pagamento(funcionario)` que receba um objeto do tipo `Funcionario` e imprima o nome do funcionário e o valor de seu salário, chamando o método `calcular_salario`.

## Tarefas:
- Crie vários funcionários (horistas, mensalistas, comissionados) e adicione-os a uma lista.
- Use a função `processar_pagamento` para iterar sobre a lista e imprimir os salários de todos os funcionários.

## Requisitos:
1. Use a classe abstrata `ABC` para garantir que a classe `Funcionario` não possa ser instanciada diretamente.
2. Use **getters** e **setters** para acessar e modificar os atributos encapsulados.
3. Implemente o conceito de polimorfismo no método `processar_pagamento`.
4. Garanta a encapsulação dos atributos em todas as classes.

## Tarefas adicionais:
1. **Novo tipo de funcionário**: Por exemplo, um funcionário que recebe um salário por projeto, onde o pagamento é baseado em um valor fixo por projeto.
2. **Validações**: Implementar validação para garantir que as horas trabalhadas e o valor da comissão sejam positivos.
3. **Simulação de pagamentos**: Crie uma função que simule um mês de pagamentos, incluindo feriados e fins de semana para funcionários horistas.
