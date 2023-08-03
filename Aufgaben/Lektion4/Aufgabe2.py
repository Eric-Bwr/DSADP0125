def alphabetPosition(letter):
    res = ord(str(letter).lower()) - ord('a')
    if res < 0 or res > 25:
        return 0
    return res + 1


if __name__ == '__main__':
    S = "Eine alte Dame geht heute einkaufen."

    letterSum = 0

    for letter in S:
        position = alphabetPosition(letter)
        letterSum += position
        print("Letter: ", letter, " with Number: ", position)
    print("Number for String: ", letterSum)
