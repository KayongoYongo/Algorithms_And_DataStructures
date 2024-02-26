#!/usr/bin/python3

from typing import List

def kidsWithCandies(candies: List[int], extraCandies: int) -> List[bool]:
    """
    This function returns a boolean list which tries to identify which
    sstudent has the highest number of candies. If it is the highest,
    return True. Otherwise, return False.

    Args:
        candies: A list showing the current number of candies a stuudent
        has
        extracandies: The current number of extra candies a student has.

    Return:
        List: A list containing bollean values
    """

    max_candies = max(candies)
    highest_candies = []

    for i in range(len(candies)):
        if (candies[i] + extraCandies >= max_candies):
            highest_candies.append(True)
        else:
            highest_candies.append(False)

    return highest_candies

print("Example 1")
candies = [2,3,5,1,3]
extraCandies = 3
print("The candies are {}. The extra candies are {}. The result is {}".format(candies, extraCandies, kidsWithCandies(candies,extraCandies)))
print("Example 2")
candies = [4,2,1,1,2]
extraCandies = 1
print("The candies are {}. The extra candies are {}. The result is {}".format(candies, extraCandies, kidsWithCandies(candies,extraCandies)))
print("Example 3")
candies = [12,1,12] 
extraCandies = 10
print("The candies are {}. The extra candies are {}. The result is {}".format(candies, extraCandies, kidsWithCandies(candies,extraCandies)))
