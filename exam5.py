salario = float(input('Digite o salário aqui, por favor: '))

if salario <= 0:
    print('O salário é inválido!')
elif 1200 > salario > 0:
    print('O salário está fora de legislação!')
else:
    print('O salário está dentro da legislação!')
