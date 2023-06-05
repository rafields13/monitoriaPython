# Desenvolva um programa que leia n números e mostre estas informações:

# a) A quantidade de elementos dados;

# b) A soma dos valores;

# c) A média dos valores; e

# d) A porcentagem de números pares.

def calculate_number_information():
    numbers = []
    total_number_elements = 0
    sum = 0
    pair_numbers = 0

    quantity = int(input("Type the quantity of numbers to read: "))

    for _ in range(quantity):
        number = int(input("Please, type a number: "))
        numbers.append(number)
        sum += number
        total_number_elements += 1

        if number % 2 == 0:
            pair_numbers += 1

    average = sum / total_number_elements
    percentage_pair_numbers = (pair_numbers / total_number_elements) * 100

    print(total_number_elements, sum, average, percentage_pair_numbers)


calculate_number_information()
