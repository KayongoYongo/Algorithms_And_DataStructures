from typing import List

def countBits(n: int) -> List[int]:
    """
    Description:
        The function is supposed to return the number of occurences
        of 1 in a raange of numbers after it has been converted to 
        binary. For example: 
        Input: n = 5
        Output: [0,1,1,2,1,2]

    Args:
        n: an integer which we will use to create the range

    Return:
        A list of numbers
    """
    # Using list comprehension, create a binary array
    binary_list = [bin(i)[2:] for i in range(n + 1)]

    result = []

    for s in binary_list:
        result.append(s.count('1'))

    print(binary_list)

    return result

n = 5
print(countBits(n))