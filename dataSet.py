# Exemplo de dados

dataSetRestaurante = [
    {'preço': 'caro', 'dia_da_semana': 'sexta', 'está_chovendo': 'sim', 'vai_esperar': 'não'},
    {'preço': 'médio', 'dia_da_semana': 'sexta', 'está_chovendo': 'não', 'vai_esperar': 'não'},
    {'preço': 'barato', 'dia_da_semana': 'sexta', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
    {'preço': 'caro', 'dia_da_semana': 'sábado', 'está_chovendo': 'não', 'vai_esperar': 'não'},
    {'preço': 'barato', 'dia_da_semana': 'sábado', 'está_chovendo': 'sim', 'vai_esperar': 'sim'},
    {'preço': 'médio', 'dia_da_semana': 'sábado', 'está_chovendo': 'sim', 'vai_esperar': 'sim'},
    {'preço': 'caro', 'dia_da_semana': 'segunda', 'está_chovendo': 'não', 'vai_esperar': 'não'},
    {'preço': 'médio', 'dia_da_semana': 'segunda', 'está_chovendo': 'sim', 'vai_esperar': 'não'},
    {'preço': 'barato', 'dia_da_semana': 'segunda', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
    {'preço': 'barato', 'dia_da_semana': 'sexta', 'está_chovendo': 'sim', 'vai_esperar': 'sim'}
]

data_frame_dados_restaurante = []
data_frame_decisoes_restaurante = []

for amostra in dataSetRestaurante:
    atributos = {k: v for k, v in amostra.items() if k != 'vai_esperar'}
    classe = amostra['vai_esperar']
    
    data_frame_dados_restaurante.append(atributos)
    data_frame_decisoes_restaurante.append(classe)


# Novo dataset para prever o resultado de um jogo de futebol com 50 casos
dataSetFutebol = [
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'vencer'}
]

data_frame_dados_futebol = []
data_frame_decisoes_futebol = []

for amostra in dataSetFutebol:
    atributos = {k: v for k, v in amostra.items() if k != 'resultado'}
    classe = amostra['resultado']
    
    data_frame_dados_futebol.append(atributos)
    data_frame_decisoes_futebol.append(classe)
