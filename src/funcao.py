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
def cadastrar_acidente():
    janela_cad = Toplevel()
    janela_cad.title('Cadastrar Acidente')

    # Labels (textos fixos)
    Label(janela_cad, text='Tipo de acidente: ').grid(column=0, row=0)
    Label(janela_cad, text='Local: ').grid(column=0, row=1)
    Label(janela_cad, text='Data: ').grid(column=0, row=2)
    Label(janela_cad, text='Classificação: ').grid(column=0, row=3)

    tipo_entry = Entry(janela_cad)
    local_entry = Entry(janela_cad)
    data_entry = Entry(janela_cad)
    classificao_entry = Entry(janela_cad)

    tipo_entry.grid(column=1, row=0)
    local_entry.grid(column=1, row=1)
    data_entry.grid(column=1, row=2)
    classificao_entry.grid(column=1, row=3)

    def salvar():
        tipo = tipo_entry.get()
        local = local_entry.get()
        data = data_entry.get()
        classificacao = classificao_entry.get()

        if not tipo or not local or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos!")
            return
        
        campos = ['Tipo', 'Local', 'Data', 'Classificação']
        novo_acidente = {
            'Tipo': tipo,
            'Local': local,
            'Data': data,
            'Classificação': classificacao
        }
        
        with open(ARQUIVO, 'a', newline='', encoding='utf-8') as arquivo:
            df_csv = csv.DictWriter(arquivo, fieldnames=campos)
            
            # Cabeçalho da tabela
            if os.stat(ARQUIVO).st_size == 0:
                df_csv.writeheader() #Cabeçalho

            df_csv.writerow(novo_acidente)

        messagebox.showinfo('Sucesso', 'Acidente cadastrado com sucesso!')
        janela_cad.destroy()

    Button(janela_cad, text='Salvar', command=salvar).grid(row=4, column=0, columnspan=2)
        
#Visualizando as reclamações do arquivo .CSV
def visualizar_acidentes():

    janela_ver = Toplevel()
    janela_ver.title('Ver acidentes')

    if not os.path.exists(ARQUIVO) or os.stat(ARQUIVO).st_size == 0:
        print('Atenção! Nenhuma reclamação cadastradas.')
        return
    
    with open(ARQUIVO, 'r', encoding='utf-8') as arquivo:
        leitor = csv.reader(arquivo)

        texto = ''
        for linha in leitor:
            texto += f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]}\n"

        Label(janela_ver, text=texto, justify='left').grid(row=0, column=0)

    janela_ver.mainloop()
