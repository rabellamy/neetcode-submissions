class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n
        
        left_product = 1
        right_product = 1
        
        # We only use ONE loop, but we still do N iterations
        for i in range(n):
            # 1. Handle the left side (moving left to right)
            output[i] *= left_product
            left_product *= nums[i]
            
            # 2. Handle the right side (moving right to left)
            # j is the mirrored index on the opposite side of the array
            j = n - 1 - i 
            output[j] *= right_product
            right_product *= nums[j]
            
        return output