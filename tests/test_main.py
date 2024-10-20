"""
Tests functionality found in main.py
"""

from example_package import create_formatted_string


def test_create_formatted_string() -> None:
    """
    Tests create_formatted_string
    """

    assert isinstance(create_formatted_string("Festina lente."), str)
