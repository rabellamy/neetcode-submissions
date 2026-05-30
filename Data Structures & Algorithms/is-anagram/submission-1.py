class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Edge Case: Different lengths cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Initialize an array of 26 zeros to represent the alphabet frequencies
        char_counts = [0] * 26
        
        # Iterate through both strings simultaneously
        for i in range(len(s)):
            # ord() gets the ASCII value. Subtracting ord('a') maps 'a'-'z' to indices 0-25
            # Increment for characters in 's'
            char_counts[ord(s[i]) - ord('a')] += 1
            # Decrement for characters in 't'
            char_counts[ord(t[i]) - ord('a')] -= 1
            
        # If they are anagrams, all counts will have balanced back to 0
        for count in char_counts:
            if count != 0:
                return False
                
        return True