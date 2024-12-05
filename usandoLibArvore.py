import pandas as pd
from arvore import construir_arvore, prever
from data.dataSet import dataSetRestaurante, dataSetRestaurantBook, dataSetRestaurantBook2, dataSetFutebol
from data.splitData import split_data
from validacao.validacao import validar_modelo


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


dataFrameTreinoRestaurantBook, dataFrameValidacaoRestaurantBook = split_data(pd.DataFrame(dataSetRestaurantBook2))
# esta dando erro: dataFrameTreinoRestaurantBook, dataFrameValidacaoRestaurantBook = split_data(pd.read_csv('./data/restaurantBook/dataset_restaurant_100_linhas.csv'))
# Build the trained tree on the RESTAURANT BOOK DataSet (example from the reference book)

arvore_restaurant_book = construir_arvore(dataFrameTreinoRestaurantBook)
# Testing the decision tree on a new example
novo_exemplo31 = {'Alt': 'No', 'Bar': 'No', 'Fri': 'Yes', 'Hun': 'Yes', 'Pat': 'Some', 'Price': '$$$', 'Rain': 'No', 'Res': 'Yes', 'Type': 'French', 'Est': '0-10'}
novo_exemplo32 = {'Alt': 'Yes', 'Bar': 'No', 'Fri': 'No', 'Hun': 'No', 'Pat': 'Full', 'Price': '$$$', 'Rain': 'Yes', 'Res': 'No', 'Type': 'Italian', 'Est': '>60'}
print("Decisão 1 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo31))  # Espera "Yes" ou "No" com base na árvore
print("Decisão 2 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo32))  # Espera "Yes" ou "No" com base na árvore
validar_modelo(arvore_restaurant_book, dataFrameValidacaoRestaurantBook)

# Build the trained tree on the CREDIT DataSet (attempt of a real example)
dataFrameTreinoCredito, dataFrameValidacaoCredito = split_data(pd.read_csv('./data/credito/dataset_credito_10000_linhas_balanceadas.csv'))
arvore_credito = construir_arvore(dataFrameTreinoCredito)
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
print("Decisão 1 árvore-credito:", prever(arvore_credito, novo_exemplo41))  # Espera "Sim" ou "Não" com base na árvore

validar_modelo(arvore_credito, dataFrameValidacaoCredito)
