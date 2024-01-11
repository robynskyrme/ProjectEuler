# 8.12.2023
# Project euler #40: Champernowne's Constant

# Weird bug in this -- it works fine for the first six numbers, but somewhere before the seventh it goes wrong......


import math

def how_many_digits(n):
    d = math.log(n,10)
    d = math.floor(d) + 1
    return d

def champernowne_counter(limit):

    fullchampernowne = ""

    concat_int = 1
    length = 0
    cursor = 1
    digits_collected = []

    while length < limit:
        fullchampernowne = fullchampernowne + str(concat_int)
        length = length + how_many_digits(concat_int)
        # print(str(concat_int) + " = " + str(length))

        if length == cursor:
            print("EXACTLY HERE")
            digits_collected.append(concat_int % 10)
            cursor *= 10

        if length > cursor:
            shortfall = abs(cursor-length)
            print("JUST MISSED ONE, by " + str(shortfall))
            int_nugget = concat_int
            int_nugget = (int(int_nugget) // (10 ** shortfall)) % 10
            digits_collected.append(int_nugget)
            cursor *= 10

        concat_int += 1

    mark = 10000000
    print(fullchampernowne[mark-1])
    return digits_collected

def multiplyList(myList):
    # Multiply elements one by one
    result = 1
    for x in myList:
        result = result * x
    return result

if __name__ == "__main__":
    digits = champernowne_counter(10000000)
    print(digits)

    p = multiplyList(digits)
    print (p)