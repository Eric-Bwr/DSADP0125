import random

from matplotlib import pyplot as plt


def encrypt(S, key):  # Just shifts the letters differently depending on case
    res = ""
    offset = key % 26
    for letter in S:
        if letter.isalpha():
            if letter.isupper():
                letterEncrypted = chr((ord(letter) - ord('A') + offset) % 26 + ord('A'))
            else:
                letterEncrypted = chr((ord(letter) - ord('a') + offset) % 26 + ord('a'))
            res += letterEncrypted
        else:
            res += letter
    return res


def decrypt(encryptedText, key):
    # We can just shift them back
    return encrypt(encryptedText, 26 - key)


# Compute the amount of letters of the input string (encryptedText) appearing in the alphabet and show it via plotly
def histogram(encryptedText):
    data = [0] * 26
    for letter in encryptedText:
        letter = letter.lower()
        if letter.isalpha():
            index = ord(letter) - ord('a')
            data[index] += 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    labels = [alphabet[i] for i in range(len(data))]
    plt.bar(labels, data)
    plt.title('Histogramm of the encrypted text')
    plt.legend()
    plt.show()


if __name__ == '__main__':
    S = "Eine alte Dame geht heute einkaufen."
    print("Input text: ", S)

    key = random.randint(0, 1000)

    encryptedText = encrypt(S, key)
    print("EncryptedText: ", encryptedText)
    print("Key: ", key)

    result = decrypt(encryptedText, key)
    print("Result: ", result)

    histogram(encryptedText)
