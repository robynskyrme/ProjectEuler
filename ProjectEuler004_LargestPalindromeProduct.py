import time

def is_it_palind(word):
# Assume it's a palindrome: switch this to false as soon as a pair doesn't match
    palind = True
# Variable for length of string
    c = len(word)
# Variable for the character toward the end of the string
    e = c
# Loop using variable for character toward the start of the string
    for s in range (c):
# Subtract the count from the length; deal with the zero indexing with a -1
        e = c-s-1
#        print (word[s],word[e])
# Do the check!
        if word[s] != word[e]:
            palind = False

    return palind

def palinprodcheck(d):

    # Set two variables each to the largest 3 digit number and loop downwards, crossmultiplying

    # Set upper and lower limits for loops based on the largest and smallest numbers of n-digits
    ul = pow(10,d)-1
    ll = pow(10,d-1)

    x = ul
    y = ll

    largestp = 0
    largestpx = 0
    largestpy = 0

    print ()

    while x > ll:
        y = ul
        while y > ll:
            # Do the math[s]
            n = x * y
            sn = str(n)
            # print (x, " times ", y, " = ", sn)
            if is_it_palind(sn) == True:
                # print ("Found: ", x, ".", y, " = ", sn)
                # Hold the largest palindrome in memory, along with the 2 relevant factors, and update it if a larger one is found
                if n > largestp:
                    largestp = n
                    largestpx = x
                    largestpy = y
            y = y - 1
        x = x - 1

    print ("The largest palindromic product of two", d, "-digit numbers is", largestp, "(", largestpx, "x", largestpy, ")")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    # (I've decided to start timing them as a habit now)

    d = input("How many digits? ")

    # Make the input string into a number
    d = int(d)

    timestart = time.time()

    palinprodcheck(d)

    timer = time.time()-timestart

    print (timer, "seconds")
