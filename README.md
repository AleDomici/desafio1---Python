# Sistema de Controle Financeiro Pessoal

Este sistema utiliza os princípios da Programação Orientada a Objetos (POO) em Python para simular uma carteira virtual que permite registrar transações financeiras, categorizá-las, visualizar o histórico e obter um resumo financeiro.

---

## Estrutura do Sistema

### Classe **Transacao**

A **classe Transacao** representa uma transação financeira, com os seguintes atributos e métodos:

#### Atributos:
- **descricao**: Descrição da transação (por exemplo, "Salário", "Mercado").
- **valor**: Valor da transação (positivo para entradas, negativo para saídas).
- **categoria**: Categoria da transação (por exemplo, "Renda", "Alimentação").
- **data**: Data da transação no formato "DD/MM/AAAA".

#### Métodos:
- **resumo()**: Retorna uma string no formato: `Descrição | +Valor | Categoria | Data`.

---

### Classe **Carteira**

A **classe Carteira** simula uma carteira de transações, com os seguintes atributos e métodos:

#### Atributos:
- **transacoes**: Lista de objetos **Transacao**.

#### Métodos:
- **adicionar(transacao)**: Adiciona uma nova transação à carteira.
- **exibir_transacoes()**: Exibe todas as transações registradas.
- **saldo()**: Retorna o saldo total.
- **filtrar_por_categoria(categoria)**: Exibe transações de uma determinada categoria.
- **gastos_totais()**: Retorna a soma dos valores negativos (gastos).
- **renda_total()**: Retorna a soma dos valores positivos (renda).
- **resumo_geral()**: Imprime o total de transações, renda total, gastos totais e saldo final.

---

## Como Executar

### Pré-requisitos

- Python 3.x instalado no sistema.
- Um ambiente de desenvolvimento Python configurado (como Anaconda, PyCharm, VSCode, etc.).

### Passos para Execução

#### 1. Clone o Repositório:

Se o código está em um repositório Git, clone-o para a sua máquina:

```bash
git clone <https://github.com/AleDomici/desafio1---Python.git>
```
```bash
cd <desafio1---Python>
```

## 2. Crie um Ambiente Virtual (opcional, mas recomendado):

No terminal, execute os seguintes comandos:

```bash
python -m venv venv
source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
```

## 3. Execute o Código:

Crie um arquivo chamado `main.py` ou outro nome de sua escolha e copie o seguinte código para ele:

```python
```


## Exemplo de uso
carteira = Carteira()   
transacao1 = Transacao("Salário", 2500, "Renda", "10/04/2025")   
transacao2 = Transacao("Mercado", -500, "Alimentação", "12/04/2025")   
carteira.adicionar(transacao1)   
carteira.adicionar(transacao2)   

print("Transações:")   
carteira.exibir_transacoes()   

print("\nResumo Geral:")   
carteira.resumo_geral()   

print("\nFiltrar por categoria 'Alimentação':")   
for t in carteira.filtrar_por_categoria("Alimentação"):
    print(t.resumo())    

## 4. Execute o Código:
No terminal, execute o script com o comando:

```bash
python main.py
```
## Interaja com o Programa

O programa exibirá as transações cadastradas, o resumo geral das finanças e filtrará por categoria conforme configurado no exemplo.

## Exemplo de Saída:

```yaml
transacoes:
  - descricao: "Salário"
    valor: 2500.0
    categoria: "Renda"
    data: "10/04/2025"
  - descricao: "Mercado"
    valor: -500.0
    categoria: "Alimentação"
    data: "12/04/2025"

resumo_geral:
  total_transacoes: 2
  renda_total: 2500.0
  gastos_totais: -500.0
  saldo_final: 2000.0
```

