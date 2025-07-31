from tkinter import *
from funcao import visualizar_reclamacoes, cadastrar_reclamacao

def interface_grafica():
    janela = Tk()
    janela.title('Menu')
    janela.geometry('300x200')

    text1 = Label(janela, text='Transportes da Bahia')
    text1.grid(column=1, row=1, padx=50)

    bt1 = Button(janela, text='Cadastrar Reclamação', command=cadastrar_reclamacao)
    bt1.grid(column=1, row=2, padx=50)
    

    janela.mainloop()

interface_grafica()