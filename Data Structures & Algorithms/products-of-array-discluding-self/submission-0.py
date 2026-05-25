class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # Initialize the output array with zeros
        output = [0] * n
        
        # Iterate over each element to calculate its target product
        for i in range(n):
            current_product = 1
            # Nested loop to multiply all elements except the one at index i
            for j in range(n):
                if i != j:
                    current_product *= nums[j]
            
            # Store the computed product in the output array
            output[i] = current_product
            
        return output