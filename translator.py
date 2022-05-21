#!/usr/bin/env python3
""" Program that translates between English and a simple version of the Pig
    Latin Language as defined by the piglatin module.
"""

import piglatin
import argparse


def main():
    ''' Main program for Piglatin Translator CLI Program. '''

    parser = argparse.ArgumentParser(description='Translates between Piglatin and English')
    parser.add_argument('phrase', type=str, help='message to translate')
    parser.add_argument('mode', type=str, choices=['piglatin', 'english'],
                        help='choose to translate to piglatin or english')
    args = parser.parse_args()

    translator = piglatin.SimplifiedPiglatin()
    if args.mode == 'piglatin':
        print(translator.encrypt(args.phrase))
    elif args.mode == 'english':
        print(translator.decrypt(args.phrase))
    else:
        print('Error: unexpected translation mode')

    return


if __name__ == '__main__':
    main()
