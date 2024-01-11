
# 8.3.2023 Revisiting some Project Eulers I lost in December

# 1.9.2023
# just updated to use new prime check
# (so it presumably DID work before, it was just so incredibly slow that i never let it finish
# -- it now completes in c. 16 seconds)

import time
from hinimath import prime

                            # Method returns True if m divides n with modulo zero
def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

                            # Primality test
def find_largest_prime_factor(n):
    ans = 1
    found = False
    div = 2
    while found == False:
        if does_it_divide(div,n):
            if prime(n/div):
                ans = n/div
                found = True
        div = div + 1
    return int(ans)


if __name__ == '__main__':
    inputn = input("Test number: ")
    inputn = int(inputn)

    timestart = time.time()
    f = find_largest_prime_factor(inputn)
    print(f)
    timer = time.time()-timestart

    print (timer, "seconds")