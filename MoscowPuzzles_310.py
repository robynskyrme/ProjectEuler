# 21.4.2023
# Moscow Puzzles: 307
#
# ...distributing oranges between parcels. "We calculated that if we put
# 10 oranges to a package, one package wou ldonly get 9..."
# (ditto for packages of 9 = remainder 8, all the way down to parcels of 2 = remainder 1)
#
# "How many oranges did we have?"

()
def divides(m,n):
    ans = True
    if m%n != 0:
        ans = False

    return ans


def oranges(n):
    tickboxes = ""
    for k in range (10,1,-1):
        if divides(n+1,k):
            tickboxes = tickboxes + "#"
        else:
            tickboxes = tickboxes + " "
    if tickboxes == "#########":
        tickboxes = tickboxes + "   <<<<<<<<<<<<< " + str(n)
    print(tickboxes)



if __name__ == "__main__":
    for j in range(2525):
        oranges(j)