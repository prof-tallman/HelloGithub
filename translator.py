#!/usr/bin/env python3
""" Program that translates between English and a simple version of the Pig
    Latin Language as defined by the piglatin module.
"""

import piglatin
import argparse


def main():
    ''' Main program for Piglatin Translator CLI Program. '''

    parser = argparse.ArgumentParser(
        description='Translates between Pig Latin and English')
    parser.add_argument(
        '-p', '--phrase', type=str, help='message to translate', required=True)
    parser.add_argument(
        '-m', '--mode', type=str, choices=['piglatin', 'english'],
        help='choose to translate to piglatin or english', required=True)
    parser.add_argument(
        '-v', '--verify', action='store_true',
        help='check if the phrase contains invalid characters')
    args = parser.parse_args()

    translator = piglatin.SimplifiedPiglatin()
    if args.verify:
        if args.piglatin and not translator.valid_phrase(args.piglatin):
            print('Error: the phrase contains invalid characters.')
            return
        elif args.english and not translator.valid_phrase(args.english):
            print('Error: the phrase contains invalid characters.')
            return

    if args.piglatin:
        print(translator.encrypt(args.piglatin))
    elif args.english:
        print(translator.decrypt(args.english))
    else:
        print('Error: no message to translate')
    return


if __name__ == '__main__':
    main()
