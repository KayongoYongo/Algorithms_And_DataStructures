def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Description:
        This function finds the largest possible sub string between two strings.

    Args:
        str1:Strings to check
        str2: Strings to check

    Return:
        The largest possible sub string
    """
    l1, l2 = len(str1), len(str2)

    """
    The for loop decides the size of the possible sub string.
    If we start from the beginning, eg for i in range(1, l1 + 1):
    This will check for the smalles possible sub string.
    If we start from the end, we will be checking for the largest possible sub string
    """
    for i in range(1, l1 + 1):
        # find the factors
        if l1 % i != 0:
            continue
        
        # finds the sub strings
        sub = str1[:i]

        # copies
        copies = l1 // i

        # check if copies
        if sub * copies != str1:
            continue

        # copies
        copies = l2 // i

        # check if copies
        if sub * copies != str2:
            continue

        return sub

    return ""

str1 ="ABCABC"
str2 ="ABC"
print(f"For {str1} and {str2}, the gcd of sub strings is {gcdOfStrings(str1, str2)}")