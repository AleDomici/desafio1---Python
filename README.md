#💰 Desafio: Controle Financeiro Pessoal com POO
Crie um sistema de controle financeiro com classes, atributos e métodos que simulem uma carteira virtual.

##✅ Objetivos

Neste desafio, você vai aplicar os princípios básicos de Programação Orientada a Objetos (POO) em Python para criar um sistema simples de controle financeiro pessoal. A proposta é simular uma carteira virtual que permite registrar transações (entradas e saídas de dinheiro), categorizá-las, visualizar o histórico financeiro e obter um resumo geral com renda, gastos e saldo.
O foco é praticar:
Criação de classes e objetos


Uso de atributos e métodos


Encapsulamento de dados


Manipulação de listas


Lógica de filtragem e agregação de valores

Classe Transacao:
Atributos:


descricao (ex: "Salário", "Mercado")


valor (positivo para entrada, negativo para saída)


categoria (ex: "Renda", "Alimentação", "Moradia", etc)


data (string no formato "DD/MM/AAAA")


Métodos:


resumo(): retorna uma string no formato:
 "Salário | +2500 | Renda | 10/04/2025"



Classe Carteira:
Atributos:


Lista de transações


Métodos:


adicionar(transacao): adiciona uma nova transação


exibir_transacoes(): mostra todas as transações cadastradas


saldo(): retorna o saldo total


filtrar_por_categoria(categoria): exibe as transações de uma determinada categoria


gastos_totais(): retorna a soma dos valores negativos


renda_total(): retorna a soma dos valores positivos


resumo_geral(): imprime:


Total de transações


Renda total


Gastos totais


Saldo final

