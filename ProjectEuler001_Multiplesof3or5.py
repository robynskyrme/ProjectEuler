# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def MultofM(n,m):
    mult = True
    if n % m > 0:
        mult = False
    return mult

def CheckNumbersUpTo(r):
    total = 0
    for c in range (r):
        current = False
        if MultofM(c,3):
            current = True
        if MultofM(c,5):
            current = True
        if current:
            total = total + c

    return total

if __name__ == '__main__':
    n = 1000
    print ("Sum of multiples up to", n, ":", (CheckNumbersUpTo(n)))


# Press the green button in the gutter to run the script.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
