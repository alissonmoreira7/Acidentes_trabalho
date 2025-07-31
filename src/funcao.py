#PROBLEMA: LOOPING NA FUNÇÃO DE CADASTRO E NÃO ESTÁ COLOCANDO OS DADOS NO ARQUIVO CSV.
import csv
import os
from tkinter import *
from tkinter import messagebox
from datetime import datetime
from config import ARQUIVO

#Obtendo o último id
def obter_ultimo_id():
    if not os.path.exists(ARQUIVO) or os.stat(ARQUIVO).st_size == 0: #Verificando a existência ou se tem algo dentro do arquivo.
        return 0
    with open(ARQUIVO, 'r') as file:
        linhas = list(csv.reader(file)) 
        if len(linhas) <= 1: #Se linhas tem uma ou nada de conteúdo quer dizer que ou tem o cabeçalho ou nada.
             return 0
        return int(linhas[-1][0])

#Cadastar reclamação
def cadastrar_reclamacao():
    janela_cad = Toplevel()
    janela_cad.title('Cadastrar reclamação')

    # Labels (textos fixos)
    Label(janela_cad, text='Tipo da reclamação: ').grid(column=0, row=0)
    Label(janela_cad, text='Local: ').grid(column=0, row=1)
    Label(janela_cad, text='Data: ').grid(column=0, row=2)

    tipo_entry = Entry(janela_cad)
    local_entry = Entry(janela_cad)
    data_entry = Entry(janela_cad)

    tipo_entry.grid(column=1, row=0)
    local_entry.grid(column=1, row=1)
    data_entry.grid(column=1, row=2)

    def salvar():
        tipo = tipo_entry.get()
        local = local_entry.get()
        data = data_entry.get

        if not tipo or not local or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        

#Visualizando as reclamações do arquivo .CSV
def visualizar_reclamacoes():
    if not os.path.exists(ARQUIVO) or os.stat(ARQUIVO).st_size == 0:
        print('Atenção! Nenhuma reclamação cadastradas.')
        return
    
    with open(ARQUIVO, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]}")
