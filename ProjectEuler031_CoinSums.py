# 17.9.2023
# Project Euler 31: Coin Sums

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?


coin_combinations = []

def all_possible_choices_from_list_using_binary_counting(list):
    bits = len(list)
    max = 2 ** bits
    format_string = "0" + str(bits) + "b"

    for count in range(1,max):
        count_as_binary = format(count,format_string)
        make_list_of_specified_coins(count_as_binary)

def make_list_of_specified_coins(coins_used_code):
    coins_used = []
    for bit in range(len(coins_used_code)):
        if coins_used_code[bit] != "0":
            coins_used.append(coins[bit])
#    print(coins_used)

    recurse_fill_using_specified_coins(goal,coins,[],0)

def recurse_fill_using_specified_coins(gap,coins,coin_multiples,current_denomination):

    fill = gap-gap

    if coin_multiples == []:
        for mults in range(len(coins)):
            coin_multiples.append(0)

    coin_multiples[current_denomination] += 1


    for coin in range(len(coins)):
        fill = fill + coins[coin] * coin_multiples[coin]

        if fill == gap:
            print(fill)
            current_denomination += 1
            return fill, current_denomination

        if fill > gap:
            coin_multiples *= 0
            return fill, current_denomination

    print(fill)
    print(current_denomination)

    fill, current_denomination = recurse_fill_using_specified_coins(gap,coins,coin_multiples,current_denomination)




    return fill, current_denomination




if __name__ == "__main__":
    coins = [5,2,1]
    goal = 100
    all_possible_choices_from_list_using_binary_counting(coins)