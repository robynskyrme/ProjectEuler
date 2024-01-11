# 10.3.2023
# Project Euler 7: What is the 10001st prime?


def does_it_divide(m,n):
    factor = True
    if n%m != 0:
        factor = False
    return factor

                            # Primality test
def is_it_prime(n):
    prime = True
    half = int(n/2)
                            # (test counts down from half of n, one integer at a time, asks if it divides:
    for c in range(half,1,-1):
                            # (if it ever does, n is not prime)
        if does_it_divide(c,n) == True:
            prime = False
                            # There is a special case for excluding 1, which would otherwise return as prime
    if n == 1:
        prime = False
    return prime

def nth_prime(n):
    prime_count = 0
    count = 1

    while prime_count < n:
        if is_it_prime(count):
            prime_count += 1
            # print(str(prime_count) + ": " + str(count))
            nth_prime = count

        count += 1

    return nth_prime

if __name__ == "__main__":
    nth_prime = nth_prime(10001)
    print(nth_prime)