from typing import List

def maxArea(self, height: List[int]) -> int:
    # optimal solution
    res = 0
    l, r =  0, len(height) - 1

    while l < r:
        # find the area of the container
        area = (r - l) * min(height[l], height[r])
        res = max(res, area)

        if height[l] < height[r]:
            l += 1
        else:
            r-= 1

    return res