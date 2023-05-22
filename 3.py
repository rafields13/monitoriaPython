# Receba um valor em Real e mostre a sua conversão em Dólar e em Euro. Faça a conversão em duas casas decimais após a
# vírgula.

x = float(input('Digite o valor desejado em Reais, por favor: '))
d = x / 4.97
e = x / 5.37
print(f'O valor digitado convertido em Dóllar é {d:.2f}.\nO valor convertido em Euro é {e:.2f}.')
