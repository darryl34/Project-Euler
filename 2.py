# Problem 2 - Even Fibonacci numbers

def fibonacci(limit):
    a, b = 0, 1
    fib_sequence = []
    while b < limit:
        a, b = b, a + b
        fib_sequence.append(a)
    return fib_sequence

def sum_even_num(sequence):
    return sum(i for i in sequence if i % 2 == 0)

print(sum_even_num(fibonacci(4000000)))