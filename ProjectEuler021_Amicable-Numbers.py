# Project Euler 21: Amicable numbers

# Evaluate the sum of all amicable numbers below 10000

# unfinished

import math



def sumproperfactors(n):
    if n == 1:
        return 1
    factors = []
    s = math.sqrt(n)
    max = int(s)

    for div in range (2,max):
        if n % div == 0:
            factors.append(div)
            factors.append(n//div)
    if s == max:
        factors.append(max)
    factors.append(1)


    print(factors)
    return(sum(factors))

def amicable_numbers_below(n):

    print(sumproperfactors(n))



    return [1,2,3]

if __name__ == "__main__":
    list = amicable_numbers_below(100)
    #print(sum(list))