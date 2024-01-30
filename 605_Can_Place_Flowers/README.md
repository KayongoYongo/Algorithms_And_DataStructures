# 605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array `flowerbed` containing `0's` and `1's`, where 0 means empty and 1 means not empty, and an integer `n`, return `true` if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and `false` otherwise.

# Thoughts on the problem
The problem is classified as easy. At the time of writing, it has an acceptance rate of 29.5%. After many trials and errors, I
finally understood why it has such a low acceptance rate. The major things to consider are the edge cases.

# Things to consider
1. Since the problem involves finding the appearance of `1's` in the list, I need to have a counter that finds the number
of `1's` before and after 1 has been added to the list `flowerbed`.
2. Since we  are considering `i + 1` and `i - 1`, another problem comes up. I need to consider the element at `[0]`, the element at
`[length(flowerbed)] - 1` and the elements between  `i > 0 and length(flowerbed) - 1`.
3. From point 2, it comes under the assumption that the list has a length > 1. What if the list has length of 1 ? This will be
another test case considered in solving the problem.
4. Finally, after finding the number of flowers that can be added to the list, I need to read the question carefully.
The question returns true if `n` new flowers can be planted in the garden. So, if the variable `extra_flowers` returns
`true`, it not only works if `n == extra_flowers`, it also returns true if `extra_flowers > n`. The latter would be true
if the question asked n flowers **ONLY**.

# The solution
1. In order to find the number of extra flowers that can be added, we need to find the number of `1's` before and after they have
been added to the list. My solution for theis was creating a deep copy of the `flowerbed` list. My reason for this is that a deep copy
of the list does not have any relation to the `flowerbed` list. Any changes made to the `flowerbed` won't affect the deep copy.
2. Deal with the three edge cases separately. In terms of order, start with the case involving the first element. Otherwise, the output
will show irregular behavior.
3. Finally, confirm if the `extra_flower` >= `n` and then return a boolean value.
