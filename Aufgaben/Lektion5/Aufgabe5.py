import numpy as np


def generateAssetMatrices(numMatrices):
    res = []
    for _ in range(numMatrices):
        res.append(np.random.uniform(0, 100000, size=(1000, 1000)))
    return res


def mine(transactions):
    block = {
        "Transactions": transactions.copy(),
        "HashKey": np.random.randint(0, int(1e10))
    }
    return block


def findMinMaxAssets(chain):
    minAsset = float("inf")
    maxAsset = float("-inf")
    minBlock = None
    maxBlock = None

    for block in chain:
        for transaction in block["Transactions"]:
            assetMatrix = transaction["Asset"]
            assetValue = np.max(assetMatrix)

            if assetValue < minAsset:
                minAsset = assetValue
                minBlock = block

            if assetValue > maxAsset:
                maxAsset = assetValue
                maxBlock = block

    return minBlock, maxBlock


def simulate():
    chain = []
    transactions = []
    numTransactionsPerBlock = 10  # Should be 100 but that takes too long generating the matrices
    numBlocks = 100

    assetMatrices = generateAssetMatrices(numTransactionsPerBlock * numBlocks)

    for i in range(numBlocks):
        for j in range(numTransactionsPerBlock):
            assetMatrix = assetMatrices[i * numTransactionsPerBlock + j]
            transaction = {"Asset": assetMatrix}
            transactions.append(transaction)

        block = mine(transactions)
        chain.append(block)
        transactions = []

    minBlock, maxBlock = findMinMaxAssets(chain)

    print("Smallest: ")
    print(minBlock)
    print("\nLargest: ")
    print(maxBlock)


if __name__ == "__main__":
    simulate()
