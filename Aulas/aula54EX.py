"""
Faça uma lista de comprar com listas
O usuário deve ter a possibilidade de
inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com 
erros de índices inexistentes na lista.
"""
# import os
# lista = []


# while True:
#     print('Selecione uma opção:')
#     opcao = input('[i]nserir [a]pagar [l]istar: ')

#     if opcao == 'i':
#         os.system('cls')
#         valor = input('Valor: ')
#         lista.append(valor)
#     elif opcao == 'a':
#         try:
#             apagar = int(input('Escolha o índice para apagar: '))
#             lista.pop(apagar)
#             for indice, nome in enumerate(lista):
#                     print(indice, nome)
#         except:
#                 print('Lista vazia ou índice incorreto')
#     elif opcao == 'l':
#         if lista:
#             for indice, nome in enumerate(lista):
#                 print(indice, nome)
#         else:
#             print('Nenhum valor encontrado')
#     else:
#         print('Digite uma opção válida')
        


import os

lista = []

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')

    if opcao == 'i':
        os.system('cls')
        valor = input('Valor: ')
        lista.append(valor)
    elif opcao == 'a':
        indice_str = input('Escolha o índice para apagar: ')
        try:
            indice = int(indice_str)
            del lista[indice]
        except ValueError:
            print('Por favor digite número inteiro.')
        except IndexError:
            print('Índice não existe na lista')
        except Exception:
            print('Erro desconhecido')
    elif opcao == 'l':
        os.system('cls')

        if len(lista) == 0:
            print('Nada para listar')

        for i, valor in enumerate(lista):
            print(i, valor)
    else:
        print('Por favor, escolha i, a ou l.')      

    