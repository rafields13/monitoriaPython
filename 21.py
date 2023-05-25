# Faça um programa que receba n números inteiros, e todos os números menores ou igual a 0 passem a ser 1.

q = int(input('Digite um número, por favor: '))
for i in range(q):
    x = int(input('Digite um outro número, por favor: '))
    if x <= 0:
        x = 1
    print(f'{x}')
