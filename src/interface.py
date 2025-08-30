from tkinter import *
from funcao import visualizar_acidentes, cadastrar_acidente

def interface_grafica():
    janela = Tk()
    janela.title('Menu')
    janela.geometry('400x300')
    
    text1 = Label(janela, text='Cadastro de Acidentes de Trabalho')
    text1.grid(column=0, row=1,  padx= 50, pady= 10)

    #Botão de cadastro de acidentes
    bt1 = Button(janela, text='Cadastrar Acidente', command=cadastrar_acidente)
    bt1.grid(column=0, row=2,  padx= 50, pady= 10)
  
    #Botão para ver os acidentes
    bt2 = Button(janela, text='Ver Acidente', command=visualizar_acidentes)
    bt2.grid(column=0, row=3, padx= 50, pady= 10)

    def sair_janela():
        janela.destroy()

    #Botão para sair
    bt3 = Button(janela, text='Sair', command=sair_janela)
    bt3.grid(column=0, row=4, padx=50, pady=10)

    janela.mainloop()


interface_grafica()