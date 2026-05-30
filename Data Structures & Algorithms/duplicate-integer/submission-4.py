class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool: # [cite: 60, 61]
        # Initialize an empty set to keep track of the numbers we've seen
        seen = set()
        
        for num in nums:
            # If the number is already in our set, we found a duplicate
            if num in seen:
                return True
                
            # Otherwise, add the number to the set and continue
            seen.add(num)
            
        # If the loop completes, all elements are unique
        return False