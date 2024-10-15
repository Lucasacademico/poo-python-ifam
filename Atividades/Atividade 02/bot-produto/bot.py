from botcity.web import WebBot, Browser, By
from botcity.maestro import *
from webdriver_manager.chrome import ChromeDriverManager
BotMaestroSDK.RAISE_NOT_CONNECTED = False

# Importação da class produto
from produto import Produto


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
    produto = Produto("Picolé", 2.00, 10)
    produto.exibir_informacoes()  

    # -------- ALTERAR O PATH AQUI -----------
    bot.browse(r"C:\Users\lrand\OneDrive\Área de Trabalho\Nova pasta\poo-python-ifam\Atividades\Atividade 02\bot-produto\html\index.html")  # 

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


