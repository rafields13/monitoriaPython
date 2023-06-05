# Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 e 10. O usuário deve
# informar de qual número ele deseja ver a tabuada. A saída deve ser conforme os exemplos abaixo:

# a) Faça uma tabuada usando FOR e um WHILE.

x = int(input('Type a number, please: '))

while x < 1 or x > 10:
    print('This number is INVALID! Type again, please.')
    x = int(input('Type a number, please: '))

print(f'Multiplication table of number {x}:')

for i in range(1, 11):
    result = x * i
    print(x, 'x', i, '=', result

# b) Faça um código, usando FOR, que mostre todas as tabuadas (1 até 10).

for i in range(1, 11):
    for p in range(1, 11):
        result = i * p
        print(i, 'x', p, '=', result)
