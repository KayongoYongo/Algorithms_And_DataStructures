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
    s = s.strip()

    # Remove any whtespaces within the string
    word_list= s.split()

    # Use two pointer approach to switch the strings
    left, right = 0, len(word_list) - 1

    while left < right:
        word_list[left], word_list[right] = word_list[right], word_list[left]
        left += 1
        right -= 1
    
    return " ".join(word_list)

# Example 1
string1 = "the sky is blue"
print("The string, '{}' in reverse is '{}'.".format(string1, reverseWords(string1)))

# Example 2
string2 = "  hello world  "
print("The string, '{}' in reverse is '{}'.".format(string2, reverseWords(string2)))

# Example 3
string3 = "a good   example"
print("The string, '{}' in reverse is '{}'.".format(string3, reverseWords(string3)))
