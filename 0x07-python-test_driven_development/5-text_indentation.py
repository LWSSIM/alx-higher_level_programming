#!/usr/bin/python3
'''
    fn to indent text
'''


def text_indentation(text):
    '''
    formats and print input text with 2*'\n' per sentence

    Args:
        text: input

    Raises:
        on bad format raises type err

    Note:
        - Delimiters define sentences, prints 1 sentence/line /
            Prints newline after each line

        leading / trailling spaces in each line /
        are ommited.
        recursive ' ' inside a line is replcaed by a single ' '
    '''
    if not isinstance(text, str) or text is None:
        raise TypeError('text must be a string')

    delimiters = [".", "?", ":"]
    is_space = 1

    for char in text:
        if char.isspace():
            if is_space == 1:
                continue
            print(" ", end='')
            is_space = 1
        elif char in delimiters:
            print(char + '\n\n', end='')
            is_space = 1
        else:
            print(char, end='')
            is_space = 0

