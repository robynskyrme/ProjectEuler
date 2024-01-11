# 8.9.2023
# Project Euler 28 : Number Spiral Diagonals

# Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed.
# It can be verified that the sum of the numbers on the diagonals is 101.

# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

                            # Ok instinctively I want to just play around and come up with a formula for this
                            # but
                            # I'm not very good at recursion, and this seems like an excuse to try to use it

                            # function to calculate the corners of a square: it will need to calculate
                            # those of the square inside that, by calculating those of the square inside that...
def corners_total(edge):
    total = 0
    count = 0
    skip = edge - 1
                            # all the way down to the 'final case' (when the edge length is 1):
    if edge == 1:
                            # values returned are: total, and last corner counted (i.e. number to keep counting from)
        return 1,1

                            # In all other cases, this is the recursive call:
    else:
        total,count = corners_total(edge-2)

                            # Counts the values, pretty much manually
        for j in range (4):
            count = count + skip
            total = total + count

    return total,count


if __name__ == "__main__":
    total,count = (corners_total(1001))

    print("Total of the diagonals: " + str(total))