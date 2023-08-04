if __name__ == '__main__':
    inputText = open("PythonString.txt", "r").read()
    # print(inputText)
    inputText = inputText.replace('.', '')  # Remove .
    words = inputText.split()  # Could use .lower() if case sensitivity is not needed
    # print(words)

    # Compute the amount of words coming up in the string input
    wordCounts = {}
    for word in words:
        wordCounts[word] = wordCounts.get(word, 0) + 1
    # print(wordCounts)

    # Compute the probability of a word coming up in the string input
    probs = []
    length = len(words)
    for word in wordCounts.keys():
        wordCounts[word] = int((wordCounts.get(word) / length) * 100)

    # Print the percentages
    print(inputText)
    for key in wordCounts.keys():
        print(key, "-", wordCounts.get(key), "%")
