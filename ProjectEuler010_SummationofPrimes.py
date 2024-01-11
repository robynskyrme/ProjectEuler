# 23.8.2023

# Project Euler 10
# Summation of primes

# Find the sum of the primes below two million.

# 24.8.2023 -- this is more than ten times faster now that I've introduced a sieve into the prime check

import time
from hinimath import prime
# ed. on 30.8: it works! haha (but, only if hinimath.py is in the exact same directory. that's fine, for now)
# and you can't import the whole module at once, only individual ones from within it -- why?

def sum_primes_below(max):
    n = 2
    primesum = 0
    count = 1
    while n < max:
        if prime(n):
                            # Output every 1000th prime, just to keep me happy it's still alive :)
            if count == 1000:
                print(n)
                count = 1

            count += 1
            primesum += n
        n += 1

    return primesum

if __name__ == "__main__":
    below = 200000
    begin_clock = time.time()
    print ("The sum of primes below " + str(below) + " is " + str(sum_primes_below(below)))
    end_clock = time.time()-begin_clock

    print (end_clock, "seconds")