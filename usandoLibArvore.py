from arvore import construir_arvore, prever
from dataSet import data_frame_dados_futebol, data_frame_decisoes_futebol, data_frame_dados_restaurante, data_frame_decisoes_restaurante


# Construir a árvore treinada no DataSet RESTAURANTE
arvore_restaurante = construir_arvore(data_frame_dados_restaurante, data_frame_decisoes_restaurante)

# Testando a árvore de decisão em um novo exemplo
novo_exemplo11 = {'preço': 'caro', 'dia_da_semana': 'sexta', 'esta_chovendo': 'não', 'tipo_de_comida': 'brasileira'}
novo_exemplo12 = {'preço': 'barato', 'dia_da_semana': 'sábado', 'esta_chovendo': 'sim', 'tipo_de_comida': 'brasileira'}
print("Decisão:", prever(arvore_restaurante, novo_exemplo11))  # Espera "não" ou "sim" com base na árvore
print("Decisão:", prever(arvore_restaurante, novo_exemplo12))  # Espera "não" ou "sim" com base na árvore


# Construir a árvore treinada no DataSet FUTEBOL
arvore_futebol = construir_arvore(data_frame_dados_futebol, data_frame_decisoes_futebol)

# Testando a árvore de decisão em um novo exemplo
novo_exemplo21 = {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim'}
novo_exemplo22 = {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim'}
print("Decisão:", prever(arvore_futebol, novo_exemplo21))  # Espera "perder" ou "ganhar" com base na árvore
print("Decisão:", prever(arvore_futebol, novo_exemplo22))  # Espera "perder" ou "ganhar" com base na árvore

