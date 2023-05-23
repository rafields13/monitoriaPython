# Faça um algoritmo que retorne a hora que for digitada de acordo com a hora que o usuário digita.

x = int(input('Digite a hora aqui, por favor: '))
if 0 <= x < 6:
    print(f'São {x} horas. Boa madrugada!')
elif 6 <= x < 12:
    print(f'São {x} horas. Bom dia!')
elif 12 < x <= 18:
    print(f'São {x} horas. Boa tarde!')
else:
    print(f'São {x} horas. Boa noite!')
