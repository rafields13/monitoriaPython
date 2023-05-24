# Crie um algoritmo que faça uma função que  receba uma variável e mostre na tela se ela é ou não um número múltiplo
# de 2.

def multiple(x):
    if x % 2 == 0:
        print(f'{x} é múltiplo de 2.')
    else:
        print(f'{x} não é múltiplo de 2.')


if __name__ == '__main__':
    a = int(input('Digite um número, por favor: '))
    multiple(a)
