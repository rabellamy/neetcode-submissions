class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string.
        Format: <length_of_string>:<string_characters>
        """
        res = []
        for s in strs:
            # Prepend the length of the string and a colon delimiter
            res.append(f"{len(s)}:{s}")
            
        # Join into a single continuous string
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of strings using length prefixes.
        """
        decoded_strs = []
        i = 0  # Pointer to our current position in the encoded string
        
        while i < len(s):
            # Find the next colon which acts as the separator for the length
            colon_idx = s.find(':', i)
            
            # Extract the length of the upcoming string
            length = int(s[i:colon_idx])
            
            # Determine the start and end indices of the actual string
            start_idx = colon_idx + 1
            end_idx = start_idx + length
            
            # Extract the string using slicing and add to results
            decoded_strs.append(s[start_idx:end_idx])
            
            # Move the pointer to the start of the next length prefix
            i = end_idx
            
        return decoded_strs