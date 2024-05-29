
import pandas as pd

funcionarios = {
    'Nome': ['Mauro', 'Felipe', 'Lucas'],
    'Idade': [53, 16, 20],
    'Escolaridade': ['Superior', 'Ensino Medio', 'Cursando']
}

df_dicionario = pd.DataFrame(funcionarios)

# print(df_dicionario)

for indice, linha in df_dicionario.iterrows():
    dic = linha.to_dict()
    print(dic)
    print(dic['Nome'])
    print(dic['Idade'])
    print(dic['Escolaridade'])
