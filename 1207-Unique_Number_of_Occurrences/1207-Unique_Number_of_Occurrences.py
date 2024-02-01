#!/usr/bin/python3

from typing import List


def uniqueOccurrences(arr: List[int]) -> bool:
    """
    This function finds the unique occurences of a number
    in the list.

    Args:
        arr: A list containing a unique number of elements

    Return:
        A boolean value True or False
    """

    # Create a blank dictionary
    num_frequency = {}

    # Iterate through the list and append the uniuq appearance of a number to it
    # Additionally, set the number as the key
    for a in arr:
        # This code retieves the value associated with key a from the dictionary
        # if key a is not present, it returns the default value 0
        # if it is, 1 is added to the number
        num_frequency[a] = num_frequency.get(a, 0) + 1

    # Create a list to store the values
    values = list(num_frequency.values())

    # Check whether if they exist or not by using a set
    # The reason for using a set is cause it does not store duplicate values
    return len(values) == len(set(values))

# Test case 1
arr = [1,2,2,1,1,3]
result = uniqueOccurrences(arr)
print("For list {}. The result is {}".format(arr, result))

# Test case 2
arr = [1,2]
result = uniqueOccurrences(arr)
print("For list {}. The result is {}".format(arr, result))

# Test case 3
arr = [-3,0,1,-3,1,1,1,-3,10,0]
result = uniqueOccurrences(arr)
print("For list {}. The result is {}".format(arr, result))
