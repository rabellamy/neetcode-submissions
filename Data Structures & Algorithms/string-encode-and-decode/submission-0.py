class Solution:

    def encode(self, strs: List[str]) -> str:
        """
        Encodes a list of strings to a single string using delimiter escaping.
        We escape '#' by turning it into '##', and use '#|' as the end-of-string marker.
        """
        res = []
        for s in strs:
            # Escape the escape character
            escaped_str = s.replace('#', '##')
            # Append string with the unique end marker
            res.append(escaped_str + '#|')
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        """
        Decodes a single string back to a list of strings.
        """
        decoded_strs = []
        current_str = []
        i = 0
        
        while i < len(s):
            if s[i] == '#':
                # Check the next character to determine action
                if i + 1 < len(s) and s[i + 1] == '#':
                    # It's an escaped '#', append one '#' and skip the next
                    current_str.append('#')
                    i += 2
                elif i + 1 < len(s) and s[i + 1] == '|':
                    # It's the end of the current string
                    decoded_strs.append("".join(current_str))
                    current_str = []
                    i += 2
            else:
                # Regular character
                current_str.append(s[i])
                i += 1
                
        return decoded_strs
