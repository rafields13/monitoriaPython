n = int(input('Digite um número para entrar no loop. (Caso queira sair, digite -1). '))
q = 0
soma = 0
numeros_pares = []
porcentagem_numeros_pares = 0

while n != -1:
    x = int(input('Digite um número, por favor: '))

    if x == -1:
        break

    if x % 2 == 0:
        numeros_pares.append(x)

    q += 1
    soma += x
    porcentagem_numeros_pares = len(numeros_pares) / q * 100

media = soma / q
print(q, soma, media, porcentagem_numeros_pares)
