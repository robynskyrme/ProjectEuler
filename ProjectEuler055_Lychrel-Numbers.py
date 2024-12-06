
# Project Euler #55

# How many Lychrel numbers are there below ten-thousand?
# (Lychrel numbers do NOT become palindromes after repeatedly being added to their reverse)

# Gives the answer 250, when correct is apparently 249 (!) --- will look again


import math

def rev(n):
    if n < 10:
        return n

    ans = 0
    place = int(math.log(n,10))

    while n != 0:
        ans += (n % 10) * 10**place
        n = n//10
        place -= 1

    return ans


def palin(n):
    if n == rev(n):
        return True
    return False


def lychrel(n):            # tests whether a number is Lychrel; returns true if no palindrome after 50 iterations
    iter = 50

    j = 0

    while j <= iter:
        n += rev(n)
        #print(n)
        if palin(n):
            return False
        j += 1

    return True




if __name__ == "__main__":              # Count them
    tally = 0
    for a in range(1,10000):
        if lychrel(a):
            print(a)
            tally += 1
    print(tally)

    print(lychrel(9999))