
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


def process_original_file(filename):
    with open(filename, "r") as file:
        allWords = file.read().split(" ")
        allWords = [word.strip() for word in allWords]
    return allWords


wordList = create_word_list("british-american-words.txt")
print(create_UStoUK_dict(wordList))
print(create_UKtoUS_dict(wordList))