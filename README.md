# HelloGithub
Example of a basic software repository

## Purpose
Implements a simplified Pig Latin translator that was designed for the English language. It assumes that any message is written in all lowercase and only contains letters and spaces. Punctuation will not be translated correctly.

## Files
The main program file is `transltor.py` which wraps the translation object in a simple command line interface. The translation object is in the file `piglatin.py` and it includes a short unit test.

## Version
Requires python3 and the `argparse` module.

## Usage
```
python translator.py "hello try this" piglatin
python translator.py "ellohay rytay histay" english
```

## Language Rules
### Converting from English to Pig Latin
* Words that begin with a vowel (aeiou but not y) have the fake syllable "quay" added to the end
* Words that begin with a consonant (includes y) have their first letter moved to the tail and the letters "ay" appended
### Converting from Pig Latin to English
* Words that end with 'quay' have the last four letters removed.
* Words that only end in 'ay' have the last two letters removed and the new tail letter is moved to the head.

## Testing
The piglatin module contains a short unit test that verifies the object translates from English to Pig Latin correctly and vice-versa.
```
English: "ice cream is the best thing since sliced bread"
Piglatin: "icequay reamcay isquay hetay estbay hingtay incesay licedsay readbay"
```
