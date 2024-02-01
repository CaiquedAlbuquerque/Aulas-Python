# Calculadora com while #

# numero1 = int(input('Digite um número: '))

# print('      ')
# print('---TABUADA---')
# print('      ')
# for numeros in range(1, 11):
#     print('=' * 13 )
#     soma = numero1 * numeros
#     print(f'{numero1:^2} x  {numeros:^2} = {soma:^2}')


while True:
    num_1 = input('Digite um número: ')   
    operador = input('Digite o operador (+-/*): ')
    num_2 = input('Digite outro número: ')
    numeros_validos = None
    num_1_float = 0
    num_2_float = 0
    
    try:               
        num_1_float = float(num_1)
        num_2_float = float(num_2)
        numeros_validos = True    
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Um ou ambos os números digitados são inválidos')
        continue
    
    operadores_permitidos = '+-/*'
    
    if operador not in operadores_permitidos:
        print('Operador inválido')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

        
    if operador == '+':
        soma = num_1_float + num_2_float
        print(f'O resultado entre {num_1_float} e {num_2_float} é {num_1_float + num_2_float}')             
    elif operador == '-':
        print(f'O resultado entre {num_1_float} e {num_2_float} é {num_1_float - num_2_float})')           
    elif operador == '/':
        print(f'O resultado entre {num_1_float} e {num_2_float} é {num_1_float / num_2_float}')          
    elif operador == '*':
        print(f'O resultado entre {num_1_float} e {num_2_float} é {num_1_float * num_2_float}')
    else:
        print('Nunca deveria chegar aqui')
        
        
        
    sair = input('Deseja sair? [s]im:').lower().startswith('s')
    
    if sair is True:
        break
        
        
    
        
