# 8.5.2023
# Project euler #52: Permuted Multiples
#
# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
#
# Find the smallest positive integer, x, such that 2x, 3, 4x, 5x, and 6x contain the same digits.


# BRUTE FORCE! (to begin with, at least, to check that my test works)
# for x, 2x it finds the answer given -- for x, 2x. 3x. it finds 142857 -- to it seems to work
# ---- but it's taking a lot longer to find x, 2x, 3x, 4x --- so, going up to 6 may well need a more clever method

# To test it out,


                            # takes an integer n and m for how many multiples to check up to (i.e. 3 = x, 2x, 3x)
def find_multiples(n,m):
    multiples = []
    mults = n
    for i in range(m):
        multiples.append(mults)
        mults += mults

    answer = permute_check(n,multiples)
    if answer:
        return(answer)
    else:
        return None


def permute_check(n,list):
    hash = hash_ints(n)

    for i in range(len(list)):
        mult_hash = hash_ints(list[i])
        # print("\n")
        # print(n)
        # print(mult_hash)
        # print(hash)
        if mult_hash != hash:
            return False

    return n


def hash_ints(n):

    hash = []

    for i in range(10):
        hash.append(0)

    while n:
        digit = n %10
        hash[digit] += 1
        n = n//10

    return hash




if __name__ == "__main__":
    i = 10000000

    ans = None

    increment = 100000
    check = increment + i

    while ans == None:
        ans = find_multiples(i,4)
        i += 1
        if i == check:
            print(" ... " + str(check))
            check += increment

    print(ans)