# 8.12.2024

# Project Euler #37
# Truncatable Primes

# Sum the only 11 primes which are truncatable in both directions

import time
import math
from rsmath import prime

def bookends23or7(n):

    right = n % 10

    if right != 3 and right != 7:
        return False

    left = n//10**int((math.log(n,10)))

    if left != 3 and left != 7 and left != 2:
        return False

    return True

def alldigitsvalid(n):
    digits = [0,0,0,0,0,0,0,0,0,0]
    while n:
        right = n % 10
        digits[right] += 1

        n = n//10

    digits[1] = 0
    digits[3] = 0
    digits[7] = 0
    digits[9] = 0

    if sum(digits) > 0:
        return False

    return True

def trunc_simul(n):
    if not prime(n):
        return False
    #print(n)
    right = n
    left = n

    tenthpower = int(math.log(n,10))

    length = tenthpower + 1

    while length > 1:
        #print(right)
        right = right//10
        left = left % 10**tenthpower
        if not prime(left) or not prime(right):
            #print("bang! " + str(left) + " or " + str(right) + " is not prime")
            return False
        length -= 1
        tenthpower -= 1

    print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA " + str(n) + " is truncatable in both directions")
    return True


if __name__ == "__main__":
    print("")
    stopwatch = time.time()

    list = []

    n = 10

    while len(list) < 11 and n < 1000000:
        if bookends23or7(n):
            if trunc_simul(n):
                list.append(n)
                print(list)
        print(n)
        n += 1


    # while len(list) < 2:
    #     if bookends3or7(n):
    #         if alldigitsvalid(n):
    #             if trunc_simul(n):
    #                 print(n)
    #                 list.append(n)
    #     n += 1

    print(list)

    print("\n/// done in " + str(time.time()-stopwatch) +" seconds ///")




