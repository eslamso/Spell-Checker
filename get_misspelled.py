from binary_search import binary_search


def get_misspelled(text, dictionary):
    """check if word is digit or not and return list of misspelled words"""
    misspelled = []
    for word in text:
        if not len(word) == 0 and not word.isdigit():
            if not binary_search(dictionary, word):
                misspelled.append(word)
    return misspelled
