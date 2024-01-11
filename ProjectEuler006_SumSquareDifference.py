# 23.8.2023

# Project Euler 6
# The sum of the squares of the first ten natural numbers is 305.
# The square of the sum of the first ten natural numbers 3025.
# So the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

#######

# Call (a) the sum of the squares and (b) the square of the sum.

                            # (a) is the square pyramidal numbers (OEIS A000330)
                            # and the formula for the nth is n*(n+1)*(2*n+1)/6
def square_pyramidal_number(n):
    spn = n*(n+1)*(2*n+1)/6
    return int(spn)

                            # (b) the sum of any consecutive integers beginning 1 is a triangular number
                            # formula for nth triangular number is n*(n+1)/2

def triangle(n):
    t = n*(n+1)/2
    return int(t)


def difference(n):
    spn = square_pyramidal_number(n)
                            # square this result
    t = triangle(n) ** 2

    return t-spn


if __name__ == "__main__":
    print("Difference between the sum of the squares of the first one hundred natural numbers and the square of the sum is " + str(difference(100)))