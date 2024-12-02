import graphviz
from usandoLibArvore import arvore_futebol, arvore_restaurant_book, arvore_restaurante


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
    grafo.render(view=False)  # Saves the file without opening it


visualizar_arvore(arvore_restaurant_book)
#visualizar_arvore(arvore_futebol)
#visualizar_arvore(arvore_restaurante)
