# 8.3.2023
# Revisitng some missing Project Euler

# Project Euler 4
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.

def is_it_even(n):
    even = True
    if n%2 == 0:
        even = True
    else:
        even = False
    return even



                            # Generate the Fibonacci sequence for n < k
                            # up to k
def fibonacci(k):
    x = 1
    y = 1
    m = 1
    n = 1

    even_sum = 0

    while n < k:
        print(n)
        if is_it_even(n):
            print("Even")
            even_sum = even_sum + n
        m = n
        x = y
        y = m

        n = x + y

    print("Sum of even values up to " + str(k) + ": " + str(even_sum))


if __name__ == "__main__":
    fibonacci(4000000)