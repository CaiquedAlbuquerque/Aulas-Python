"""
Interando strings com while
"""
#       01234
# nome = 'Caque'  #Iteráveis
#      -54321
# f'{string[:3]}ABC{string[4:]}
nome = 'Caique'
nome_len = len(nome)
nome_com = ''

i = 0
nome_com = ''
while i < len(nome):
    letra = nome[i]
    nome_com += f'*{letra}'
    i += 1
    
print(nome_com )






