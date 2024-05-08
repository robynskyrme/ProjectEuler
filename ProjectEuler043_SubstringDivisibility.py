# 19.1.2024
# Project Euler 43 : Substring Divisibility

import math

def substring(n,start,length):
    if length < 1:
        return None

    new_string = n % 10 ** (start+1)

    digits = math.floor(math.log(new_string,10))+1

    new_string = new_string // 10 ** (digits-length)

    return new_string


def pandigital_zero_nine(n):
    digits = math.floor(math.log(n,10))+1
    if digits != 10:
        return False
    for d in range(digits):
        d += 1
        digit = substring(n,digits-d,1)
        print (digit)
    return True






if __name__ == "__main__":

    big_number = 1406357284

    # for d in range (8,1,-1):
    #     print(substring(big_number,d,3))

    print(pandigital_zero_nine(big_number))