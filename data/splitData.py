
def split_data(dataFrame):
  
  #df = pd.read_csv('./dataset_credito_1000_linhas_balanceadas.csv').dropna()
  df_validacao = dataFrame.sample(frac=0.1, random_state=42).reset_index(drop=True)
  df_treino = dataFrame.drop(df_validacao.index).reset_index(drop=True)
  
  return df_treino, df_validacao
