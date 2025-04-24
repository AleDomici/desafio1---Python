class Transacao:
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data

    def resumo(self):
        sinal = '+' if self.valor >= 0 else ''
        return f"{self.descricao} | {sinal}{self.valor} | {self.categoria} | {self.data}"
    
    
class Carteira:
    def __init__(self):
        self.transacoes = []

        def adicionar(self, transacao):
            self.transacoes.append(transacao)

        def exibir_transacoes(self):
         for transacao in self.transacoes:
                print(transacao.resumo())

        def saldo(self):
            return sum(transacao.valor for transacao in self.transacoes)
        
        def filtrar_por_categoria(self, categoria):
            return[transacao for transacao in self.transacoes if transacao.categoria == categoria]
        
        def gastos_totais(self):
            return sum(transacao.valor for transacao in self.transacoes if transacao.valor < 0)
        
        def renda_total(self):
            return sum(transacao.valor for transacao in self.transacoes if transacao.valor > 0)
        
