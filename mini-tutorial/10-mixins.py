'''Mixins são uma maneira de adicionar funcionalidades a uma classe sem usar herança tradicional. 
Eles são úteis para compartilhar comportamento entre classes de maneiras mais flexíveis.'''
class FiltroMixin:
    def aplicar_filtro(self, dados):
        return [dado for dado in dados if dado % 2 == 0]

class ProcessadorDados(FiltroMixin):
    def processar(self, dados):
        return self.aplicar_filtro(dados)

# Usando a funcionalidade do mixin
processador = ProcessadorDados()
dados = [1, 2, 3, 4, 5, 6]
print(processador.processar(dados))  # Saída: [2, 4, 6]
