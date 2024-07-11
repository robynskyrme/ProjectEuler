
# Project Euler 31: Coin Sums

# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

 # I really, really, really hate this one




combinations = []

def fill(coins,goal):
    answer = []

    # print("called with coins / goal:")
    # print(str(coins) + " / " + str(goal))

    if goal == 0:
        return [set()]
    if goal == min(coins):
        return [[min(coins)]]

                            # assume COINS is in descending order for now
                            # starting from the largest,
    for coin in coins:
        x = goal - coin
        if x > 0:

            #print("Calling function with goal of " + str(x))

            fills = fill(coins,x)

            #print("fills looks like:" + str(fills))

            for count in range(len(fills)):
                combination = fills[count]
                print("combination looks like: " + str(combination))
                combination.append(coin)
                answer.append(combination)

    return answer




if __name__ == "__main__":
    coins = [200,100,50,20,10,5,2,1]
    goal = 200
    print(fill(coins,goal))