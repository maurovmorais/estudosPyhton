import tkinter as tk
import datetime


def executar_codigo():
    
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
        
    # Coloque aqui o código que deseja executar 
    print("O código foi executado com sucesso!")

# Criar a janela
janela = tk.Tk()

# Adicionar um botão
botao = tk.Button(janela, text="Executar Código", command=executar_codigo)
botao.pack()

# Rodar o loop da janela
janela.mainloop()