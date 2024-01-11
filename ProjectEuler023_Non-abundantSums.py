# 15.3.2023
# Project Euler 23: Non-abundant sums
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
#
# UNFINISHED
# think it might work but it's phenomenally slow


import math

abundant_numbers = []

sums_of_two_abundants = []

abundant_numbers.append(12)
sums_of_two_abundants.append(24)

not_sum_of_abundants = []

def list_divisors(n):
    divisors = []
    for j in range(math.ceil(n/2)):
        j += 1
        if does_it_divide(j,n):
            divisors.append(j)

    return divisors


def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

def abundant(n):
    if sum(list_divisors(n)) > n:
        abundant = True
    else:
        abundant = False

    return abundant


def add_next_abundant_number():
    #print("function called")
    largest_abundant = abundant_numbers[len(abundant_numbers)-1]

    check = largest_abundant + 1

    while not abundant(check):
        check += 1

    abundant_numbers.append(check)
    #print(abundant_numbers)


def update_sums():
    #print(abundant_numbers)
    for a in abundant_numbers:
        for b in abundant_numbers:
            #print(a+b)
            if sums_of_two_abundants.count(a+b) == 0:
                sums_of_two_abundants.append(a+b)

def sum_of_abundants(n):
    #print(n)
    #print("sum of abundantrs called")
    if sums_of_two_abundants.count(n) == 0:
        return False
    else:
        return True


if __name__ == "__main__":

    k = 1

    while max(sums_of_two_abundants) < 10000:


        #print(k)
        #print(sums_of_two_abundants)


        if not sum_of_abundants(k):
            not_sum_of_abundants.append(k)

        else:
            #print(k)
            add_next_abundant_number()
            update_sums()

        k = k + 1

    print(sum(not_sum_of_abundants))

