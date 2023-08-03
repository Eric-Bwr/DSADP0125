def calcFibonacciUntilN(n):
    fiboLeft = 0
    fiboRight = 1
    for i in range(n):
        temp = fiboLeft + fiboRight
        fiboLeft = fiboRight
        fiboRight = temp
    return fiboLeft


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    fiboNumber = calcFibonacciUntilN(25)
    print("Fibo Number: ", fiboNumber)
    while not isPrime(fiboNumber):
        fiboNumber += 1
    print("First Prime-Number after 25th. Fibo-Number: ", fiboNumber)
