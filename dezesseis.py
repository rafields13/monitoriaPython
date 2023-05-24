# Crie uma função que receba dois parâmetros e faça a soma, produto, divisão e subtração desses parâmetros. Após isso,
# implemente a aplicação dessa função em outro programa e mostre o resultado no segundo programa.

def operations(x, y):
    print(x + y)
    print(x - y)
    print(x * y)
    print(x / y)


if __name__ == '__main__':
    a = int(input('Digite um número, por favor: '))
    b = int(input('Digite um número, por favor: '))
    operations(a, b)
