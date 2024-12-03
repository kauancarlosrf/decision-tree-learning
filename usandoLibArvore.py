import pandas as pd
from arvore import construir_arvore, prever
from data.dataSet import dataSetRestaurante, dataSetRestaurantBook, dataSetFutebol


# Build the trained tree on the RESTAURANT DataSet
arvore_restaurante = construir_arvore(dataSetRestaurante)
# Testing the decision tree on a new example
novo_exemplo11 = {'preço': 'caro', 'dia_da_semana': 'sexta', 'esta_chovendo': 'não'}
novo_exemplo12 = {'preço': 'barato', 'dia_da_semana': 'sábado', 'esta_chovendo': 'sim'}
print("Decisão 1 árvore-restaurante:", prever(arvore_restaurante, novo_exemplo11))  # Espera "não" ou "sim" com base na árvore
print("Decisão 2 árvore-restaurante:", prever(arvore_restaurante, novo_exemplo12))  # Espera "não" ou "sim" com base na árvore

# Build the trained tree on the FOOTBALL DataSet
arvore_futebol = construir_arvore(dataSetFutebol)
# Testing the decision tree on a new example
novo_exemplo21 = {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim'}
novo_exemplo22 = {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim'}
print("Decisão 1 árvore-futebol:", prever(arvore_futebol, novo_exemplo21))  # Espera "perder" ou "ganhar" com base na árvore
print("Decisão 2 árvore-futebol:", prever(arvore_futebol, novo_exemplo22))  # Espera "perder" ou "ganhar" com base na árvore

# Build the trained tree on the RESTAURANT BOOK DataSet (example from the reference book)
arvore_restaurant_book = construir_arvore(dataSetRestaurantBook)
# Testing the decision tree on a new example
novo_exemplo31 = {'Alt': 'No', 'Bar': 'No', 'Fri': 'Yes', 'Hun': 'Yes', 'Pat': 'Some', 'Price': '$$$', 'Rain': 'No', 'Res': 'Yes', 'Type': 'French', 'Est': '0-10'}
novo_exemplo32 = {'Alt': 'Yes', 'Bar': 'No', 'Fri': 'No', 'Hun': 'No', 'Pat': 'Full', 'Price': '$$$', 'Rain': 'Yes', 'Res': 'No', 'Type': 'Italian', 'Est': '>60'}
print("Decisão 1 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo31))  # Espera "Yes" ou "No" com base na árvore
print("Decisão 2 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo32))  # Espera "Yes" ou "No" com base na árvore

# Build the trained tree on the CREDIT DataSet (attempt of a real example)
arvore_credito = construir_arvore(pd.read_csv('dataset_credito_10000_linhas_balanceadas.csv'))
# Testing the decision tree on a new example
novo_exemplo41 = {
    'idade': 30,
    'renda_mensal': 4000,
    'score_credito': 750,
    'dividas': 'não',
    'tempo_emprego': '3-5 anos',
    'tipo_residencia': 'casa',
    'historico_pagamento': 'bom',
    'idade_conta_bancaria': 5,
    'numero_cartoes_ativos': 2,
    'limite_cartao_anterior': 3000,
    'regiao_residencia': 'sul',
    'possui_carro': 'sim',
    'possui_imovel': 'sim',
    'numero_dependentes': 2,
    'historico_criminal': 'não',
    'ocupacao': 'empregado',
    'educacao': 'ensino superior',
    'gastos_mensais': 2000,
    'tempo_residencia_atual': 3
}

novo_exemplo_42 = {
    'idade': 40,
    'renda_mensal': 5000,
    'score_credito': 750,
    'dividas': 'sim',
    'tempo_emprego': '3-5 anos',
    'tipo_residencia': 'apartamento',
    'historico_pagamento': 'ruim',
    'idade_conta_bancaria': 10,
    'numero_cartoes_ativos': 1,
    'limite_cartao_anterior': 1000,
    'regiao_residencia': 'norte',
    'possui_carro': 'não',
    'possui_imovel': 'não',
    'numero_dependentes': 1,
    'historico_criminal': 'sim',
    'ocupacao': 'autônomo',
    'educacao': 'ensino médio',
    'gastos_mensais': 2500,
    'tempo_residencia_atual': 5
}
print("Decisão 1 árvore-credito:", prever(arvore_credito, novo_exemplo41))  # Espera "Sim" ou "Não" com base na árvore
