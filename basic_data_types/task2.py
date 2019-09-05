"""
Include tasks for basic data types and  exception handling
"""

import sys


def multiply_digits_of_number(number):
    """
    Returns product of digits in a number
    """
    if not isinstance(number, int):
        raise TypeError('Must be an integer')

    product = 1
    while number:
        digit = number % 10
        product *= digit
        number //= 10

    return product


def main(argv):
    """
    Main entry point of program
    """
    try:
        argument = int(argv[1])
        print(multiply_digits_of_number(argument))
    except IndexError:
        print("Error: No argument supplied.")
    except ValueError:
        print("Error: Invalid integer.")


if __name__ == "__main__":
    main(sys.argv)
