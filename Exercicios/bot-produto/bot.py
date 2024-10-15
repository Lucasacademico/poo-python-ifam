from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
BotMaestroSDK.RAISE_NOT_CONNECTED = False


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

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
    bot.browse(r"C:\Users\lrand\OneDrive\Área de Trabalho\Nova pasta\bot-produto\index.html")  # Altere o caminho conforme necessário

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