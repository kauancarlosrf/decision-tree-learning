import random
import pandas as pd

# Definindo os atributos possíveis
atributos_credito = {
    'idade': [25, 30, 35, 40, 45],
    'renda_mensal': [2000, 3000, 4000, 5000, 6000],
    'score_credito': [600, 650, 700, 750, 800],
    'dividas': ['sim', 'não'],
    'tempo_emprego': ['1-3 anos', '3-5 anos', '5-10 anos', '10+ anos'],
    'tipo_residencia': ['casa', 'apartamento'],
    'historico_pagamento': ['bom', 'ruim'],
    'idade_conta_bancaria': [1, 2, 5, 10],
    'numero_cartoes_ativos': [1, 2, 3],
    'limite_cartao_anterior': [1000, 3000, 5000],
    'regiao_residencia': ['norte', 'sul', 'leste', 'oeste'],
    'possui_carro': ['sim', 'não'],
    'possui_imovel': ['sim', 'não'],
    'numero_dependentes': [0, 1, 2, 3],
    'historico_criminal': ['sim', 'não'],
    'ocupacao': ['empregado', 'autônomo', 'desempregado'],
    'educacao': ['ensino fundamental', 'ensino médio', 'ensino superior'],
    'gastos_mensais': [1000, 1500, 2000, 2500],
    'tempo_residencia_atual': [1, 3, 5, 10]
}

atributos_restaurant_book = {
    'Alt': ['Yes', 'No'],
    'Bar': ['Yes', 'No'],
    'Fri': ['Yes', 'No'],
    'Hun': ['Yes', 'No'],
    'Pat': ['Some', 'Full', 'None'],
    'Price': ['barato', 'intermediario', 'caro'],
    'Rain': ['Yes', 'No'],
    'Res': ['Yes', 'No'],
    'Type': ['Burger', 'French', 'Thai', 'Italian'],
    'Est': ['0-10', '10-30', '30-60', 'acima60'],
}

# Geração de n exemplos
dados = []
for _ in range(100):
    exemplo = {atributo: random.choice(valores) for atributo, valores in atributos_restaurant_book.items()}
    # A decisão (sim ou não) será gerada aleatoriamente, mas de forma equilibrada
    exemplo['decisao*'] = random.choice(['sim', 'não'])
    dados.append(exemplo)

# Criando o DataFrame
df = pd.DataFrame(dados)
# Salvando em um arquivo CSV
df.to_csv('./dataset_restaurant_100_linhas.csv', index=False)
print(df.head())
