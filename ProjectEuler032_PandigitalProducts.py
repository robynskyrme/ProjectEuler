# 18.9.2023
# Project Euler 32: Pandigital Products

# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

import math

def number_as_list_of_digits(n):
    n_as_list = []
    magnitude = int(math.log(n,10))+1
    for place in range(magnitude):
        place += 1
        digit = n // 10**(magnitude-place) % 10
        n_as_list.append(digit)
    return n_as_list

def is_number_pandigital(n):
    digits_in_n = int(math.log(n,10))+1

    if digits_in_n > 9:
        return

    all_digits_to_n = []
    for digits in range(digits_in_n):
        digits += 1
        all_digits_to_n.append(digits)

    n_as_list = number_as_list_of_digits(n)

    for d in n_as_list:
        if all_digits_to_n.count(d) > 0:
            all_digits_to_n.remove(d)

    if all_digits_to_n == []:
        return True
    else:
        return False


#def search_for_pandigital_identities()



if __name__ == "__main__":
    print(is_number_pandigital(123456789))