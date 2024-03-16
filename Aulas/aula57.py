"""
Listas de listas e seus indices
"""

salas = [
    # 0        1
    ['Maria', 'Helena',],  # 0
    # 0 
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# print(salas[2][2])
# print(salas[2][3][2])

for sala in salas:
    print(f'sala é {sala}')
    for aluno in sala:
        print(aluno)
        