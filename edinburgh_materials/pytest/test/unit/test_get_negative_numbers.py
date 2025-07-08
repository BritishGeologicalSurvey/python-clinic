"""
Tests for get_negative_numbers.py

On Windows PowerShell, set the PYTHONPATH to be able to import modules.
$env:PYTHONPATH = $pwd
"""
import pytest

from get_negative_numbers import is_negative


@pytest.mark.parametrize(('number', 'result'), [
    (-1, True),
    (0, False),
    (3, False),
    (-2.34, True),
    (3.14, False),
    ('−4', True),  # U+2212 Minus sign
    ('-5', True),  # U+002D Hyphen-minus
    ('‐6', True),  # U+2010 Hyphen
    (1e10, False),
    (1e-10, False),
    (-1e10, True),
    (-1e-10, True),
])
def test_is_negative(number, result):
    assert is_negative(number) is result


@pytest.mark.parametrize('number', [
    'three',
    '- three',
    True
])
def test_is_negative_invalid_numbers_raises_valueerror(number):
    with pytest.raises(ValueError, match="Cannot convert number to int"):
        is_negative(number)
