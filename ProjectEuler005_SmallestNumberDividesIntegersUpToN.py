
def Divisor(n,x):
    Div = False
    if int(n/x) == n/x:
        Div = True

    return Div

def SmallestDivisorUpTo(n):

    sd = n


    DoesItDivideAll = False

    while DoesItDivideAll == False:

        TripWire = False

        for d in range(1,n+1):
         #   print (d, sd)
            if Divisor(sd,d) == False:
                TripWire = True

        if TripWire == True:
            DoesItDivideAll = False
        else:
            DoesItDivideAll = True

        sd = sd + 1

    return sd-1




    return sd


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    n = input("Number to check: ")

    n = int(n)

    print (SmallestDivisorUpTo(n), "is the smallest number which divides all integers up to and including", n)
