# -*- coding: utf-8 -*-
"""
Created on Tue Dec 18 13:14:01 2018

@author: jostev
"""


def main():
    """
    This is the function that gets run when the file is run as a script
    :return:
    """
    # Read in the data from file
    with open('day1_input.txt') as f:
        data = f.read()

    changes = data.strip().split('\n')

    print(drift(changes))


def drift(changes):
    """
    Calculate the final drift after applying all changes.
    """
    print(f'my_namespace is {__name__}')
    running_total = 0
    for item in changes:
        running_total += int(item)

    return running_total


if __name__ == '__main__':
    main()
