from typing import List

def maxPairWiseProduct(nums: List[int]) -> int:
        n = len(nums)
        product = 0
        i, j = 0,0
        for i in range(i, n):
            for j in range(i+1, n):
                product = max(product, nums[i] * nums[j])
        return product

def maxPairWiseProductFast(nums: List[int]) -> int:
    max1 = max2 = float('-inf')
    for num in nums:
        if num > max1:
            max2 = max1
            max1 = num
        elif num > max2:
            max2 = num
    print(f"maxwise pair product is as below")
    return max1 * max2
    
