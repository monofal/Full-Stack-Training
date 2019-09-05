import sys


def convert_dict_to_string(dict):
    str_output = ""
    for keys, values in dict.items():
        str_output += values

    return str_output


def remove_all_except_first(str_input):
    dic_removed_duplicates = {}
    for c in str_input:
        if str(c).upper() not in dic_removed_duplicates:
            dic_removed_duplicates[str(c).upper()] = c

    return convert_dict_to_string(dic_removed_duplicates)


def remove_first_occurrence(str_input):
    slow_index = 0
    fast_index = 1
    count = len(str_input)
    lstDeletedCharacters = list()

    while slow_index < count:
        if slow_index != fast_index and str_input[slow_index].upper() == str_input[fast_index].upper() \
                and lstDeletedCharacters.count(str_input[slow_index]) == 0:
            lstDeletedCharacters.append(str_input[slow_index])
            str_input = str_input[0:slow_index] + '*' + str_input[slow_index + 1:]

        fast_index += 1

        if fast_index >= count:
            slow_index += 1
            fast_index = 0

    str_input = str_input.replace("*", "")

    return str_input


def main(argv):
    try:
        str_rem_except_first = argv[1]
        str_rem_firstOcc = argv[2]
        print("Characters removed : ", remove_all_except_first(str_rem_except_first))
        print("First Occurrence removed : ", remove_first_occurrence(str_rem_firstOcc))
    except IndexError:
        print("Error: No valid argument supplied.")


if __name__ == "__main__":
    main(sys.argv)
