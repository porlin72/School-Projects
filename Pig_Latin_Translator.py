"""Pig Latin Translator"""
pyg = 'ay'

original = raw_input('Enter a word:')

word = original.lower()
first = original[0]

# Check for a valid input by the user
if len(original) > 0 and original.isalpha():
    # Checks if the first letter of the word is a vowel
    if first == 'a' or first == 'e' or first == 'i' or first == 'o'                  or first ==  'u':
        new_word = original + pyg
        print new_word
    else:
        new_word = original[1:] + original[0] + pyg
        print new_word
else:
    print 'empty'