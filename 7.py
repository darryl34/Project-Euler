# Problem 7 - 10001st prime

import numpy as np

n = 200000
sieve = np.array([True for _ in range(n)])
sieve[0:2] = False
upper_bound = int(np.sqrt(n))

for i in range(2, upper_bound+1):
    if sieve[i]:
        j = i * i
        counter = 0
        while j < n:
            sieve[j] = False
            j = i*i + counter*i
            counter += 1

primes = np.where(sieve == True)[0]

print(primes[10000])