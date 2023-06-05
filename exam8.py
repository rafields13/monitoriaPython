n = int(input('Digite um número para poder digitar a senha. (Caso queira sair, digite -1). '))

while n != -1:
    x = int(input('Digite a senha, por favor: '))

    if x == 2002:
        print('Acesso permitido!')
        break
    else:
        print('Senha inválida!')
