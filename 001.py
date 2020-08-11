# Problem 1 - Multiples of 3 and 5

def findSumOfMultiples(n):
    multiples = [i for i in range(n) if i%3==0 or i%5==0]
    return sum(multiples)

print(findSumOfMultiples(1000))