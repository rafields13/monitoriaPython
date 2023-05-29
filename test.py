x = 0
sum = 0
counter = 0

while x != -1:

    x = int(input('Digite um número, por favor: '))

    if x == -1:
        break

    sum += x
    counter += 1

average = sum / counter
print(f'A média dos números informados é: {average}')
