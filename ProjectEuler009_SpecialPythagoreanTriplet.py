# 23.8.2023

# Project Euler 9
# Special Pythagorean Triplet

#  Find the proudct abc of a < b < c such that a^2 + b^2 = c^2 and a + b + c = 1000

                            # Method to check whether 3 numbers are a pythagorean triple
def pyth_triple(a,b,c):
    triple = False
    if a*a + b*b == c*c:
        triple = True

    return triple

                            # Iterate a and b, calculating c from that
def searchfortriples(n):
    for a in range(n):
        for b in range (n):
            c = n - (a+b)
                            # Check that the relation holds
            if a < b < c:
                            # If the criterion is met, break out of the loops by returning a value and quitting function
                            # (This does mean that if n is made larger, this method will only find the first such triple)
                if pyth_triple(a,b,c):
                    return a,b,c


if __name__ == "__main__":
    n = 1000
    a,b,c = searchfortriples(n)

    print ("Product is " + str(a*b*c))