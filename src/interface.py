from tkinter import *
from funcao import visualizar_acidentes, cadastrar_acidente

def interface_grafica():
    janela = Tk()
    janela.title('Menu')
    janela.geometry('300x200')
    
    text1 = Label(janela, text='Acidentes de Trabalho')
    text1.grid(column=1, row=1, padx=50)

    #Botão de cadastro de acidente
    bt1 = Button(janela, text='Cadastrar Acidente', command=cadastrar_acidente)
    bt1.grid(column=1, row=2, padx=50)
    
    #Botão para ver os acidentes
    bt2 = Button(janela, text='Ver Acidente', command=visualizar_acidentes)
    bt2.grid(column=1, row=3, padx=50)

    janela.mainloop()

interface_grafica()