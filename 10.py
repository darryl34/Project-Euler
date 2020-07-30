# Problem 10 - Summation of primes

import numpy as np

n = 5000000
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
idx = np.where(primes < 2000000)[0]
subset = primes[idx]
print(sum(subset))