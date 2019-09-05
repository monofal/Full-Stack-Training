import sys


def multiply_digits_of_number(inputNum):
    lst_digits = list(str(inputNum))
    result = 1;
    for c in lst_digits:
        try:
            digit = int(c)
            result *= digit
        except ValueError:
            print("Error: Invalid input integer.")
            sys.exit()

    return result;


def main(argv):
    try:
        argument = argv[1]
        print(multiply_digits_of_number(argument))
    except IndexError:
        print("Error: No argument supplied.")


if __name__ == "__main__":
    main(sys.argv)
