notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0]]


def media(lista: list = [0]) -> float:
    """ Funçao para calcular a media de notas passadas por uma lista
    Parametro: lista
    retorna: calculo
    """
    calculo = sum(lista) / len(lista)

    return calculo


# lista Comprehension
medias = [round(media(nota), 1) for nota in notas]
print(medias)

# nomes estudantes
cadastro = [('Joao', 'Joca'), ('Maria', 'Santa'), ('Jose', 'ZZ')]

# Gerando a lista de nomes extraindo da tupla
nomes = [nome[0] for nome in cadastro]
print(nomes)

# usando o Zip
estudantes = list(zip(nomes, medias))
print(estudantes)

# Gerando a lista de pessoas candidatos a bolsa
candidatos = [estudante[0] for estudante in estudantes if estudante[1] >= 8.0]
print(candidatos)

# Desempacotar uma tupla em mais tuplas
cadastro = [('Joao', 'Joca'), ('Maria', 'Santa'), ('Jose', 'ZZ')]
nome, apelido = zip(*cadastro)
print('nome = ', nome)
print('apelido = ', apelido)
