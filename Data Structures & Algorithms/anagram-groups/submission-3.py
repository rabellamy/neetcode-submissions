class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        n = len(strs)
        # Array to keep track of which strings have already been placed in a group
        visited = [False] * n
        result = []
        
        # Iterate through every string in the array
        for i in range(n):
            # If the current string has already been grouped, skip it
            if visited[i]:
                continue
            
            # Start a new group with the current ungrouped string
            current_group = [strs[i]]
            visited[i] = True
            
            # Compare the current string with all remaining strings
            for j in range(i + 1, n):
                if not visited[j]:
                    # Check if they are anagrams by sorting both strings
                    if sorted(strs[i]) == sorted(strs[j]):
                        current_group.append(strs[j])
                        visited[j] = True # Mark as grouped so we don't process it again
                        
            # Add the completed group to our final result
            result.append(current_group)
            
        return result