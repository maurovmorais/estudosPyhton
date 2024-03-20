import datetime

var_dateMes = datetime.datetime.now()
var_strMes = var_dateMes.strftime("%m")
var_strMesAnoAtual = str(int(var_strMes)).zfill(2)+"_"+str(var_dateMes.strftime("%Y"))
var_strMesAnterior = str(int(var_strMes)-1).zfill(2)+"_"+str(var_dateMes.strftime("%Y"))

print(var_strMesAnoAtual)
print(var_strMesAnterior)


#Pegar o nome do mês
import calendar
import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')
 
# initializing month number
numero_mes = 9
               
# printing original month number
print("Númnero do mês : " + str(numero_mes))
 
# using month_name() to get month name
res = calendar.month_name[numero_mes]
 
# printing result
print("Nome do mês : " + str(res)[0:3])

