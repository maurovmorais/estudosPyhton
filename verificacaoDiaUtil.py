import holidays



import datetime

# Lista de feriados nacionais do Brasil
feriados_nacionais = [
    (1, 1),    # Ano Novo
    (4, 21),   # Tiradentes
    (5, 1),    # Dia do Trabalho
    (9, 7),    # Independência do Brasil
    (10, 12),  # Nossa Senhora Aparecida
    (11, 2),   # Finados
    (11, 15),  # Proclamação da República
    (12, 25)   # Natal
]

def is_segundo_dia_util(dt):
    # Verifica se é segunda-feira e se é o segundo dia do mês
    return dt.weekday() == 0 and dt.day == 2

def is_feriado_nacional(dt):
    # Verifica se a data corresponde a um feriado nacional do Brasil
    return (dt.month, dt.day) in feriados_nacionais

def is_segundo_dia_util_com_feriado(dt):
    # Verifica se é o segundo dia útil do mês considerando os feriados nacionais
    if is_segundo_dia_util(dt) and not is_feriado_nacional(dt):
        return True
    return False

# Data para verificar
data_verificar = datetime.date(2024, 4, 2)

if is_segundo_dia_util_com_feriado(data_verificar):
    print("É o segundo dia útil do mês considerando os feriados nacionais do Brasil.")
else:
    print("Não é o segundo dia útil do mês considerando os feriados nacionais do Brasil.")