import numpy as np
from matplotlib import pyplot

# Addition von unabhängigen Normalverteilungen
if __name__ == '__main__':
    loc = 10  # mu, average value, the resulting value should be close to this one
    scale = 2  # sigma, deviation
    numberOfNormalLists = 1000
    numberOfNormalPerList = 10000

    normalsList = []
    averageOfNormals = []
    for i in range(numberOfNormalLists):
        normals = np.random.normal(loc, scale, numberOfNormalPerList)  # Generate numberOfNormalPerList´s normals
        normalsList.append(normals)
        averageOfNormals.append(np.sum(normals) / numberOfNormalPerList) # Prepare the average

    print(averageOfNormals)  # Average per individual normal
    print(np.sum(averageOfNormals) / numberOfNormalLists)  # Should be close to loc / mu

    # Graphical representation of the first normal list, more or less for debugging
    pyplot.hist(normalsList[0], bins=50, density=True, label='Normal')
    pyplot.title('Normal distribution of ')
    pyplot.legend()
    pyplot.show()
