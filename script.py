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
        return [transacao for transacao in self.transacoes if transacao.categoria == categoria]

    def gastos_totais(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor < 0)

    def renda_total(self):
        return sum(transacao.valor for transacao in self.transacoes if transacao.valor > 0)

    def resumo_geral(self):
        total_transacoes = len(self.transacoes)
        renda_total = self.renda_total()
        gastos_totais = self.gastos_totais()
        saldo_final = self.saldo()
        print(f"Total de transações: {total_transacoes}")
        print(f"Renda total: {renda_total}")
        print(f"Gastos totais: {gastos_totais}")
        print(f"Saldo final: {saldo_final}")

def main():
    carteira = Carteira()

    while True:
        print("\nMenu de Opções:")
        print("1. Adicionar Transação")
        print("2. Exibir Transações")
        print("3. Resumo Geral")
        print("4. Filtrar por Categoria")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")