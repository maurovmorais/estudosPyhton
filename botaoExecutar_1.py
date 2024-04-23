import tkinter as tk
import subprocess

def executar_script():
    subprocess.Popen(['python', 'manipulando_datas.py'])

# Crie a janela principal
root = tk.Tk()
root.title("Executar Script Python")

# Crie o botão para executar o script
botao_executar = tk.Button(root, text="Executar Script", command=executar_script)
botao_executar.pack()

# Execute o loop principal da interface gráfica
root.mainloop()
