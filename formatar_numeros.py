import pandas as pd

# Criar um DataFrame de exemplo
data = {'Número': [3.14159, 2.71828, 1.41421]}
df = pd.DataFrame(data)

# Arredondar o número com duas casas decimais
df['Número'] = df['Número'].round(2)

# Exportar o DataFrame para um arquivo Excel
df.to_excel('numeros_formatados.xlsx',index=False)