class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_length = 0
        
        # Iterate through every number in the array
        for num in nums:
            current_num = num
            current_length = 1
            
            # Continuously search the array for the next consecutive number
            while current_num + 1 in nums:
                current_num += 1
                current_length += 1
                
            # Update the maximum length found so far
            max_length = max(max_length, current_length)
            
        return max_length