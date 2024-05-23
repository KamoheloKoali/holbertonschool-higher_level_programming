#!/usr/bin/python3
"""
5-text_indentation.py prints a text with 2 new lines after each of these characters: ., ? and :

Examples:
    >>> text_indentation("Hello. How are you? I'm fine.")
    Hello.

    How are you?

    I'm fine.
    >>> text_indentation("This is a test: does it work? Yes, it does.")
    This is a test:

    does it work?

    Yes, it does.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (string): first parameter

    Raises:
        TypeError: if text is not a string
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    delimiters = ".?:"

    for character in text:
        for delimiter in delimiters:
            if character is delimiter:
                print(character, end="")
                print("\n" * 2)
                break
        if character in delimiters:
            continue
        print(character, end="")
