# Crie uma variação do programa anterior, porém com os seguintes requisitos: calcule uma média ponderada,onde o peso
# da Nota 1 é 1, peso da Nota 2 é 1.5 e peso da Nota 3 é 2. Ao invés de mostrar se o aluno foi aprovado ou não com
# base na média ponderada mostre uma menção de SR, II, MI, MM, MS ou SS, conforme a média ponderada e usando a
# escala: SR - 0 | II - < 2 | MI - < 5 | MM - < 7 | MS - < 9 | SS - >= 9

x = float(input('Digite a primeira nota aqui, por favor: '))
y = float(input('Digite a segunda nota aqui, por favor: '))
z = float(input('Digite a terceira nota aqui, por favor: '))

if x > 10 or x < 0 or y > 10 or y < 0 or z > 10 or z < 0:
    print('Pelo menos uma das notas digitadas é inválida!')
else:
    weightedAverage = (x + (y * 1.5) + (z * 2)) / 4.5
    if weightedAverage == 0:
        print('Você tirou SR!')
    elif 0 < weightedAverage < 2:
        print('Você tirou II!')
    elif 2 < weightedAverage < 5:
        print('Você tirou MI!')
    elif 5 < weightedAverage < 7:
        print('Você tirou MM!')
    elif 7 < weightedAverage < 9:
        print('Você tirou MS!')
    else:
        print('Você tirou SS!')
