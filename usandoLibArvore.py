from arvore import construir_arvore, prever
from dataSet import data_frame_dados_futebol, data_frame_decisoes_futebol, data_frame_dados_restaurante, data_frame_decisoes_restaurante, data_frame_dados_restaurant_book, data_frame_decisoes_restaurant_book

import graphviz


# Construir a árvore treinada no DataSet RESTAURANTE
# Build the trained tree on the RESTAURANT DataSet
arvore_restaurante = construir_arvore(data_frame_dados_restaurante, data_frame_decisoes_restaurante)

# Testando a árvore de decisão em um novo exemplo
# Testing the decision tree on a new example
novo_exemplo11 = {'preço': 'caro', 'dia_da_semana': 'sexta', 'esta_chovendo': 'não'}
novo_exemplo12 = {'preço': 'barato', 'dia_da_semana': 'sábado', 'esta_chovendo': 'sim'}
print("Decisão 1 árvore-restaurante:", prever(arvore_restaurante, novo_exemplo11))  # Espera "não" ou "sim" com base na árvore
print("Decisão 2 árvore-restaurante:", prever(arvore_restaurante, novo_exemplo12))  # Espera "não" ou "sim" com base na árvore


# Construir a árvore treinada no DataSet FUTEBOL
# Build the trained tree on the FOOTBALL DataSet
arvore_futebol = construir_arvore(data_frame_dados_futebol, data_frame_decisoes_futebol)

# Testando a árvore de decisão em um novo exemplo
# Testing the decision tree on a new example
novo_exemplo21 = {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim'}
novo_exemplo22 = {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim'}
print("Decisão 1 árvore-futebol:", prever(arvore_futebol, novo_exemplo21))  # Espera "perder" ou "ganhar" com base na árvore
print("Decisão 2 árvore-futebol:", prever(arvore_futebol, novo_exemplo22))  # Espera "perder" ou "ganhar" com base na árvore

# Construir a árvore treinada no DataSet RESTAURANT BOOK (exemplo do livro de referência)
# Build the trained tree on the RESTAURANT BOOK DataSet (example from the reference book)
arvore_restaurant_book = construir_arvore(data_frame_dados_restaurant_book, data_frame_decisoes_restaurant_book)

# Testando a árvore de decisão em um novo exemplo
# Testing the decision tree on a new example
novo_exemplo31 = {'Alt': 'No', 'Bar': 'No', 'Fri': 'Yes', 'Hun': 'Yes', 'Pat': 'Some', 'Price': '$$$', 'Rain': 'No', 'Res': 'Yes', 'Type': 'French', 'Est': '0-10'}
novo_exemplo32 = {'Alt': 'Yes', 'Bar': 'No', 'Fri': 'No', 'Hun': 'No', 'Pat': 'Full', 'Price': '$$$', 'Rain': 'Yes', 'Res': 'No', 'Type': 'Italian', 'Est': '>60'}
print("Decisão 1 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo31))  # Espera "Yes" ou "No" com base na árvore
print("Decisão 2 árvore-restaurant-book:", prever(arvore_restaurant_book, novo_exemplo32))  # Espera "Yes" ou "No" com base na árvore




def visualizar_arvore(no, nome='Arvore_Decisao'):
    def construir_grafo(no, grafo, caminho=''):
        if no.folha:
            grafo.node(caminho, f'{no.classe}', shape='box', style='filled', color='lightgrey')
        else:
            grafo.node(caminho, f'{no.atributo}')
            for filho in no.filhos:
                novo_caminho = f'{caminho}->{filho.valor}'
                grafo.edge(caminho, novo_caminho, label=f'{filho.valor}')
                construir_grafo(filho, grafo, novo_caminho)
    
    grafo = graphviz.Digraph(nome, format='png')
    construir_grafo(no, grafo)
    grafo.render(view=False)  # Salva e não abre o arquivo gerado
    # Saves the file without opening it


#visualizar_arvore(arvore_restaurant_book)
visualizar_arvore(arvore_futebol)
