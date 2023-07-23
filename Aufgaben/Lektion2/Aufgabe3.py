import numpy.random


class Aufgabe3:
    def __init__(self):
        self.N = 100
        self.STD_DEVIATION = 50
        self.MEAN = 50
        # Erstelle ein N x N array mit 0
        self.matrix = [[0 for _ in range(self.N)] for _ in range(self.N)]
        for x in range(self.N):
            for y in range(self.N):
                value = numpy.random.normal(loc=self.MEAN, scale=self.STD_DEVIATION)
                self.matrix[x][y] = value
                self.matrix[y][x] = value

        for x in range(self.N):
            print(self.matrix[x])


if __name__ == '__main__':
    Aufgabe3()
