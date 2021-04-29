from uteis import numeros


num = int(input('Digite um numero: '))
fat = numeros.fatorial(num) # Importar def fatorial do Modulo uteis.py
print(f'O Fatorial de {num} é {fat}')
print(f'O dobro de um {num} é {numeros.dobro(num)}')