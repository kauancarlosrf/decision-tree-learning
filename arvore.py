import numpy as np
import pandas as pd
from collections import Counter


# Função para calcular a entropia
def calcular_entropia(y):
    contagem_classes = Counter(y)
    cardinalidade_do_conjunto = len(y)
    entropia = 0
    for classe, count in contagem_classes.items():
        probabilidade_classe = count / cardinalidade_do_conjunto
        entropia -= probabilidade_classe * np.log2(probabilidade_classe)
    return entropia

# Função para calcular o ganho de informação
def calcular_ganho_informacao(X, pai, atributo):
    entropia_total_pai = calcular_entropia(pai)
    ramos_de_divisoes_para_os_filhos, lista_cardinalidades_filhos = np.unique(X[atributo], return_counts=True)
    
    entropia_condicional_de_todos_filhos = 0
    for ramo_filho, cardinalidade_filho in zip(ramos_de_divisoes_para_os_filhos, lista_cardinalidades_filhos):
        filho = pai[X[atributo] == ramo_filho]
        peso_filho = cardinalidade_filho / len(pai)
        entropia_condicional_de_todos_filhos += peso_filho * calcular_entropia(filho)
    
    ganho_informacao = entropia_total_pai - entropia_condicional_de_todos_filhos
    return ganho_informacao

# Função para encontrar o melhor atributo para dividir os dados
def encontrar_abtributo_com_ganho_informacao_maximo(data_set, lista_decisoes):
    ganhos = {atributo: calcular_ganho_informacao(data_set, lista_decisoes, atributo) for atributo in data_set.columns}
    #print(ganhos)
    return max(ganhos, key=ganhos.get)

# Definição da classe do nó da árvore de decisão
class No:
    def __init__(self, atributo=None, valor=None, folha=False, classe=None, filhos=None):
        self.atributo = atributo
        self.valor = valor
        self.folha = folha
        self.classe = classe
        self.filhos = filhos or []

# Função para construir a árvore de decisão recursivamente
def construir_arvore(dados_data_set_cru, decisoes_data_set_cru):
    # Arrumando dados
    data_set = pd.DataFrame(dados_data_set_cru)
    lista_decisoes_data_set = pd.Series(decisoes_data_set_cru)

    # Verifica se todas as amostras têm a mesma classe
    if len(set(classe=lista_decisoes_data_set.iloc[0])) == 1:
        return No(folha=True, classe=classe=lista_decisoes_data_set.iloc[0].iloc[0])
    
    # Se não houver atributos restantes, retorna a classe majoritária
    if data_set.empty:
        classe_majoritaria = classe=lista_decisoes_data_set.iloc[0].mode()[0]
        return No(folha=True, classe=classe_majoritaria)

    # Encontrar o melhor atributo para dividir
    melhor_atributo = encontrar_abtributo_com_ganho_informacao_maximo(data_set, classe=lista_decisoes_data_set.iloc[0])
    raiz = No(atributo=melhor_atributo)
    
    # Criar nós filhos para cada valor do atributo
    for valor in data_set[melhor_atributo].unique():
        data_set_sub = data_set[data_set[melhor_atributo] == valor].drop(columns=melhor_atributo)
        lista_decisoes_data_set_sub = classe=lista_decisoes_data_set.iloc[0][data_set[melhor_atributo] == valor]
        
        filho = construir_arvore(data_set_sub, lista_decisoes_data_set_sub)
        filho.valor = valor
        raiz.filhos.append(filho)
    
    return raiz

# Função para fazer previsões com a árvore de decisão
def prever(arvore, exemplo):
    while not arvore.folha:
        atributo_valor = exemplo[arvore.atributo]
        arvore = next((filho for filho in arvore.filhos if filho.valor == atributo_valor), None)
        if arvore is None:
            return None  # Caso não encontre um caminho
    return arvore.classe

