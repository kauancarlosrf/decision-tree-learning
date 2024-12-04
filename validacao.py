from arvore import prever

def validar_modelo(arvore, conjunto_validacao):
    acertos = 0
    total = len(conjunto_validacao)

    if total == 0:
        print("Nenhum exemplo para teste.")
        return 0

    for _, exemplo in conjunto_validacao.iterrows():
        # Remover 'decisao*' da Série diretamente (sem axis=1)
        entrada = exemplo.drop('decisao*').to_dict()  # Remove a coluna 'decisao*' diretamente
        resposta_real = exemplo['decisao*']
        
        resposta_prevista = prever(arvore, entrada)
        
        if resposta_prevista == resposta_real:
            acertos += 1

    proporcao_acertos = acertos / total
    print(f"Proporção de acertos: {proporcao_acertos:.2%}")
    return proporcao_acertos
