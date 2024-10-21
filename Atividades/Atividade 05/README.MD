# Sistema de Gerenciamento de Aluguel de Veículos

## Descrição

Este projeto visa a implementação de um sistema para gerenciar o aluguel de veículos de diferentes tipos (carros e motocicletas). O sistema deve calcular o custo do aluguel com base no tipo de veículo, número de dias de locação, e aplicar diferentes regras de cálculo de acordo com o veículo alugado.

## Requisitos

### Funcionalidades Gerais
1. **Encapsulamento**  
   - Propriedades privadas para armazenar:
     - Nome do veículo
     - Ano de fabricação
     - Valor diário de aluguel
   - Métodos de instância para obter e definir os valores encapsulados.

2. **Cálculo do Aluguel**  
   - Método de cálculo do valor total do aluguel com base no número de dias.
   - Sobrecarga do método de cálculo para aceitar argumentos opcionais, como descontos.

### Funcionalidades Específicas para Carros
1. **Propriedade "Tipo de Combustível"**  
   - Adicionar uma propriedade específica que indique o tipo de combustível (gasolina, etanol, etc.).

2. **Regras de Desconto**  
   - Sobrescrever o método de cálculo para aplicar um desconto extra quando o aluguel for por mais de 7 dias.

### Funcionalidades Específicas para Motocicletas
1. **Propriedade "Cilindrada"**  
   - Adicionar uma propriedade específica para armazenar a cilindrada da motocicleta (ex.: 150cc, 250cc, etc.).
 
2. **Regras de Aumento de Custo**  
   - Sobrescrever o método de cálculo do valor total para aumentar o custo se a cilindrada for maior que 200cc.

### Funcionalidades de Classe
1. **Quantidade de Veículos Cadastrados**  
   - Método de classe para calcular a quantidade total de veículos cadastrados no sistema.

2. **Ajuste de Preço Global**  
   - Método de classe para aplicar um aumento percentual no valor diário de aluguel de todos os veículos.

### Funcionalidade Adicional
- Sobrecarga do método de cálculo para aceitar um segundo argumento opcional, como um cupom de desconto que possa reduzir o valor final do aluguel.
