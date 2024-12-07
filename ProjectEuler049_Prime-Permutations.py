# 7.12.2024

# Project Euler #49

# The arithmetic sequence, 1487, 4871, 8714, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and,
# (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three
# 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

# Solved! runs in about 5 seconds

from rsmath import prime
import time


def is_permutation(m,n):
    if len(str(n)) != len (str(m)):
        return False

    m_histo = [0,0,0,0,0,0,0,0,0,0]
    n_histo = [0,0,0,0,0,0,0,0,0,0]

    while m:
        digit = m % 10
        m_histo[digit] += 1
        m = m//10

    while n:
        digit = n % 10
        n_histo[digit] += 1
        n = n//10

    if m_histo == n_histo:
        return True

    return False


def n_plus_j_plus_j(n):

    if not prime(n):
        return

    for j in range(1000,3333):
        x = n + j
        if is_permutation(n,x) and prime(x):
            y = n + 2*j
            if is_permutation(n,y) and prime(y):
                print((str(n),str(x),str(y)))
                print("-- difference of " + str(j))



if __name__ == "__main__":
    stopwatch = time.time()

    for i in range(1001,4000):
        n_plus_j_plus_j(i)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")
