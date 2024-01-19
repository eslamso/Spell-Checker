from read_dictionary import dictionary
from get_misspelled import get_misspelled
from get_suggestions import get_suggestions
from print_result import print_result
from remove_punctuation import remove_punctuation
from under_line import under_line

print('********* Welcome to spell checker program *********\n')

my_dictionary = dictionary()  # list of dictionary words

text = input('Type your text to be checked: ')
text = text.lower().split()  # list of text words
text = remove_punctuation(text)
misspelled_words = get_misspelled(text, my_dictionary)
under_line(text, misspelled_words)
suggestions = get_suggestions(misspelled_words, my_dictionary)
print_result(suggestions, misspelled_words)
