# Problem 9 - Pythagorean triplet

import numpy as np

def find_triplet():
    for a in range(1, 500):
        for b in range(1, 500):
            c = np.sqrt(a**2 + b**2)

            if a + b + c == 1000:
                print(f"{a}, {b}, {c} = 1000")
                print(f"Product: {a*b*c}")
                return

find_triplet()