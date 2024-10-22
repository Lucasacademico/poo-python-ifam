# Classe base Pagamento

from abc import ABC, abstractmethod

# Classe base Pagamento
class Pagamento(ABC):

    @abstractmethod
    def processar_pagamento(self):
        pass 

    def detalhes_pagamento(self, metodo):
        print(f'Processando pagamento via {metodo}')

class PagamentoCartaoCredito(Pagamento):

    def processar_pagamento(self):
        print(f"- O pagamento do cartão foi processado com sucesso!")

class PagamentoBoleto(Pagamento):

    def processar_pagamento(self):
        print(f"- O pagamento do boleto foi processado com sucesso!") 

# Função de teste corrigida
def testar_pagamentos():
    pagamento_cartao = PagamentoCartaoCredito()  
    pagamento_boleto = PagamentoBoleto()  
    pagamento_cartao.detalhes_pagamento("Boleto bancário")
    pagamento_cartao.processar_pagamento()
    pagamento_boleto.detalhes_pagamento("Cartão de crédito")
    pagamento_boleto.processar_pagamento()
    

# Executar o teste
testar_pagamentos()