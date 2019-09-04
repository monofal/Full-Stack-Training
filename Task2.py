import sys


def multiplyDigitsOfNumber(inputNum):
    lstDigits = list(str(inputNum))
    result = 1;
    for c in lstDigits:
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
        print(multiplyDigitsOfNumber(argument))
    except IndexError:
        print("Error: No argument supplied.")


if __name__ == "__main__":
    main(sys.argv)
