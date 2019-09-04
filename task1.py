"""
Include tasks for basic data types and  exception handling
"""
import argparse


def remove_all_except_first(word):
    """
    Remove all characters in a string except first occurrence of that character
    """
    no_duplicates = ''
    for character in word:
        # check for both upper and lower cases
        if str(character).upper() not in no_duplicates.upper():
            no_duplicates += character

    return no_duplicates


def remove_first_occurrence(word):
    """
    Remove first occurrence of of a character in a string
    Limitations : As this method uses special character
    (asterik) , if asterik appears in an input string it won't work.
    """
    # keep two indexes , one will sit (slow index) at a position and
    # the  other (fast_index) will loop through remaining characters in a string
    slow_index = 0
    fast_index = 1
    character_count = len(word)
    # list to keep track of characters that are deleted
    deleted_characters = list()

    while slow_index < character_count:

        # check if fast_index is not outside the bounds of array
        # check if character is not already deleted from the string
        if fast_index < character_count and word[slow_index].upper() == word[fast_index].upper() \
                and deleted_characters.count(word[slow_index]) == 0:
            deleted_characters.append(word[slow_index])
            # replace deleted character with a special character
            word = word[0:slow_index] + '*' + word[slow_index + 1:]

        fast_index += 1

        # if fast_index reaches at the end, move slow_index to next character and
        # move fast_index one place next to slow_index
        if fast_index >= character_count:
            slow_index += 1
            fast_index = slow_index + 1

    # replace special character from the string to generate output
    word = word.replace("*", "")

    return word


def main():
    """
    Main entry point of program
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("no_duplicates", help="Remove All Except First")
    parser.add_argument("remove_first", help="Remove First Occurrence")

    args = parser.parse_args()
    print("Characters removed : ", remove_all_except_first(args.no_duplicates))
    print("First Occurrence removed : ", remove_first_occurrence(args.remove_first))


if __name__ == "__main__":
    main()
