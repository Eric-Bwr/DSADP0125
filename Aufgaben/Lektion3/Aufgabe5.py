import random

if __name__ == '__main__':
    numberOfIterations = 100000
    amountWon = 0
    amountSpent = 0  # Will be equal to the iteration count but one can actually
    # put in prices and costs thus this is more future-proof

    # Choose 6 random numbers out of 49
    # Sample is used because it makes sure that there are no duplicates
    # The winning numbers
    numbersWinning = random.sample(range(1, 50), 6)
    for _ in range(numberOfIterations):
        # And for the player
        numbersForPlayer = random.sample(range(1, 50), 6)
        # This just computes the amount of duplicates in the list to see if a player got a winning number
        matchingNumbers = 0
        for i in range(len(numbersForPlayer)):
            for x in range(len(numbersWinning)):
                if numbersForPlayer[i] == numbersWinning[x]:
                    matchingNumbers += 1

        # To make it more realistic one can put in actual prizes (with tax) and costs. Here we just add 1 "credit" per
        # winning number, one may want to set actual prizes per amount of winning numbers. And actual costs per "ticket"
        amountWon += 1 * matchingNumbers
        amountSpent += 1

    print("Amount Won: ", amountWon)
    print("Amount Spent: ", amountSpent)
    print("Total Yield: ", amountWon - amountSpent)
