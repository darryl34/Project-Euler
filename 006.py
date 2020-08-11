# Problem 6 - Sum square difference

def sum_of_squares(n):
    s = 0
    for i in range(1, n+1):
        s += i*i
    return s

def square_of_sum(n):
    s = 0
    for i in range(1, n+1):
        s += i 
    return s*s

def diff(n):
    return square_of_sum(n)-sum_of_squares(n)

print(diff(100))
