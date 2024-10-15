from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
BotMaestroSDK.RAISE_NOT_CONNECTED = False


class Produto:
    def __init__(self, nome, preco, quantidade):
        self._nome = nome
        self._preco = preco
        self._quantidade = quantidade

    # Getter para o nome
    @property
    def nome(self):
        return self._nome

    # Setter para o nome
    @nome.setter
    def nome(self, valor):
        self._nome = valor

    # Getter para o preço
    @property
    def preco(self):
        return self._preco

    # Setter para o preço
    @preco.setter
    def preco(self, valor):
        self._preco = valor

    # Getter para a quantidade
    @property
    def quantidade(self):
        return self._quantidade

    # Setter para a quantidade
    @quantidade.setter
    def quantidade(self, valor):
        self._quantidade = valor

    def exibir_informacoes(self):
        """Exibe as informações do produto."""
        print(f'Nome: {self.nome}')
        print(f'Preço: R$ {self.preco:.2f}')
        print(f'Quantidade: {self.quantidade}')

    def atualizar_informacoes(self, nome=None, preco=None, quantidade=None):
        """Atualiza as informações do produto."""
        if nome is not None:
            self.nome = nome
        if preco is not None:
            self.preco = preco
        if quantidade is not None:
            self.quantidade = quantidade


def main():
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")

    bot = WebBot()
    bot.headless = False
    bot.browser = Browser.CHROME
    bot.driver_path = ChromeDriverManager().install()

    print("Iniciando a automação do formulário de produto.")
    produto = Produto("Produto Exemplo", 99.99, 10)
    produto.exibir_informacoes()  
    bot.browse(r"C:\Users\matutino\Desktop\poo-python-ifam\Exercicios\bot-produto\index.html")  # Altere o caminho conforme necessário

    # Preenchendo o formulário com os getters
    bot.find_element('//*[@id="nome"]', By.XPATH).send_keys(str(produto.nome))
    bot.wait(1000)
    bot.find_element('//*[@id="preco"]', By.XPATH).send_keys(str(produto.preco))
    bot.wait(1000)
    bot.find_element('//*[@id="quantidade"]', By.XPATH).send_keys(str(produto.quantidade))
    bot.wait(1000)
    bot.enter()

    print("Formulário enviado com sucesso.")


def not_found(label):
    print(f"Element not found: {label}")


if __name__ == '__main__':
    main()


