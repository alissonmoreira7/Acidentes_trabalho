import csv
import os
from datetime import datetime
from config import ARQUIVO

#Menu de controle do programa
def menu():
    print('-=-'*15)
    print(' '*9, 'Cadastro de Reclamações')
    print('-=-'*15)
    print('Cadastrar reclamação   [ 1 ]')
    print('Visualizar reclamações [ 2 ]')
    print('Sair do programa       [ 3 ]')

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
    os.makedirs(os.path.dirname(ARQUIVO), exist_ok=True)
    
    ultimo_id = obter_ultimo_id()
    with open(ARQUIVO,'a', newline='') as arquivo:
        dados_arquivo = csv.writer(arquivo)

        if os.stat(ARQUIVO).st_size == 0: #Se está vazio, insira o cabeçalho.
            dados_arquivo.writerow(['id', 'tipo', 'local', 'data'])

        while True:
            tipo = input('Qual é o tipo da sua reclamação? ').strip()
            local = input('Qual foi o local da ocorrência? ').strip()
            date = input('Qual foi a data do ocorrido? (DD/MM/AAAA): ').strip()

            #Válidando a entrada correta da data e formatada.
            try:
                datetime.strptime(date, "%d/%m/%Y")
            except ValueError:
                print('Data inválida! Use o formato DD/MM/AAAA.')
                continue 

            if tipo and local and date:
                ultimo_id += 1
                dados_arquivo.writerow([ultimo_id, tipo, local, date])
                print('Reclamação cadastrada com sucesso!!!')
            else:
                print('Todos os campos são necessários!!!')

#Visualizando as reclamações do arquivo .CSV
def visualizar_reclamacoes():
    if not os.path.exists(ARQUIVO) or os.stat(ARQUIVO).st_size == 0:
        print('Atenção! Nenhuma reclamação cadastradas.')
        return
    
    with open(ARQUIVO, 'r') as arquivo:
        leitor = csv.reader(arquivo)
        for linha in leitor:
            print(f"{linha[0]:<4} | {linha[1]:<20} | {linha[2]:<20} | {linha[3]}")