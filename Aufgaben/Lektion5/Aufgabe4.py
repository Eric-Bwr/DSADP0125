from math import sqrt
import numpy.random

if __name__ == '__main__':
    N = 250
    K = 100
    STD_DEVIATION = sqrt(50)
    MEAN = 50

    # Erstelle ein N x N array mit 0
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    y = 0
    for x in range(N):
        matrix[x][y] = 1
        if y <= K:
            value = numpy.random.normal(loc=MEAN, scale=STD_DEVIATION)
            if x + 1 < N:
                matrix[x + 1][y] = value
            if y + 1 < N:
                matrix[x][y + 1] = value
        y += 1

    # for x in range(N):
    #     print(matrix[x])

    numSimulations = 1000
    pathLengths = []

    for _ in range(numSimulations):
        path = []
        currentNode = (0, 0)

        while currentNode != (N - 1, N - 1):
            path.append(currentNode)
            x, y = currentNode
            rightValue = matrix[x + 1][y] if x + 1 < N else None
            downValue = matrix[x][y + 1] if y + 1 < N else None

            if rightValue is None and downValue is None:
                break

            if rightValue is None:
                currentNode = (x, y + 1)
            elif downValue is None:
                currentNode = (x + 1, y)
            else:
                if rightValue >= downValue:
                    currentNode = (x + 1, y)
                else:
                    currentNode = (x, y + 1)

        pathLengths.append(len(path))

    print("Median length:", sum(pathLengths) / numSimulations)

