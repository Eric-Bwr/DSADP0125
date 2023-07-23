import random
from copy import copy


class Aufgabe2:
    def __init__(self):
        self.numberCount = 50
        self.numberIteration = 25
        self.minNumber = 0
        self.maxNumber = 100

        self.iterate()

    def iterate(self):
        queue = self.fillQueue()
        queueLeft = copy(queue)
        queueRight = copy(queue)
        for i in range(self.numberIteration):
            self.shiftLeft(queueLeft)
            self.shiftRight(queueRight)
        print("Shifted Left: ", queueLeft)
        print("Shifted Right: ", queueRight)

    def fillQueue(self):
        queue = []
        for i in range(self.numberCount):
            queue.append(random.randint(self.minNumber, self.maxNumber))
        return queue

    def shiftRight(self, queue):  # Pop last element and insert at the beginning (push)
        elementRight = queue.pop()
        queue.insert(0, elementRight)

    def shiftLeft(self, queue):  # Pop first element and insert at the end (push_back)
        elementLeft = queue.pop(0)
        queue.append(elementLeft)


if __name__ == '__main__':
    Aufgabe2()
