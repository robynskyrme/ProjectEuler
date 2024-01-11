# 23.8.2023

# Project Euler 20
# Factorial Digit Sum

# Find the sum of the digits of 100!

def factorial(n):
    f = 1
    while n > 1:
        f = f*n
        n -= 1

    return f


if __name__ == "__main__":
    n = (factorial(100))
    s = 0

    for a in str(n):
        s += int(a)

    print(s)