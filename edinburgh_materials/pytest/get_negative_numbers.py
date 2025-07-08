"""Script to return negative numbers from a list."""
import time


def get_negative_numbers(numbers):
    time.sleep(15)
    negative_numbers = [number for number in numbers
                        if is_negative(number)]
    return negative_numbers


def is_negative(number):
    """
    Function should handle integers, floats and string representations of
    each.  It should raise a helpful error if number cannot be converted.
    """
    # Don't accept booleans
    if isinstance(number, bool):
        msg = f"Cannot convert number to int: '{number}'"
        raise ValueError(msg)

    # Check hyphens
    acceptable_minus_signs = str.maketrans({"−": "-", "‐": "-"})
    if isinstance(number, str):
        number = number.translate(acceptable_minus_signs)

    # Make sure the number can be converted
    try:
        int(number)
    except ValueError:
        msg = f"Cannot convert number to int: '{number}'"
        raise ValueError(msg)

    return str(number).startswith('-')


if __name__ == "__main__":
    numbers = [1, -2, 3, -6, -18, 200, -7, '-3', '3', 'three', 'minus three', '‐6']
    print(get_negative_numbers(numbers))
