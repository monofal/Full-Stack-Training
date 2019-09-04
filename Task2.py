def multiplyDigitsOfNumber(inputNum):
    lstDigits = list(str(inputNum))
    result = 1;
    for digit in lstDigits:
        result *= int(digit);

    return result;

print(multiplyDigitsOfNumber(1532))
