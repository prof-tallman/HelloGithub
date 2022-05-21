#!/usr/bin/env python3
""" A translator between English and a simplified version of the Pig Latin
    Language.
"""

class SimplifiedPiglatin:
    """ Translates between English and a simple version of Pig Latin. """

    vowels = 'aeiou'
    consonants = 'bcdfghjklmnpqrstvwxyz'

    def __init__(self):
        pass


    def valid_phrase(self, phrase):
        ''' Checks if a string contains only lowercase letters and spaces. '''

        phrase = phrase.replace(' ', '')
        return phrase.isalpha() and phrase.islower()


    def encrypt(self, english_phrase):
        ''' Converts a phrase to CSC314 Piglatin; assumes lowercase and
            no punctuation.
        '''

        # translate words one at a time, adding a space at the end of each word
        piglatin_phrase = ''
        for word in english_phrase.split():
            if word[0] in Translator.vowels:
                piglatin_phrase += word + "quay" + " "
            else:
                piglatin_phrase += word[1:] + word[0] + "ay" + " "

        # removes the trailing space
        return piglatin_phrase[:-1]


    def decrypt(self, piglatin_phrase):
        ''' Converts a phrase to Piglatin; assumes lowercase and no
            punctuation.
        '''

        # translate words one at a time, adding a space at the end of each word
        english_phrase = ''
        for word in piglatin_phrase.split():
            if not word.endswith('ay'):
                english_phrase += word + " "
                continue
            word = word[:-2]    # removes trailing 'ay'
            if word.endswith('qu'):
                english_phrase += word[:-2] + " "
            else:
                english_phrase += word[-1] + word[:-1] + " "

        # removes the trailing space
        return english_phrase[:-1]

    # end of Translator class


def run_unit_tests():
    """ Tests the 'encrypt' and 'decrypt' Pig Latin functions. """

    translator = SimplifiedPiglatin()

    english1 = "ice cream is the best thing since sliced bread"
    piglatin1 = "icequay reamcay isquay hetay estbay hingtay incesay licedsay readbay"

    test1a = translator.encrypt(english1)
    if test1a != piglatin1:
        print(f"FAILED: '{english1}' translated as '{test1a}' instead of '{piglatin1}'")

    test1b = translator.decrypt(piglatin1)
    if test1b != english1:
        print(f"FAILED: '{piglatin1}' translated as '{test1b}' instead of '{english1}'")

    # end of run_unit_tests


if __name__ == '__main__':
    run_unit_tests()
