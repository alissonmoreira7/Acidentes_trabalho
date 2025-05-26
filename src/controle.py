import csv
import os
from datetime import datetime
from funcao import menu

while True:

    menu()
    while True:

        opcao = int(input('Digite a sua opção: '))

        if opcao not in (1, 2, 3):
             print('Erro! Tente digitar um valor entre 1 e 3.')
             continue
        else:
             break

    # Cadastrar mais reclamações
    if opcao == 1:
                count = 0
                file_path = "../data/reclamacoes.csv"
                
                with open(file_path, 'a', newline='') as r2:
                    df_csv = csv.writer(r2)
                    
                    # Cabeçalho da tabela
                    if os.stat(file_path).st_size == 0:
                        df_csv.writerow(('id', 'tipo', 'local', 'data')) #Cabeçalho
                    
                    while True:
                        # Itens da tabela
                        tipo = input('Qual é o tipo da sua reclamação? ')
                        local = input('Qual foi o local da ocorrência? ')

                        try:
                            date = input('Qual foi a data do ocorrido? (DD/MM/AAAA): ')
                            datetime.strptime(date, "%d/%m/%Y")
                            
                        except ValueError:
                            print("Data inválida! Use o formato DD/MM/AAAA.")
                            continue

                        # Verificação do preenchimento correto dos campos
                        if tipo and local and date:
                            count += 1
                            df_csv.writerow((count, tipo, local, date))

                        else:
                            print("Todos os campos são obrigatórios!")

                        escolha = input('Você deseja cadastrar outra reclamação? [S/N]').lower()
                        if escolha != 's':
                            break


            #Visualizar os dados das reclamações
    elif opcao == 2:
                with open("../data/reclamacoes.csv", 'r') as r2:
                    df_csv = csv.reader(r2, delimiter=',')

                    for linha in df_csv:
                        print(linha)

    elif opcao == 3:
        print("Saindo do programa...")
        break