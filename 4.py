# Crie um programa que calcule o IMC, recebendo pelo teclado o peso e a altura. Faça a conversão em duas casas
# decimais após a vírgula.

h = float(input('Digite a altura em metros aqui, por favor: '))
w = float(input('Digite o peso em kilogramas aqui, por favor: '))
imc = w / h**2
print(f'O IMC é {imc:.2f}.')
