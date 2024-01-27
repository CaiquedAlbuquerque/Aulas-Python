# Operadores in e not in
# Strings são interáveis
#  0 1 2 3 4 5
#  C a i q u e
# -6-5-4-3-2-1
nome = 'Caique'
# print(nome[2])
# print(nome[-4])
# print('Ca' in nome)
# print('ique' in nome)
# print(10 * '-')
# print('Cai' not in nome)
# print('zero' in nome)

nome = input('Digite o seu nome: ')
encontrar = input('Digite o que quer encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')