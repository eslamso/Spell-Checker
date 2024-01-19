class Format:
    underline = '\033[4m'
    end = '\033[0m'


def under_line(alist, misspelled):
    """print line under the misspelled words"""
    for word in alist:
        if word in misspelled:
            print(Format.underline + word + Format.end, end=" ")
        else:
            print(word, end=" ")


