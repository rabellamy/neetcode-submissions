class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # If the lengths are different, they cannot be anagrams
        if len(s) != len(t):
            return False
            
        # Sort both strings and compare them for exact equality
        # Python's sorted() function returns a list of characters,
        # which can be directly compared
        return sorted(s) == sorted(t)