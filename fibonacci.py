def fibonacci(number):
    if number <= 0:
        return 'The number must be greater than 0.'
    elif number == 1:
        return [0]
    elif number == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, number):
            next_number = fibonacci_sequence[i - 1] + fibonacci_sequence[i - 2]
            fibonacci_sequence.append(next_number)
        return fibonacci_sequence


n = int(input("Type a number greater than 0, please: "))
sequence = fibonacci(n)
print("The Fibonacci Sequence for number", n, "is:", sequence)
