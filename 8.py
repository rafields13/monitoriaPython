# Crie um programa que receba três notas de 0 até 10 (faça as validações para aceitar apenas esse intervalo),
# depois faça o cálculo da média aritmética e então mostre a média calculada e também se o aluno passou ou não. A
# escola aceita notas 7 (sete) acima para aprovação.

x = float(input('Digite a primeira nota aqui, por favor: '))
y = float(input('Digite a segunda nota aqui, por favor: '))
z = float(input('Digite a terceira nota aqui, por favor: '))

if x > 10 or x < 0 or y > 10 or y < 0 or z > 10 or z < 0:
    print('Pelo menos uma das notas digitadas é inválida!')
else:
    average = (x + y + z) / 3
    if average >= 7:
        print('Você foi aprovado!')
    else:
        print('Você foi reprovado!')
