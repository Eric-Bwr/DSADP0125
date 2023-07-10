def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


if __name__ == '__main__':
    primeCounter = 0
    number = 2
    while primeCounter < 1000:
        if isPrime(number):
            primeCounter += 1
        number += 1
    print(number - 1)
