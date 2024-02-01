#!/usr/bin/python3

def mergeAlternately(word1: str, word2: str) -> str:
    """
    This function takes two words and merges them alternatively.

    Args:
    word1-Just a simple word
    word2-Just a simple word

    Return:
    A string which has both words which have been merged
    alternatively.
    """
    # Initialize an empty string
    merged = ""

    # Find the lengths of the strings
    len_word1, len_word2 = len(word1), len(word2)

    # Find the max value of the lengths
    max_len = max(len_word1, len_word2)

    # Iterate through the strings by using max as the range
    for i in range(max_len):
        if i < len_word1:
            merged += word1[i]
        if i < len_word2:
            merged += word2[i]

    return merged

# Test cases
# Test 1
word1 = "abc" 
word2 = "pqr"
result = mergeAlternately(word1, word2)
print("Word1 is {}, Word2 is {}. The result is {}".format(word1, word2, result))
