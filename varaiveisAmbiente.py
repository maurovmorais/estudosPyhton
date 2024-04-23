import os
from config import database_infos

EMAIL = os.environ['EMAIL']
NOME = os.environ['Nome']

print(EMAIL)
print(NOME)


print(database_infos)

print(database_infos['port'])

