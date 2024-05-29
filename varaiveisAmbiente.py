import os

EMAIL = os.environ['EMAIL']
NOME = os.environ['Nome']

print(EMAIL)
print(NOME)

from config import database_infos

print(database_infos)
print(database_infos['port'])
