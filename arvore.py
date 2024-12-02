import numpy as np
import pandas as pd
from collections import Counter


# Function to calculate entropy
def calcular_entropia(y):
    contagem_classes = Counter(y)
    cardinalidade_do_conjunto = len(y)
    entropia = 0
    for classe, count in contagem_classes.items():
        probabilidade_classe = count / cardinalidade_do_conjunto
        entropia -= probabilidade_classe * np.log2(probabilidade_classe)
    return entropia

# Function to calculate information gain
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

# Function to find the best attribute to split the data
def encontrar_melhor_atributo(df_atributos, df_lista_decisoes):
    ganhos = {atributo: calcular_ganho_informacao(df_atributos, df_lista_decisoes, atributo) for atributo in df_atributos.columns}
    #print(ganhos)
    return max(ganhos, key=ganhos.get)

# Definição da classe do nó da árvore de decisão
# Definition of the decision tree node class
class No:
    def __init__(self, atributo=None, valor=None, folha=False, classe=None, filhos=None):
        self.atributo = atributo
        self.valor = valor
        self.folha = folha
        self.classe = classe
        self.filhos = filhos or []

# Function to recursively build the decision tree
def construir_arvore(data_frame):
    # Organizing data
    df_completo = pd.DataFrame(data_frame)
    df_atributos = df_completo.drop(columns='decisao*')
    df_lista_decisoes = df_completo['decisao*']

    # Verifica se todas as amostras têm a mesma classe
    # Check if all samples have the same class
    if len(set(df_lista_decisoes)) == 1:
        return No(folha=True, classe=df_lista_decisoes.iloc[0])
    
    # If there are no remaining attributes, return the majority class
    if df_atributos.empty:
        classe_majoritaria = df_lista_decisoes.mode()[0]
        return No(folha=True, classe=classe_majoritaria)

    # Find the best attribute to split the data
    melhor_atributo = encontrar_melhor_atributo(df_atributos, df_lista_decisoes)
    raiz = No(atributo=melhor_atributo)
    
    # Criar nós filhos para cada valor do atributo
    # Create child nodes for each value of the attribute
    for valor in df_atributos[melhor_atributo].unique():
        df_atributos_sub = df_atributos[df_atributos[melhor_atributo] == valor].drop(columns=melhor_atributo)
        df_lista_decisoes_sub = df_lista_decisoes[df_atributos[melhor_atributo] == valor]
        
        filho = construir_arvore(pd.concat([df_atributos_sub, df_lista_decisoes_sub], axis=1))
        filho.valor = valor
        raiz.filhos.append(filho)
    
    return raiz

# Function to make predictions with the decision tree
def prever(arvore, exemplo):
    while not arvore.folha:
        atributo_valor = exemplo[arvore.atributo]
        arvore = next((filho for filho in arvore.filhos if filho.valor == atributo_valor), None)
        if arvore is None:
            return None  # Caso não encontre um caminho
            # If no path is found
    return arvore.classe  # Retorna a classe do nó folha
    # Returns the class of the leaf node
