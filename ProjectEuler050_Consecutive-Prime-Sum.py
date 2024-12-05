
## Project Euler #50

# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21
# terms, and is equal to 953

# Which prime, below one-million, can be written as the sum of the most consecutive primes?

## NOTES
# --- any sum of primes which is prime will contain an odd number of terms, unless it contains 2,
#       in which case it will contain an even number of terms


## DONE
# The longest sum of consecutive primes below 1000000 which adds to a prime is 997651, a sum of 543 consecutive primes
# 25.730888605117798 seconds


import time
from rsmath import prime

primes = []
def longestprimesum(ceil):
    seqmax = getlongestseqbelow(ceil)       # function to find length of the LONGEST prime sequence below the ceiling


    answerlength = 0
    startprime = 0

    primes.append(0)

    #print(primes)
    copy = primes[:]

    iter = 1
    while copy:      # 2 nested loops (n^2) to search substrings by removing from each end
        for j in range(len(copy)-1):
            copy.pop(len(copy)-1)
            #print(copy)
            if prime(sum(copy)):
                if len(copy) > answerlength:
                    answerlength = len(copy)
                    startprime = copy[0]
        copy = primes[:]

        for c in range(iter):
            copy.pop(0)

        iter += 1

    # print(answerlength)
    # print(startprime)

    primeindex = primes.index(startprime)
    # print(primeindex)

    total = 0
    for s in range(answerlength):
        total += primes[primeindex]
        primeindex += 1

    return total,answerlength


def getlongestseqbelow(ceil):
    total = 0
    number = 1

    while total < ceil:
        if prime(number):
            primes.append(number)
            total += number
        number += 1

    if total >= ceil:
        primes.pop(len(primes)-1)

    return len(primes)



if __name__ == "__main__":
    stopclock = time.time()
    input = 1000000
    answer,length = longestprimesum(input)
    print("The longest sum of consecutive primes below " + str(input) + " which adds to a prime is " + str(answer) + ", a sum of " + str(length) + " consecutive primes")
    print(str(time.time()-stopclock) + " seconds")