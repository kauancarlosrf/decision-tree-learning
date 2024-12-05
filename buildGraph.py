import graphviz
from usandoLibArvore import arvore_futebol, arvore_restaurant_book, arvore_restaurante, arvore_credito

def visualizar_arvore(no):
    def construir_grafo(no, grafo, caminho=''):
        if no.folha:
            grafo.node(caminho, f'{no.classe}', shape='box', style='filled', color='lightgrey')
        else:
            grafo.node(caminho, f'{no.atributo}')
            for filho in no.filhos:
                novo_caminho = f'{caminho}->{filho.valor}'
                grafo.edge(caminho, novo_caminho, label=f'{filho.valor}')
                construir_grafo(filho, grafo, novo_caminho)
    
    # Ajustando ranksep para aumentar a distância entre as camadas
    grafo = graphviz.Digraph("arvore_credito", format='pdf', graph_attr={'size': '1000,1000', 'ranksep': '2'})
    construir_grafo(no, grafo)
    grafo.render(view=False)  # Saves the file without opening it

#visualizar_arvore(arvore_restaurant_book)
#visualizar_arvore(arvore_futebol)
#visualizar_arvore(arvore_restaurante)
visualizar_arvore(arvore_credito)
