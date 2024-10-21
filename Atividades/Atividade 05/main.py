import sys
import os

# Adiciona o diretório atual ao caminho do sistema
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from carro import Carro
from motocicleta import Motocicleta

def main():
    # Criando instâncias de veículos
    carro1 = Carro("Toyota", "Corolla", 2020, 100, "Gasolina")
    motocicleta1 = Motocicleta("Yamaha", "Fazer", 2021, 80, 250)

    # Testando o cálculo de aluguel
    dias_aluguel = 10
    desconto = 0.1  # 10% de desconto

    valor_aluguel_carro = carro1.calcular_valor_aluguel(dias_aluguel, desconto)
    valor_aluguel_moto = motocicleta1.calcular_valor_aluguel(dias_aluguel)

    # Imprimindo detalhes dos veículos
    print(carro1)
    print(f'Valor do aluguel por {dias_aluguel} dias: {valor_aluguel_carro:.2f}\n')

    print(motocicleta1)
    print(f'Valor do aluguel por {dias_aluguel} dias: {valor_aluguel_moto:.2f}\n')

if __name__ == "__main__":
    main()
