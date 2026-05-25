class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Initialize the output array with 1s. 
        # This will eventually hold our final results.
        output = [1] * n
        
        # Step 1: Calculate left prefix products.
        # left_product keeps track of the product of all elements to the left of index i.
        left_product = 1
        for i in range(n):
            # Store the product of all elements to the left of i
            output[i] = left_product
            # Update the running left_product to include the current element
            left_product *= nums[i]
            
        # Step 2: Calculate right suffix products and multiply with left products.
        # right_product keeps track of the product of all elements to the right of index i.
        right_product = 1
        # Iterate backwards from the end of the array to the beginning
        for i in range(n - 1, -1, -1):
            # Multiply the existing left product in output[i] by the right_product
            output[i] *= right_product
            # Update the running right_product to include the current element
            right_product *= nums[i]
            
        return output