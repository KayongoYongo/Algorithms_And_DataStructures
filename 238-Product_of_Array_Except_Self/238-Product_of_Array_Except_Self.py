from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
    n = len(nums)
    prefix = [1] * n
    postfix = [1] * n
    result = [0] * n

    product_pre = 1
    for i in range(n):
        prefix[i] = product_pre
        product_pre *= nums[i]

    product_post = 1
    for i in range(n-1, -1, -1):
        postfix[i] = product_post
        product_post *= nums[i]

    for i in range(n):
        result[i] = prefix[i] * postfix[i]

    return result

nums =[1,2,3,4]
print(f"The porduct of the array {nums} except the self is {productExceptSelf(nums)}")