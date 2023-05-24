# Faça um algoritmo que crie uma função que receba duas variáveis e retorne a multiplicação entre elas.

def multiplication(x, y):
    return x * y


if __name__ == '__main__':
    a = int(input('Digite um número, por favor: '))
    b = int(input('Digite outro número, por favor: '))
    print(multiplication(a, b))
