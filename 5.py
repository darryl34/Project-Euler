# Problem 5 - Smallest Multiple
# Solution

import functools

# The formula given on Wikipedia for computing the LCM is:
# lcm(a, b) = |a*b| / gcd(a, b)
# Where gcd(a, b) denotes the greatest common divisor of a and b

# When computing the LCM of more than two numbers it can be computed by
# iteratively computing the lcm of the current value and the next element of the list
# Example: lcm(a, b, c, d) = lcm(a, lcm(b, lcm(c, d)))

def find_lcm(*args):
    # We want to repeatedly apply the lcm function 
    # This is exactly what the functools.reduce function is doing
    # Example: functools.reduce(lcm, (a, b, c, d)) = lcm(lcm(lcm(a, b), c), d)
    return functools.reduce(lcm, args)

def lcm(a, b):
    return a * b // gcd(a, b)

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

print(find_lcm(*range(1, 20)))