# Desenvolva um programa que leia n números e mostre estas informações:

# a) A quantidade de elementos dados;

# b) A soma dos valores;

# c) A média dos valores; e

# d) A porcentagem de números pares.

x = 0
sum = 0
counter = 0
pairsNumbers = 0

while x != -1:

    x = int(input('Digite um número, por favor: \nObs: Caso queira sair, digite -1.'))

    if x == -1:
        break

    sum += x
    counter += 1

    if x % 2 == 0:
        pairsNumbers += 1

print(f'A quantidade de números é: {counter}.')
print(f'A soma dos n números é: {sum}.')

average = sum / counter
print(f'A média dos números informados é: {average}')

porcentagePairsNumbers = (pairsNumbers / counter) / 100
print(f'A porcentagem de números pares correspondem a: {porcentagePairsNumbers:.1f}')
