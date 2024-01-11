# 1.9.2023
# Project Euler 27 : Quadratic Primes

# Considering quadratics of the form:
#
# n^2 + an + b , where |a| < 1000 and |b| <= 1000
#
# Find the product of the coefficients, a and b, for the quadratic expression
# that produces the maximum number of primes for consecutive values of n, starting with 0.

import math
from hinimath import prime

integer_list = []

def make_list(u):
                            # Create a list of all primes between -1000 and 1000 (excluding primes between -41 and 41)
    for j in range(41,u):
        if prime(j):
            integer_list.append(j)

    half = len(integer_list)
    for j in range(half):
        integer_list.append(integer_list[j])


    for j in range(half):
        integer_list[j] = 0-integer_list[len(integer_list)-(j+1)]


def primes_from_quadratic(a,b):
    prime_chain = False
    chain_length = 0
                            # First test:
    n = 0
    if not prime(n**2+(a*n)+b):
        return
    else:
        prime_chain = True

                            # If n = 0 gave a prime, keep looking....
    while prime_chain:
        n += 1
        next = n**2+(a*n)+b
                            # Soon as there's a composite, stop looking
        if not prime(next):
            prime_chain = False
        # else:
        #    print(next)

                            # This didn't really need to be a separate variable but it's easier to read like this
    chain_length = n

    return chain_length


if __name__ == "__main__":
                            # Create the array of numbers to check (set the question's limit of 1000 here)
    make_list(1000)

    record = 0

    a_ans = 0
    b_ans = 0

                            # Literally just check the list against itself. Big O of (n^2), I guess?
    for j in integer_list:
        for k in integer_list:
            new = primes_from_quadratic(j,k)
            if new > record:
                record = new
                a_ans = j
                b_ans = k
                            # Uncomment this to see every single one checked
        #    print("For a = " + str(j) + " and b = " + str(k) + " the chain is length: " + str(new))

    print("Longest chain of primes generated was " + str(record) + ", from a = " + str(a_ans) + " and b = " + str(b_ans))
    print("Their product is " + str(a_ans * b_ans))