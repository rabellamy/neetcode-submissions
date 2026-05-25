class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict allows us to append to a list even if the key doesn't exist yet
        anagram_map = defaultdict(list)
        
        for s in strs:
            # Initialize a frequency array of 26 zeros for 'a' through 'z'
            char_counts = [0] * 26
            
            # Populate the frequency array for the current string
            for char in s:
                # ord(char) - ord('a') gives us an index from 0 to 25
                index = ord(char) - ord('a')
                char_counts[index] += 1
            
            # Tuples are immutable and hashable, making them valid dictionary keys
            # We map this frequency tuple to the original string
            anagram_map[tuple(char_counts)].append(s)
            
        # The values of the dictionary are the grouped anagram lists
        return list(anagram_map.values())
        