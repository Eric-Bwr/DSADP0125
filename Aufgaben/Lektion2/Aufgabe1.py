import random


# Approximation
class Aufgabe1:
    def __init__(self):
        self.numberCount = 25  # Testing: 1
        self.minNumber = 0  # Testing: 0
        self.maxNumber = 100  # Testing: 1 or 2 or 3
        self.numberIteration = 100000
        self.foundIdenticalList = 0
        self.probabilityOfDuplicate = 0

        self.iterate()

    def iterate(self):
        lists = []
        for i in range(self.numberIteration):
            lists.append(self.prepareList())
        for listElement in range(self.numberIteration):  # Prüfe jede liste auf eine dopplung
            for listToCompare in range(self.numberIteration):
                if listToCompare != listElement:
                    if lists[listToCompare] == lists[listElement]:
                        self.foundIdenticalList += 1
        self.probabilityOfDuplicate = self.foundIdenticalList / (self.numberIteration * self.numberIteration)
        self.probabilityOfDuplicate *= 100.0
        print(self.probabilityOfDuplicate)

    def prepareList(self):
        list = []
        for i in range(self.numberCount):
            randNumber = random.randint(self.minNumber, self.maxNumber)
            # Entferne alle Elemente, die größer sind als die neue Zahl (randNumber)
            # [1, 2, 5, 6]
            # Neue Zahl: 3
            # Entferne Zahl 5 und größer durch pop()
            # Restliche Werte Liste: [6, 5] <- Falsch herum
            # [1, 2]
            # Füge neue Zahl ein durch append()
            # [1, 2, 3]
            # Füge restliche Zahlen ein durch append()
            # [1, 2, 3, 5, 6]

            restValues = []
            numbersToRemove = 0

            for x in range(len(list)):
                if list[x] > randNumber:
                    numbersToRemove += 1
            for x in range(numbersToRemove):
                restValues.append(list.pop())
            # print("Füge an: ", randNumber)
            # print("Liste vor Hinzufügen restlicher Werte: ", list)
            list.append(randNumber)
            for x in range(len(restValues)):
                list.append(restValues[len(restValues) - 1 - x])
            # print("Finale liste pro Iteration: ", list)
        return list


if __name__ == '__main__':
    Aufgabe1()
