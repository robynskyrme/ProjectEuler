# 15.9.2023
# Project Euler 30: Digit Fifth Powers

# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

def digits_as_list(n):
    digits = []
    n = str(n)
    for d in n:
        digits.append(int(d))

    return digits

def raise_list_to_power(list,p):
    for i in range(len(list)):
        list[i] = list[i] ** p

    return list


if __name__ == "__main__":
    sum_of_answers = 0
    for count in range(2,1000000):
        powersum = sum(raise_list_to_power(digits_as_list(count),5))
        if powersum == count:
            print(str(count))
            sum_of_answers += count

    print("Sum, not including 1: " + str(sum_of_answers))