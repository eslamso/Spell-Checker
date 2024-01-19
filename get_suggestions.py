from difflib import SequenceMatcher
from selection_sort import selection_sort
def get_suggestions(misspilled, dictionary):
    """Determine the percentage of similarity between words and return dictionary its keys the misspelled words
    and the values are the suggestion words
    """
    n = int(input("enter the number of suggested words you want :"))
    suggestions = {}
    s = SequenceMatcher()
    for word in misspilled:
        result = []
        s.set_seq1(word)
        for w in dictionary:
            s.set_seq2(w)

            if s.real_quick_ratio() >= .50 and \
                    s.quick_ratio() >= .60 and \
                    s.ratio() >= .65:
                result.append((s.ratio(), w))
        result = selection_sort(result,n)
        suggestions[word] = result

    return suggestions
