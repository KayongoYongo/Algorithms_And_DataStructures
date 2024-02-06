#!/usr/bin/python3

def reverseVowels(s: str) -> str:
    """
    Description:
        This function takes in a string
        and reverses the vowels in it.

    Args:
        s: The string

    Return:
        A string with the vowels reversed
    """
    vowels = set("aeiouAEIOU")
    s_string = list(s)
    # For this problem, the two pointer approach is suitable
    i, j = 0, len(s_string) - 1

    # The loop continues as long as the pointers do not meet each other
    while i < j:
        # Move both pointers until a vowel is met
        while i < j and s_string[i].lower() not in vowels:
            i += 1
        while i < j and s_string[j].lower() not in vowels:
            j -= 1
        
        # Once the vowels have been met, switch their positions
        s_string[i], s_string[j] = s_string[j], s_string[i]
        i += 1
        j -= 1

    return ''.join(s_string)

# Test case 1
s = "Hello"
reversed_s = reverseVowels(s)
print("The string is {}. When the vowels have been reversed, the string becomes {}.".format(s, reversed_s))
