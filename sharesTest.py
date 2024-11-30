from arvore import construir_arvore, prever
import yfinance as yf
import pandas as pd
import numpy as np

#código 100% do gpt

# Baixar os dados históricos da Petrobras (PETR4.SA) no Yahoo Finance
acao = yf.Ticker("PETR4.SA")
dados_hist = acao.history(period="1y")  # Dados dos últimos 1 ano

# Exibindo as primeiras linhas dos dados
print(dados_hist.head())

# Adicionando indicadores técnicos (exemplo: Média Móvel de 20 dias e 50 dias)
dados_hist['MA20'] = dados_hist['Close'].rolling(window=20).mean()
dados_hist['MA50'] = dados_hist['Close'].rolling(window=50).mean()

# Indicador RSI (Relative Strength Index)
def calcular_rsi(data, period=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).fillna(0)
    loss = (-delta.where(delta < 0, 0)).fillna(0)
    
    avg_gain = gain.rolling(window=period).mean()
    avg_loss = loss.rolling(window=period).mean()
    
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))
    
    return rsi

dados_hist['RSI'] = calcular_rsi(dados_hist['Close'])

# Definir a classe de compra ou venda
# Exemplo: Se o preço de fechamento subiu mais de 1% no dia seguinte, é "Compra", caso contrário, é "Venda"
dados_hist['Proxima_Variacao'] = dados_hist['Close'].shift(-1) - dados_hist['Close']
dados_hist['Classe'] = np.where(dados_hist['Proxima_Variacao'] > 0, 'Compra', 'Venda')

# Selecionar as variáveis para a árvore de decisão
# Usando preço de fechamento, médias móveis e RSI como atributos
dados_modelo = dados_hist[['Close', 'MA20', 'MA50', 'RSI', 'Classe']].dropna()

# Exibindo os dados preparados
print(dados_modelo.tail())

# Agora você pode usar os dados para treinar a árvore de decisão
# Vamos separar as variáveis de entrada (X) e a classe (y)
X = dados_modelo[['Close', 'MA20', 'MA50', 'RSI']]
y = dados_modelo['Classe']

# Você pode então usar a função 'construir_arvore' e 'prever' que você já tem
# por exemplo:
# arvore = construir_arvore(X, y)

arvore_shares = construir_arvore(X,y)


exemplo = pd.Series({
    'Close': 30.00,
    'MA20': 29.50,
    'MA50': 28.75,
    'RSI': 55.00
})

# Usar a função 'prever' para fazer a previsão
previsao = prever(arvore_shares, exemplo)

print(f"A previsão para o próximo movimento da ação é: {previsao}")

