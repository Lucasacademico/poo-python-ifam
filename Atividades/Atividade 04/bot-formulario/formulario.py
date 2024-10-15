class FormBase:
    def __init__(self, nome, idade, sexo, email, telefone):
        self._nome = nome
        self._idade = idade
        self._sexo = sexo
        self._email = email
        self._telefone = telefone

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property
    def idade(self):
        return self._idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            raise ValueError("Idade não pode ser negativa.")  # Validação
        self._idade = nova_idade

    @property
    def sexo(self):
        return self._sexo
    
    @sexo.setter
    def sexo(self, novo_sexo):
        self._sexo = novo_sexo
    
    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, novo_email):
        self._email = novo_email

    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, novo_telefone):
        self._telefone = novo_telefone

    def informacao(self):
        return f'Nome: {self._nome}, \nidade: {self._idade}, \nSexo: {self._sexo}, \nE-mail: {self._email}, \nTelefone: {self._telefone}'


class FormContato(FormBase):
    def __init__(self, nome, idade, sexo, email, telefone, assunto, mensagem):
        super().__init__(nome, idade, sexo, email, telefone)
        self._assunto = assunto
        self._mensagem = mensagem

    @property
    def assunto(self):
        return self._assunto

    @assunto.setter
    def assunto(self, novo_assunto):
        self._assunto = novo_assunto  

    @property
    def mensagem(self):
        return self._mensagem

    @mensagem.setter
    def mensagem(self, nova_mensagem):
        self._mensagem = nova_mensagem  

    def informacao(self):
        return f"{super().informacao()}, \nMensagem: {self._mensagem}, \nAssunto: {self._assunto}" 


class FormLogin(FormContato):
    def __init__(self, nome, idade, sexo, email, telefone, assunto, mensagem, senha):
        super().__init__(nome, idade, sexo, email, telefone, assunto, mensagem)
        self._senha = senha

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, nova_senha):
        self._senha = nova_senha  

    def informacao(self):
        return f"{super().informacao()}, \nSenha: {self._senha}"