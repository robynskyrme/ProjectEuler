# 8.5.2023
# Project Euler #15: Lattice Paths
#
# "Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner."
# "How many such routes are there through a 20×20 grid?"
#
# started this on pencil and paper: I think the answer for an n by n grid will just be the central value of the (2n+1)th row in Pascal's Triangle
# .. for which I am sure there is a formula
# but, I've never coded Pascal's triangle, so I thought, why not
#
# 2n+1 = 41
# The middle number of the given row is 137846528820 (found by... looking at it  --  they're huge, but it's the only number surrounded by two identical numbers)
#
# Which is, says the internet, the correct answer



def next_row(aboverow):

    aboverow.insert(0,0)
    aboverow.append(0)

    newrow = []

    for j in range(len(aboverow)-1):
        sum = aboverow[j] + aboverow[j+1]
        newrow.append(sum)

    del aboverow[0]
    del aboverow[-1]

    return newrow



def pascals_triangle(height):
    pt = []
    pt.append([1])

    for j in range(height-1):
        pt.append(next_row(pt[j]))

    return pt



if __name__ == "__main__":
    print(pascals_triangle(41))