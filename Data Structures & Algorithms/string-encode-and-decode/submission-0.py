class Solution:

    def encode(self, strs: List[str]) -> str:
        result = []

        for s in strs:
            result.append(f"{len(s)}#{s}")

        return "".join(result) 

    def decode(self, s: str) -> List[str]:

        result = []
        i = 0

        while i < len(s):
            # Find where the '#' is starting from the current index 'i'
            j = i
            while s[j] != '#':
                j += 1
            
            # Everything between i and j is the length of the string
            length = int(s[i:j])
            
            # The actual string starts right after '#' (j + 1) 
            # and goes up to (j + 1 + length)
            start_of_str = j + 1
            end_of_str = start_of_str + length
            
            result.append(s[start_of_str:end_of_str])
            
            # Move your pointer 'i' to the beginning of the next
            # encoded block
            i = end_of_str

        return result