"""
Example module to perform work with pyfiglet.
"""

import pyfiglet


def create_formatted_string(text: str) -> str:
    """
    Create some text using pyfiglet.

    Args:
        text: str
            The text to display.

    Returns:
        None
    """

    # return a string formatted by pyfiglet.
    return pyfiglet.figlet_format(text=text, font="slant")


def print_formatted_string(text: str) -> str:
    """
    Show some text through pyfiglet formatted string.

    Args:
        text: str
            The text to display.

    Returns:
        None
    """

    # print a string formatted by pyfiglet.
    print(create_formatted_string(text=text))
