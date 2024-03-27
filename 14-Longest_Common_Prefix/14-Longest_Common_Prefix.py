from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    """
    Description: 
        The function finds the longest common prefix in a list of strings

    Args: 
        strs: A list of strings

    Return:
        A string which is the common prefix among the strings
    """
    if strs is None:
        return ""
    
    # Find the length of the shortest string in the array
    min_length = min(len(s) for s in strs)

    # Create an outer loop that iterates through each character
    for i in range(min_length):
        # Iterate through all the strings ignoring the first
        # We do this since we are comparing its characters to the rest
        for j in range(1, len(strs)):
            # Compare characters at position i across all strings
            if strs[j][i] != strs[0][i]:
                return strs[0][:i]

    # Return the whole shortest string if all are identical
    return strs[0][:min_length]

print("Example 1")
strs = ["flower","flow","flight"]
print(f'The common sub string in {strs} is {longestCommonPrefix(strs)}')

print("Example 2")
strs = ["dog","racecar","car"]
print(f'The common sub string in {strs} is {longestCommonPrefix(strs)}')