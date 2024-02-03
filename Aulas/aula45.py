"""
Iterável ->  str, range, etc
Interador -> quem sabe entregar um valor por vez 
next -> me entregue o próximo valor 
iter -> me entregue seu iterador 
"""
# texto = iter('Caique') # __iter__()

# print(next(texto))

# for item in texto
texto = 'Caique' # iterável
# iterador = iter(texto) # iterator

# while True:  
#     try:
#         letra = next(iterador)
#         print(letra)
#     except StopIteration:
#         break

for letra in texto:
    print(letra)
