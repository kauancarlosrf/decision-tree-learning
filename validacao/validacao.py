from arvore import prever, construir_arvore

# teste ainda bagunçado

def testar_modelo(arvore, exemplos_teste):
    acertos = 0
    total = len(exemplos_teste)

    for index, exemplo in exemplos_teste.iterrows():
        # Remove a coluna de decisão para prever apenas com atributos
        entrada = exemplo.drop('decisao*').to_dict()
        resposta_real = exemplo['decisao*']
        
        # Chama a função prever() da sua árvore de decisão
        resposta_prevista = prever(arvore, entrada)
        
        # Compara a previsão com a resposta real
        if resposta_prevista == resposta_real:
            acertos += 1

    proporcao_acertos = acertos / total
    print(f"Proporção de acertos: {proporcao_acertos:.2%}")
    return proporcao_acertos

# Exemplo de uso:
import pandas as pd

# Carregar o dataset e dividir 10% para validação
df = pd.read_csv('seu_dataset.csv')
df_validacao = df.sample(frac=0.1, random_state=42)
df_treino = df.drop(df_validacao.index)

# Construir a árvore com o conjunto de treino
arvore_credito = construir_arvore(df_treino)

# Testar a árvore com o conjunto de validação
testar_modelo(arvore_credito, df_validacao)
