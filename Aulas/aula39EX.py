"""
Interando strings com while
"""
#       01234
# nome = 'Caque'  #Iteráveis
#      -54321
# f'{string[:3]}ABC{string[4:]}
nome = 'Caique'
nome_com = ''

i = 0
while i < len(nome):
    letra = nome[i]
    nome_com += f'*{letra}'
    i += 1
    
print(nome_com )






