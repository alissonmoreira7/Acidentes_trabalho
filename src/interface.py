from tkinter import *
from funcao import visualizar_reclamacoes, cadastrar_acidente

def interface_grafica():
    janela = Tk()
    janela.title('Menu')
    janela.geometry('300x200')

    text1 = Label(janela, text='Acidentes de Trabalho')
    text1.grid(column=1, row=1, padx=50)

    bt1 = Button(janela, text='Cadastrar Acidente', command=cadastrar_acidente)
    bt1.grid(column=1, row=2, padx=50)
    
    janela.mainloop()

interface_grafica()