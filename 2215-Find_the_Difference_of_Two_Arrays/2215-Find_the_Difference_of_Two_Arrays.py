#!/usr/bin/python3

from typing import List

def findDifference(nums1: List[int], nums2: List[int]) -> List[List[int]]:
    """
    Description: This function finds the common elements 
    in array 1 and array 2

    Args:
    nums1 is an array of integers
    nums2 is an array of integers

    Return:
    An array containing distinct elements in array 1 and array 2
    """
    
    # Create an empty array to store the elements
    answer = []

    # Convert both elements to sets
    set1 = set(nums1)
    set2 = set(nums2)

    # Append the elements present in nums1 not present in nums2
    answer.append(list(set1 - set2))

    # Append elements present in nums2 not present in nums1
    answer.append(list(set2 - set1))

    return answer

# Example1
nums1 = [1,2,3]
nums2 = [2,4,6]
print("Example 1")
print("For {} and {}, the distinct integers in them are {}.".format(nums1, nums2, findDifference(nums1, nums2)))
