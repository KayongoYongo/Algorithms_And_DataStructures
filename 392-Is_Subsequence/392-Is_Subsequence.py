def isSubsequence(s: str, t: str) -> bool:
    """
    Description:
        The function checks whether a string is a subsequence of another.
        A subsequence of a string is a new string that is formed from 
        the original string by deleting some (can be none) 
        of the characters without disturbing the relative 
        positions of the remaining characters
    
    Args:
        s: A string
        t: A string

    Return:
        True if t is a subsequesnce of s. Otherwise,
        false
    """
    # Create two pointers and initialize their valuers to 0
    i, j = 0, 0

    # Pointer i will point towards the staart of s, while j will point at t
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1

    # Checks if the value of the pointer is equal to the length of the subsequence
    return True if i == len(s) else False

s = "abc"
t = "ahbgdc"
print(f"{s} is a s ubsequence of {t}. Result is {isSubsequence(s,t)}")

s = "axc"
t = "ahbgdc"
print(f"{s} is a s ubsequence of {t}. Result is {isSubsequence(s,t)}")