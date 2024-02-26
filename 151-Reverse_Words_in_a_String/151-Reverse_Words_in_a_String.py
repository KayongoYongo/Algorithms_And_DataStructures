#!/usr/bin/python3

def reverseWords(s: str) -> str:
    """
    A function that reverses the words
    in a strings

    Args:
        s: The string to be reversed

    Return:
        string that has been reversed
    """

    # Remove the white spaces before and after the string
    stripped_words = s.strip()

    # Remove any whtespaces within the string
    split_string = stripped_words.split()

    # The above function converts the string to a list

    # Next reverse the string.
    split_string.reverse()

    # Lastly, return the string by converting the list
    return (' '.join(split_string))

# Example 1
string1 = "the sky is blue"
print("The string, '{}' in reverse is '{}'.".format(string1, reverseWords(string1)))

# Example 2
string2 = "  hello world  "
print("The string, '{}' in reverse is '{}'.".format(string2, reverseWords(string2)))

# Example 3
string3 = "a good   example"
print("The string, '{}' in reverse is '{}'.".format(string3, reverseWords(string3)))
