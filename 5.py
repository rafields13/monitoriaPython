# Receba o valor de um sálario e mostre quanto deve ser depositado de FGTS (8% do valor do salário) para este salário
# informado. Faça a conversão em duas casas decimais após a vírgula.

x = float(input('Digite o valor do salário aqui, por favor: '))
fgts = 0.08 * x
print(f'O valor FGTS que deve ser depositado de acordo com esse salário é {fgts:.2f} reais.')
