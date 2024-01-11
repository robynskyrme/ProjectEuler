# Project Euler 29 : Distinct Powers

# Consider all integer combinations of a^b for 2 <= a <= 5 and 2 <= b <= 5.
# If they are then placed in numerical order, with any repeats removed, we get [sequence] of 16 distinct terms.
# How many distinct terms are in the sequence generated by a^b for 2 <= a <= 1000 and 2 <= b <= 1000?


# naive approach works for small numbers, but needs optimizing as gets very slow as it approaches 4 digits




if __name__ == "__main__":
                            # Set the number given in the question here
                            # (it will be altered later, but, for readability)
    # e.g. example given is:
    # max = 5
    # [test works]

    # question as set:
    max = 1000


    list = []

    max += 1

    for b in range (2,max):
        for a in range (2,max):
            result = a**b
            if list.count(result) == 0:
                list.append(result)
                print(result)

    #print(list)
    print(len(list))