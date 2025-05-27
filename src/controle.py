#Anotações
#Adicionar um banco de dados ao invés de usar um arquivo csv.
#Utilizar Programação Orientada a Objetos para modelar as reclamações.

import csv
import os
from funcao import visualizar_reclamacoes, cadastrar_reclamacao, obter_ultimo_id, menu
from config import ARQUIVO
ARQUIVO = "../data/reclamacoes.csv"

while True:
    print('Iniciando o programa...')
    menu()

    while True:
        try:
            opcao = int(input('Digite a sua opção: '))
            if opcao in (1, 2, 3):
                break
            else:
                print('Opção inválida. Digite um valor entre 1, 2 e 3!')
        except ValueError:
            print('Entrada inválida. Digite apenas números!')

    if opcao == 1:
        cadastrar_reclamacao()
    elif opcao == 2:
        visualizar_reclamacoes()
    elif opcao == 3:
        print('Saindo do programa...')
        break