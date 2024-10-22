
'''
Perguntas para Reflexão:
1. O que acontece se você adicionar um novo método de pagamento sem 
modificar a função processar? 
Resposta: O código continua funcionando normalmente desde que a nova subclasse implemente o método processar_pagamento.

2. Como o polimorfismo ajuda a manter o código flexível e extensível?
Resposta: Permite que os métodos sejam tratados separadamente em cada classe.

3. Qual é a diferença entre a função processar e os métodos 
processar_pagamento nas subclasses?
Resposta: Os métodos processar_pagamento() são as implementações lógicas de acordo com cada classe, 
já a função processar(), é uma função externa e faz a chamada do objeto Pagamento e chama o método processar_pagamento().

4. Como você pode garantir que todos os métodos de pagamento 
implementem o método processar_pagamento corretamente?
Resposta: Seguindo o padrão de implementação, pois o método processar_pagamento() chama a funcão processar()

'''



# Classe base Pagamento
class Pagamento:
    def processar_pagamento(self):
        pass 

class PagamentoCartaoCredito(Pagamento):
    def __init__(self, numero_cartao: int):
        self.numero_cartao = numero_cartao  

    def processar_pagamento(self):
        print(f"O pagamento do cartão {self.numero_cartao} foi processado com sucesso!")

class PagamentoBoleto(Pagamento):
    def __init__(self, codigo_boleto: int):
        self.codigo_boleto = codigo_boleto  

    def processar_pagamento(self):
        print(f"O pagamento do boleto {self.codigo_boleto} foi processado com sucesso!") 

class PagamentoPix(Pagamento):
    def __init__(self, chave_pix: str):
        self.chave_pix = chave_pix  

    def processar_pagamento(self):
        print(f"O pagamento via Pix com chave {self.chave_pix} foi processado com sucesso!")  

def processar(pagamento: Pagamento):
    pagamento.processar_pagamento()  

pagamento_cartao = PagamentoCartaoCredito(1234567890123456)
pagamento_boleto = PagamentoBoleto(987654321)
pagamento_pix = PagamentoPix("chave@pix.com")

# Testando o polimorfismo
processar(pagamento_cartao)
processar(pagamento_boleto)
processar(pagamento_pix)
