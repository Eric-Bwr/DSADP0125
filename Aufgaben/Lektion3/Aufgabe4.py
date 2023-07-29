import random
from random import randint

# Easy to understand document
# https://www.philoclopedia.de/2019/08/14/das-monty-hall-problem/


if __name__ == '__main__':
    numberOfMontyHallSimulations = 100000

    stickWins = 0
    switchWins = 0

    for _ in range(numberOfMontyHallSimulations):
        # Pick random number between 0 and 2 (giving three possible doors to choose from)
        # For the participant picked door:
        pickedDoor = randint(0, 2)
        # For the winning door:
        winningDoor = randint(0, 2)

        # Get the door/s that the monty could open (must be not the picked door and not the winning door)
        looseDoors = []
        for door in range(3):
            if door != pickedDoor and door != winningDoor:
                looseDoors.append(door)
        # Open one randomly
        openedByMonty = random.choice(looseDoors)

        # Compute the door that was not opened by the participant and not by the monty
        switchedChoice = 0
        for door in range(3):
            if door != pickedDoor and door != openedByMonty:
                switchedChoice = door

        # Increment the win counters if successfully opened correct door
        if pickedDoor == winningDoor:
            stickWins += 1

        if switchedChoice == winningDoor:
            switchWins += 1

    # Compute probs
    stickProb = stickWins / numberOfMontyHallSimulations
    switchProb = switchWins / numberOfMontyHallSimulations

    print("Stick door wins: ", stickProb)
    print("Switch door wins: ", switchProb)
