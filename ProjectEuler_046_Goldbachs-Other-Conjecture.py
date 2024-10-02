# 2.10.2024
# PE 46 Goldbach's Other Conjecture

# "What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?"

# I am sure this could be done better / faster, but:
# Smallest counterexample is 5777
# 1.638641595840454

import time
import math

doubled_squares = []
primes = [2,3,5]


def prime(n):

                            # Special cases:
    if n == 1 or n == 0:
        return False
    if n == 2:
        return True

    max = (int(math.ceil(math.sqrt(n))))

    sieve = [0]

    for s in range(max):
        sieve.append(1)

    d = 2
                            # Count up to sqrt(n)
    while d <= max:
                            # Only check a new divisor if it has not already been eliminated
        if sieve[d] == 1:
            if n % d == 0:
                return False
                            # If a number d does not divide n, then eliminate all multiples of d from the search
        for j in range(d, len(sieve), d):
            sieve[j] = 0
        d += 1

    return True

def try_n(n):
                            # if it's a prime it can be ignored; but add the prime to the list of primes
    if prime(n):
        primes.append(n)
                            # and return false as no exception found
        return False

    #print(primes)
    #print(doubled_squares)
    for x in range(len(doubled_squares)):
        for y in range(len(primes)):
            if doubled_squares[x]+primes[y] == n:
                return False

    return True



if __name__ == "__main__":
    stopwatch = time.time()

    n = 3
    counter = 0

    exception = False

    while exception == False and n < 10000:
                            # populate the list of doubled squares as we go...
        doubled_squares.append((((n-1)//2)**2)*2)
        exception = try_n(n)
        n += 2

        counter += 1
        if counter == 25:
            counter = 0
            #print(n)

    n -= 2
    print("Smallest counterexample is " + str(n))

    print (str(time.time() - stopwatch))