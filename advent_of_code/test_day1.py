# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:14:15 2018

@author: jostev
"""

from day1 import drift


def test_all_positive():
    result = drift(['+1', '+1', '+1'])
    assert result == 3


def test_adds_to_zero():
    result = drift(['+1', '+1', '-2'])
    assert result == 0


def test_negative_result():
    result = drift(['-1', '-2', '-3'])
    assert result == -6
