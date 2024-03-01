#!/usr/bin/python3

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    This function merges a sorted array

    Args:
        num1: a list
        num2: a list
        m: number of elements in list1
        n: number of elements in list2

    Return:
        None
    """

    # Append list2 to list 1
    nums1.extend(nums2)
    final_length = m + n

    # Create two empty pointers to move non zero elements
    i = 0
    j = 0

    # Iterate through the array moving the zeros
    for i in range(len(nums1)):
        if nums1[i] != 0:
            nums1[i], nums1[j] = nums1[j], nums1[i]
            j += 1

    del (nums1[final_length:])
    nums1 = nums1.sort()

nums1 = [1,2,3,0,0,0]
print("nums1 is {}".format(nums1))
m = 3
print("m is {}".format(m))
nums2 = [2,5,6]
print("nums2 is {}".format(nums2))
n = 3
print("n is {}".format(n))
print("The result is {}.".format(merge(nums1, m, nums2, n)))
