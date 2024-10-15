class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.__saldo = saldo  # atributo privado

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor

    def sacar(self, valor):
        if valor <= self.__saldo:
            self.__saldo -= valor

    def exibir_saldo(self):
        return f"Saldo: {self.__saldo}"

# Criando uma instância da ContaBancaria
minha_conta = ContaBancaria("Maria", 1000)

# Tentando acessar o saldo diretamente (não funciona, pois é privado)
# print(minha_conta.__saldo)  # Gera um erro

# Acessando o saldo através do método público
print(minha_conta.exibir_saldo())  # Saída: Saldo: 1000
