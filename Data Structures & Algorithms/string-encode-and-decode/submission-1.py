class Solution:
    """
    APPROACH: Length-Prefixed Chunk Encoding (Delimiter Chunking)
    
    Mental Pattern:
    1. To serialize a list of strings safely, we must handle strings containing any arbitrary 
       characters (including spaces, punctuation, or our own delimiters like '#').
    2. ENCODE: For each string, we calculate its length and prepend it to the string along 
       with a structural delimiter (e.g., "hello" -> "5#hello"). This guarantees we always 
       know exactly how many characters to read next.
    3. DECODE: We use a pointer 'i' to traverse the encoded string. We search for the next 
       '#' delimiter using a second pointer 'j'. 
    4. The slice s[i:j] is mathematically parsed into an integer representing the exact character 
       payload length. We read that exact block slice, append it to our results, and jump 'i' 
       directly to the start of the next encoded block, cleanly bypassing any internal '#' characters.
    
    Complexity:
    - Time: O(n) for both encode and decode, where n is the total number of characters across all strings.
    - Space: O(1) auxiliary space for processing (excluding the memory required to output the results).
    """

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
            
            # Move your pointer 'i' to the beginning of the next encoded block
            i = end_of_str

        return result