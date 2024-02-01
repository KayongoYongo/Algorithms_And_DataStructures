#!/usr/bin/python3

import copy
from typing import List

def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    # Create variables
    count = 0
    new_count = 0
    last = len(flowerbed)
    
    # Creare a deep copy of the flowerbed list
    flower_copy = copy.deepcopy(flowerbed)

    # Find the appearances of 1's in the list
    for flower in flower_copy:
        if flower == 1:
            count += 1

    # Deal with the instance where 1 element exists
    if last == 1 and flowerbed[0] == 0:
        flowerbed[0] = 1

    # Deal with the instance where len > 1 and it involves the first element
    if last > 1 and flowerbed[0] == 0  and flowerbed[1] == 0:
        flowerbed[0] = 1

    # Deal with the elements between i > 0 and i <= length - 1
    for i in range(1, last - 1):
        if flowerbed[i] == 0:
            if flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                flowerbed[i] = 1

    # Deal with the case of the last element
    if last > 1 and flowerbed[last - 1] == 0 and flowerbed[last - 2] == 0:
        flowerbed[last - 1] = 1

    # Count the number of appearances of 1 in the modified list
    for flower in flowerbed:
        if flower == 1:
            new_count += 1

    # Find the number of extra flowers
    extra_flowers = new_count - count

    # Finally, check if n and extra flowers match
    if extra_flowers >= n:
        return True
    return False

# Test case 1
flowerbed = [1,0,0,0,1]
flowerbed_copy = copy.deepcopy(flowerbed)
n = 1
result = canPlaceFlowers(flowerbed, n)
print("Test case 1")
print("({}) extra flower(s) can be added to the flowerbed {}. This is {}.Final flowerbed is {}".format(n, flowerbed_copy, result, flowerbed))

# Test case 2
flowerbed = [0]
flowerbed_copy = copy.deepcopy(flowerbed)
n = 1
result = canPlaceFlowers(flowerbed, n)
print("Test case 2")
print("({}) extra flower(s) can be added to the flowerbed {}. This is {}.Final flowerbed is {}".format(n, flowerbed_copy, result, flowerbed))

# Test case 
flowerbed = [0,0,1,0,0]
flowerbed_copy = copy.deepcopy(flowerbed)
n = 2
result = canPlaceFlowers(flowerbed, n)
print("Test case 3")
print("({}) extra flowers can be added to the flowerbed {}. This is {}. Final flowerbed is {}".format(n, flowerbed_copy, result, flowerbed))

# Test case 4
flowerbed = [0,0,1,0,0]
flowerbed_copy = copy.deepcopy(flowerbed)
n = 1
result = canPlaceFlowers(flowerbed, n)
print("Test case 4")
print("({}) extra flowers can be added to the flowerbed {}. This is {}.Final flowerbed is {}".format(n, flowerbed_copy, result, flowerbed))
