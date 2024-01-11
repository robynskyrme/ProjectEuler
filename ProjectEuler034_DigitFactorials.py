# 9.12.2023
# Project euler #34: Digit Factorials
#
# A bit brute forcey but it works

import math

def list_digits(n):
    digits = []
    while n:
        digit = n % 10
        n = n // 10
        digits.append(digit)

    digits.reverse()
    return digits

def equals_sum_of_factorials(n):
    digits = list_digits(n)
    total = 0
    exact_match = False
    for d in digits:
        total = total + math.factorial(d)
        if total > n:
            return

    #print(total)
    if total == n:
        exact_match = True
        #print(total)

    return exact_match

if __name__ == "__main__":
    total = 0
    for i in range(3,50000):
        #print(str(i) + "   " + str (list_digits(i)))
        if equals_sum_of_factorials(i):
            total += i
            #print("BANGARANG")
    print(total)
