# Import for the Desktop Bot
from botcity.core import DesktopBot

# Import for integration with BotCity Maestro SDK
from botcity.maestro import *

# Disable errors if we are not connected to Maestro
BotMaestroSDK.RAISE_NOT_CONNECTED = False

import subprocess
import time

class Bot(DesktopBot):
    def acessar_interface(self):
        # Usar subprocess para garantir que o script Tkinter seja executado corretamente
        subprocess.run(["python", r"C:/Users/matutino/Desktop/entrega/atividade13/bot-tkinter/teste.py"])
        time.sleep(2)  # Espera para garantir que a interface tenha tempo de abrir
    
    def preencher_campos(self):
        # Localiza o campo "Nome" e preenche com um nome
        if not self.find("campo_nome.png", matching=0.97, waiting_time=500):
            self.not_found("campo_nome.png")
        self.click()
        self.paste('12456')
        

    def action(self, execution=None):
        # Implementar a lógica principal aqui.
        self.acessar_interface()
        # Aqui você pode adicionar os comandos para preencher os campos na interface Tkinter

def main():
    # Integração com BotCity Maestro, caso esteja usando
    maestro = BotMaestroSDK.from_sys_args()
    execution = maestro.get_execution()
    print(f"Task ID is: {execution.task_id}")
    print(f"Task Parameters are: {execution.parameters}")


    # Inicializa o bot e chama o método para acessar a interface
    bot = Bot()
    bot.acessar_interface()

def not_found(label):
    print(f"Element not found: {label}")

if __name__ == '__main__':
    main()
