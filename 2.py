# Crie um programa que receba um nome e um número pelo teclado, em seguida, o programa deve imprimir:

# a) Uma saudação ao nome digitado pelo usuário.

name = input('Digite o nome aqui, por favor: ')
print(f'Como é bom te conhecer, {name}!')

# b) O nome multiplicado por um número também inserido pelo usuário.

x = int(input('Digite um número, por favor: '))
nameTimesX = name * x
print(f'O nome multiplicado pelo número é {nameTimesX}.')
