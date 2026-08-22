alphabet = {
    "a": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "b": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "c": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "d": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "e": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "f": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "g": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "h": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "i": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "j": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "k": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "l": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "m": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "n": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "o": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "p": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "q": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "r": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "s": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "t": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "u": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "v": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "w": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "x": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "y": ["N/A", "N/A", "N/A", "N/A", "N/A"],
    "z": ["N/A", "N/A", "N/A", "N/A", "N/A"]

    }

dictionary = []
with open("AI/WordleWords.txt", "r") as infile:
    dictionary = infile.readlines()
all_guesses = []


def guessWord(all_guesses, dictionary, alphabet):
    if len(all_guesses) == 0:
        return "slate"
    
    # reading the blacks, yellows and greens

    letter = 0
    yellows = []
    
    for letter in range(0, 5):
        if all_guesses[-1][1][letter] == "B":
            for i in range(0, 5):
                alphabet[all_guesses[-1][0][letter]][i] = "B"
        if all_guesses[-1][1][letter] == "Y":
            alphabet[all_guesses[-1][0][letter]][letter] = "Y"
            yellows.append(alphabet[all_guesses[-1][0][letter]][letter])
        if all_guesses[-1][1][letter] == "G":
            for k,v in alphabet.items():
                alphabet[k][letter] = "B"
            alphabet[all_guesses[-1][0][letter]][letter] = "G"

    # popping impossible words

    dictpop = 0
    letter = 0
    while dictpop < len(dictionary):
        for letter in range(0, 5):
            if alphabet[dictionary[dictpop][letter]][letter] in ["B", "Y"]:
                dictionary.pop(dictpop)
                dictpop -= 1
                break
        if yellows not in dictionary[dictpop]:
            dictionary.pop(dictpop)
            dictpop -= 1
        dictpop += 1

    # returning the best word

    return dictionary[0]

while True:    
    nextGuess = guessWord(all_guesses, dictionary, alphabet)
    print(nextGuess)
    BYG = input()
    all_guesses.append((nextGuess, BYG))
