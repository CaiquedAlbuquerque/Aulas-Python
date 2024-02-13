"""
enumerate - enumera iteráveis (indices)
"""
lista = ['Maria', 'Helena', 'Luiz']
lista.append('João')


for indice, nomes in enumerate(lista):
    print(indice, nomes)

# for item in enumerate(lista):
#     indice, nome = item
#     print(indice, item)
    
# for tupla_enumerada in enumerate(lista):
#     print('FOR da tupla')
#     for valor in tupla_enumerada:
#         print(f'\t{valor}')

