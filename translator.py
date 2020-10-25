
def create_word_list(filename) -> list:
    with open(filename, "r") as file:
        words = [word.strip() for word in file.readlines()]
    return words


def create_UKtoUS_dict(words) -> dict:
    UKtoUS = {}
    i = 0
    while i < len(words):
        UKtoUS[words[i]] = words[i+1]
        i += 2
    return UKtoUS


def create_UStoUK_dict(words) -> dict:
    UStoUK = {}
    j = 0
    while j < len(words):
        UStoUK[words[j+1]] = words[j]
        j += 2
    return UStoUK


def process_original_file(filename) -> list:
    with open(filename, "r") as file:
        allWords = file.readlines()
        allWords = [word.lower().strip() for word in allWords]
    return allWords


def take_text(text) -> list:
    allWords = text.split(" ")
    allWords = [word.lower().strip() for word in allWords]
    return allWords


def process_text(text) -> list:
    allWords = text.split(" ")
    allWords = [word.lower().strip() for word in allWords]
    return allWords


def create_translation(words, dialectDict) -> str:
    translation = ""
    for word in words:
        if word in dialectDict.keys():
            translation += dialectDict[word]
        else:
            translation += word
        translation += " "
    return translation


def main():
    myDict = {}
    translations = process_original_file("british-american-words.txt")
    # print(translations)
    startingDialect = input("What is your starting dialect? UK or US: ")
    if startingDialect.upper() == "UK":
        myDict = create_UKtoUS_dict(translations)
    elif startingDialect.upper() == "US":
        myDict = create_UStoUK_dict(translations)
    originalText = input("Please enter your original text: ")
    originalTextWords = take_text(originalText)
    print(create_translation(originalTextWords, myDict))


main()