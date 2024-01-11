# 15.3.2023
# Project Euler 12: Highly divisible triangular number
#
# What is the value of the first triangle number to have over five hundred divisors?

import math

def triangular_number(n):

    triangle = ((n+1)*n)/2

    return int(triangle)

def list_divisors(n):
    divisors = []
    for j in range(math.ceil(n/2)):
        j += 1
        if does_it_divide(j,n):
            divisors.append(j)

    divisors.append(n)
    return divisors

def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor


if __name__ == "__main__":
    cap = 500
    n = 1
    divisors = 0


    while divisors < cap:
        #print (str(triangular_number(n)) + " has " + str(len(list_divisors((triangular_number(n))))))
        #print(list_divisors(triangular_number(n)))

        n += 1
        divisors = len(list_divisors(triangular_number(n)))

    print(triangular_number(n))