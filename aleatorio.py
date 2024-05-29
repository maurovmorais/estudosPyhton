from random import randrange, sample

lista = []

for i in range(0, 20):
    if i not in lista:
        lista.append(randrange(1, 60, 1))

print(sorted(sample(lista, 6)))
