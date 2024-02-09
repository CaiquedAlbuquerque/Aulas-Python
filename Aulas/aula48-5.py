"""
Cuidado com dados mutáveis
= - copiador o valor (imutáveis)
= - aponta para o mesmo valor na memória (mutável)
"""
# nome = 'Caique'
# outra_variável = nome
# nome = 'João'
# print(nome)
# print(outra_variável)

lista_a = ['Caique', 'Maria', 1, True, 1.2]
lista_b = lista_a.copy()


lista_a[0] = 'Qualquer coisa'
print(lista_a)
print(lista_b)
