# 16.7.2023
# Project Euler #26

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

import time


def reciprocals(d):
    place = 1
    digits = []
                            # method does not actually do any division; I tried by hand and noticde that if a decimal
                            # repeats then so do the 'carries' when it is calculated (and, with the same exact period)


                            # loop to 'divide' (calcluate carries) while there is still a remainder
    while place != 0:
        place = (place * 10) % d
                            # make a list of these values as we encounter them
        digits.append(place)
                            # values behave entirely predictably so if ever we encounter one again, a cycle is detected
        if digits.count(place) > 1:
                            # in which case, *pretend* there is no remainder just to quit the loop:
                            # we've already found what we wanted
            place = 0

                            # the length of the list of carries (minus the one which triggered the repeat) is the
                            # length of the reptend
    return (len(digits)-1)




if __name__ == "__main__":
                            # set a value with the current 'record holder' for repdigits -- 1/7 (cycle of 6)
    peak = 7
                            # 11-999 because no point checking what the answer's already given us (1-10)
    for d in range(11,999):
        r = reciprocals(d)
                            # this is a lousy check as it calculates the values more than once
                            # 9probably slows it down a lot)
                            # will refine soon (!) -- they could just be stored or something
        if reciprocals(d) > reciprocals(peak):
            peak = d

                            # however, it does give the right answer, 983, which  I checked on Wolfram Alpha really does
                            # have 982 repeating digits (!)



    timestart = time.time()

    print("d with longest string of repeating digits in 1/d is " + str(peak) + " which has " + str(reciprocals(peak)) + " repeating digits")

    timer = time.time()-timestart
    print (timer, "seconds")