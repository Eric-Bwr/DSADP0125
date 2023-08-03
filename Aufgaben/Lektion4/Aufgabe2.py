def alphabetPosition(letter):  # compute b mod 26
    # lowercase every letter so that it is case-insensitive
    # and subtract 97 (ord('a)) so that the letter 'a' is actually 0 and not 97
    res = ord(str(letter).lower()) - ord('a')
    if res < 0 or res > 25:  # mod 26 - make sure it is in range
        return 0  # return 0 for numbers that do not fit the mod 26 range
    return res + 1  # add one so the letter 'a' is taken into account


if __name__ == '__main__':
    S = "Eine alte Dame geht heute einkaufen."

    letterSum = 0

    for letter in S:  # Loop through all letters in string
        position = alphabetPosition(letter)  # Get the alphabet position ('a' starts at 1)
        letterSum += position  # Sum the positions
        print("Letter: ", letter, " with Number: ", position)
    print("Number for String: ", letterSum)
