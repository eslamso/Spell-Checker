def print_result(suggestions, misspelled_words):
    """
    print the misspelled words with its suggestions
    """
    if len(misspelled_words) == 0:
        print("\n***** There is no misspelled words *****")
    else:
        for x in suggestions:
            print("\nthe misspelled word is {" + x + "}  &&&    Its suggestions: {", end=" ")
            for y in suggestions[x]:
                if y == suggestions[x][len(suggestions[x]) - 1]:
                    print(y, end=" ")
                else:
                    print(y, end=", ")
            print("}", end=" ")
