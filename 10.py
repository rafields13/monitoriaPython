# Crie um programa que receba duas notas e informe se a pessoa passou ou não. Considere que o usuário irá informar
# uma nota entre 0 e 10 e que média a partir de 5 leva o aluno a aprovação.

x = float(input('Digite a primeira nota aqui, por favor: '))
y = float(input('Digite a segunda nota aqui, por favor: '))

if x > 10 or x < 0 or y > 10 or y < 0:
    print('Pelo menos uma das notas digitadas é inválida!')
else:
    average = (x + y) / 2
    if average >= 5:
        print('Você foi aprovado!')
    else:
        print('Você foi reprovado!')
