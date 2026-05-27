class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Handle the edge case of an empty array immediately
        if not nums:
            return 0
            
        # Convert list to a hash set for O(1) lookups and to remove duplicates
        num_set = set(nums)
        longest_streak = 0
        
        # Iterate through the unique numbers in the set
        for num in num_set:
            # Check if this number is the START of a sequence
            # If (num - 1) is in the set, it's not the start, so we skip it
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                # Build the sequence from this starting number
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                    
                # Update the longest streak found so far
                longest_streak = max(longest_streak, current_streak)
                
        return longest_streak