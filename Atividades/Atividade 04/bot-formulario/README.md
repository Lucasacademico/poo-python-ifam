
# Instruções para Configuração do Projeto

## 1. Criar Ambiente Virtual

Para criar um ambiente virtual para o projeto, siga os passos abaixo:
1. Navegue até o diretório do projeto.
2. Execute o comando para criar o ambiente virtual:
   ```bash
   python -m venv venv
   ```
3. Ative o ambiente virtual:
   - Windows: `venv\Scripts\activate`
   - MacOS/Linux: `source venv/bin/activate`

## 2. Instalar Dependências

Após ativar o ambiente virtual, instale as dependências necessárias usando o `requirements.txt`:
```bash
pip install -r requirements.txt
```

## 3. Alterar Paths dos Formulários HTML no arquivo bot.py

Copie o Path dos arquivos da pasta formulario para os caminhos do arquivo bot.py conforme máquina do usuário.