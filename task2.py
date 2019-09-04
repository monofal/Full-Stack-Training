"""
Include tasks for basic data types and  exception handling
"""
import argparse


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


def main():
    """
    Main entry point of program
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("number", help="Integer Value")
    args = parser.parse_args()

    try:
        number = int(args.number)
        print(multiply_digits_of_number(number))
    except ValueError:
        print("TypeError: Must be an integer")


if __name__ == "__main__":
    main()
