# Problem 14 - Longest Collatz sequence
# My own solution was to use recursion (which didn't work)

def collatz(n:int):
    """
    Computes and returns the collatz sequence for an integer n
    """
    sequence = []

    while True:
        sequence.append(n)
        if n == 1:
            return sequence

        elif n % 2 == 0:
            n = n // 2

        else:
            n = n*3 + 1

curr_best = 0

for i in range(1, 1000000):
    sequence = collatz(i)

    if len(sequence) > curr_best:
        curr_best = len(sequence)
        winner = i

print(f"The number {winner} produces the longest Collatz sequence! ({curr_best})")