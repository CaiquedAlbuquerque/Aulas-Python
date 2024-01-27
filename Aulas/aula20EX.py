# try:  
#     primeiro_valor = int(input('Digite um valor: '))
#     segundo_valor = int(input('Digite outro valor: '))
    
#     if primeiro_valor > segundo_valor:
#         print(f'O primeiro valor "{primeiro_valor}" é maior do que o segundo valor "{segundo_valor}"')
#     elif segundo_valor > primeiro_valor:
#         print(f'O segundo valor "{segundo_valor}" é maior do que o primeiro valor "{primeiro_valor}"')
#     elif primeiro_valor == segundo_valor:
#         print('Os dois tem o mesmo valor')
# except:
#     print('Digite um número válido')
    
    
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite outro valor: ')

if primeiro_valor >= segundo_valor:
    print(
        f'{primeiro_valor=} é maior ou igual '
        f'ao que {segundo_valor=}'
    )
else:
    print(
        f'{segundo_valor=} é maior '
        f'do que {primeiro_valor=}'
    )
