# Exemplo de dados


dataSetRestaurante = [
    {'preço': 'caro', 'dia_da_semana': 'sexta', 'está_chovendo': 'sim', 'vai_esperar': 'sim'},
    {'preço': 'médio', 'dia_da_semana': 'sexta', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
    {'preço': 'barato', 'dia_da_semana': 'sexta', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
    {'preço': 'caro', 'dia_da_semana': 'sábado', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
    {'preço': 'barato', 'dia_da_semana': 'sábado', 'está_chovendo': 'sim', 'vai_esperar': 'sim'},
    {'preço': 'médio', 'dia_da_semana': 'sábado', 'está_chovendo': 'sim', 'vai_esperar': 'sim'},
    {'preço': 'caro', 'dia_da_semana': 'segunda', 'está_chovendo': 'não', 'vai_esperar': 'sim'},
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


dataSetFutebol = [
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'talvez'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'talvez'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'frio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'perder'},
    {'temperatura': 'quente', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'frio', 'hora_do_jogo': 'tarde', 'condicao_do_campo': 'ruim', 'resultado': 'perder'},
    {'temperatura': 'medio', 'hora_do_jogo': 'noite', 'condicao_do_campo': 'bom', 'resultado': 'vencer'},
    {'temperatura': 'medio', 'hora_do_jogo': 'manha', 'condicao_do_campo': 'ruim', 'resultado': 'vencer'}
]

data_frame_dados_futebol = []
data_frame_decisoes_futebol = []

for amostra in dataSetFutebol:
    atributos = {k: v for k, v in amostra.items() if k != 'resultado'}
    classe = amostra['resultado']
    
    data_frame_dados_futebol.append(atributos)
    data_frame_decisoes_futebol.append(classe)


dataSetRestaurantBook = [
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Some", "Price": "$$$", "Rain": "No", "Res": "Yes", "Type": "French", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "No", "Res": "Yes", "Type": "Thai", "Est": "30-60", "WillWait": "No"},
    {"Alt": "No", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Some", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "No", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "Yes", "Res": "Yes", "Type": "Thai", "Est": "10-30", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "No", "Fri": "No", "Hun": "No", "Pat": "Full", "Price": "$$$", "Rain": "No", "Res": "Yes", "Type": "French", "Est": ">60", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Some", "Price": "$$", "Rain": "Yes", "Res": "No", "Type": "Italian", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "No", "Bar": "No", "Fri": "No", "Hun": "No", "Pat": "None", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "No"},
    {"Alt": "No", "Bar": "No", "Fri": "No", "Hun": "Yes", "Pat": "Some", "Price": "$$", "Rain": "Yes", "Res": "Yes", "Type": "Thai", "Est": ">60", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "No", "Hun": "Yes", "Pat": "Full", "Price": "$$$", "Rain": "No", "Res": "Yes", "Type": "Burger", "Est": "10-30", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "No", "Pat": "Full", "Price": "$$", "Rain": "Yes", "Res": "Yes", "Type": "Italian", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "No", "Bar": "Yes", "Fri": "No", "Hun": "Yes", "Pat": "None", "Price": "$", "Rain": "No", "Res": "No", "Type": "Thai", "Est": "30-60", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "No", "Pat": "Full", "Price": "$$", "Rain": "Yes", "Res": "Yes", "Type": "Italian", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "No", "Bar": "Yes", "Fri": "No", "Hun": "Yes", "Pat": "None", "Price": "$", "Rain": "No", "Res": "No", "Type": "Thai", "Est": "30-60", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "No", "Pat": "Full", "Price": "$$", "Rain": "Yes", "Res": "Yes", "Type": "Italian", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "No", "Bar": "Yes", "Fri": "No", "Hun": "Yes", "Pat": "None", "Price": "$", "Rain": "No", "Res": "No", "Type": "Thai", "Est": "30-60", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "No", "Pat": "Full", "Price": "$$", "Rain": "Yes", "Res": "Yes", "Type": "Italian", "Est": "0-10", "WillWait": "Yes"},
    {"Alt": "No", "Bar": "Yes", "Fri": "No", "Hun": "Yes", "Pat": "None", "Price": "$", "Rain": "No", "Res": "No", "Type": "Thai", "Est": "30-60", "WillWait": "No"},
    {"Alt": "Yes", "Bar": "Yes", "Fri": "Yes", "Hun": "Yes", "Pat": "Full", "Price": "$", "Rain": "No", "Res": "No", "Type": "Burger", "Est": "0-10", "WillWait": "Yes"}
    
]

data_frame_dados_restaurant_book = []
data_frame_decisoes_restaurant_book = []

for amostra in dataSetRestaurantBook:
    atributos = {k: v for k, v in amostra.items() if k != 'WillWait'}
    classe = amostra['WillWait']
    
    data_frame_dados_restaurant_book.append(atributos)
    data_frame_decisoes_restaurant_book.append(classe)
