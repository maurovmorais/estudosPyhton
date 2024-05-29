try:
    a = int(input('Digite um numero: '))
    b = int(input('Digite um numero: '))
    res = a/b
except ZeroDivisionError as err:
    print(f'Não pode dividir por zero - {err.__class__}')
except ValueError as err:
    print(f'Valor informado: {err.__class__} - {err.__cause__}')
except Exception as err:
    print(f'Erro não esperado: {err.__class__}')
else:
    print(f'Resultado é:  {res}')
finally:
    print('Volte logo!')
    
    
    