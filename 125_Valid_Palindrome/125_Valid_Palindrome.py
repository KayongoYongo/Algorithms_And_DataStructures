#!/usr/bin/python3

def isPalindrome(s: str) -> bool:
    """
    Description:
        This function returns True if palindrome
        or False if not.

    Args:
        s: The string to be checked

    Return:
        True or False
    """
    if s == " ":
        return true

    cleaned_string = ""

    # Clean the string is alphanumeric and convert to lowercase
    for char in s:
        if char.isalnum():
            cleaned_string += char.lower()

    # Remove the white spaces from the string and convert it back to a string
    cleaned_string = "".join(cleaned_string.split())

    # Finally, check if the string is a palindrome
    return cleaned_string == cleaned_string[::-1]

s = "A man, a plan, a canal: Panama"
print("The string is {}.".format(s))
print("Is the string a palindrome? {}.".format(isPalindrome(s)))
