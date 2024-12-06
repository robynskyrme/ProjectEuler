# 6.12.2024

# Project Euler #63

# How many n-digit positive integers exist which are also an nth power?

# assumption: we are looking at numbers m raised to a power n where m < 10, because
# 10 to any power n is always of length n+1

# the last n where 9^n has n digits is 9^21, so let's start there and search downwards?
# (found by trial and error in WolframAlpha)

# Yep, solved: 49



import math
def digits(n):
    return int(math.log(n,10))+1

def countdown(m,n):
    tally = 0
    for i in range (m,0,-1):
        for j in range (n,0,-1):
            #print(str(i) + " ^ " + str(j))
            p = i ** j
            if digits(p) == j:
                tally += 1
                print((str(i)) + " to the power of " + str(j) + " has " + str(j) + " digits: " + str(p))
    return tally

if __name__ == "__main__":
    answer = countdown(9,21)
    print(answer)

