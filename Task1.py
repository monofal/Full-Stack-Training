import sys


def convertDictToString(dict):
    strOutput = ""
    for keys, values in dict.items():
        strOutput += values

    return strOutput


def removeAllExceptFirst(strInput):
    dicRemoveDuplicates = {}
    for c in strInput:
        if str(c).upper() not in dicRemoveDuplicates:
            dicRemoveDuplicates[str(c).upper()] = c

    return convertDictToString(dicRemoveDuplicates)


# This one works fine but 2nd method is more memory efficient for larger strings
# def removeFirstOccurrence(strInput):
#     lstRemoveFirstOccurrence = list()
#     lstTemp = list()
#     lstDeletedItems = list()
#
#     for c in strInput:
#         lstRemoveFirstOccurrence.append(str(c).upper())
#         lstTemp.append(c)
#
#     index = 0;
#     for item in lstRemoveFirstOccurrence:
#         if lstRemoveFirstOccurrence.count(item) > 1 and lstDeletedItems.count(item) == 0:
#             lstRemoveFirstOccurrence.remove(item)
#             lstTemp.remove(lstTemp[index]);
#             lstDeletedItems.append(item)
#
#         index += 1;
#
#     print(*lstTemp, sep="")
#     return ""


def removeFirstOccurrence(strInput):
    slowIndex = 0
    fastIndex = 1
    count = len(strInput)
    lstDeletedCharacters = list()

    while slowIndex < count:
        if slowIndex != fastIndex and strInput[slowIndex].upper() == strInput[fastIndex].upper() \
                and lstDeletedCharacters.count(strInput[slowIndex]) == 0:
            lstDeletedCharacters.append(strInput[slowIndex])
            strInput = strInput[0:slowIndex] + '*' + strInput[slowIndex + 1:]

        fastIndex += 1

        if fastIndex >= count:
            slowIndex += 1
            fastIndex = 0

    strInput = strInput.replace("*", "")

    return strInput


def main(argv):
    try:
        strRemExceptFirst = argv[1]
        strRemFirstOcc = argv[2]
        print("Characters removed : ", removeAllExceptFirst(strRemExceptFirst))
        print("First Occurrence removed : ", removeFirstOccurrence(strRemFirstOcc))
    except IndexError:
        print("Error: No valid argument supplied.")


if __name__ == "__main__":
    main(sys.argv)
