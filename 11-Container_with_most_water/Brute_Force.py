from typing import List

def maxArea(height: List[int]) -> int:
    # BRUTE FORCE
    res = 0

    for l in range(len(height)):
        for r in range(l + 1, len(height)):
            area = (r - l) * min(height[l], height[r])
            res = max(res, area)

    return res

height = [1,8,6,2,5,4,8,3,7]
print(f"The maximum area of {height} is {maxArea(height)}")