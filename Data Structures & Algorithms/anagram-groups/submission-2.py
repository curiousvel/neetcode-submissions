class Solution:
    """
    APPROACH: Character Frequency Signature Matching (Bucket Sort Style)
    
    Mental Pattern:
    1. Anagrams have identical character distributions regardless of letter order.
    2. Instead of sorting each word (O(n log n)), we generate a standardized 
       26-element frequency signature array (O(n)) representing count of a-z.
    3. We convert this mutable array into an immutable tuple to use as a unique 
       hash map key.
    4. Strings with matching signatures automatically group into the same bucket.
    
    Complexity:
    - Time: O(m * n) where m is number of strings, n is average string length.
    - Space: O(m * n) to store grouped results in the hash map.
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Map character frequency patterns to lists of matching anagram strings.
        # Key: tuple of 26 integers (character counts) -> Value: List of strings
        # We use defaultdict(list) to automatically initialize empty lists for new keys.
        anagram_groups = defaultdict(list)

        for current_string in strs:
            # Create a frequency bucket for the 26 lowercase English letters (a-z).
            # Indices: 0 corresponds to 'a', 1 to 'b', ..., 25 to 'z'.
            char_counts = [0] * 26 
            
            for char in current_string:
                # Map the character to an index between 0 and 25 using its ASCII value.
                # Example: ord('c') - ord('a') -> 99 - 97 = index 2.
                char_counts[ord(char) - ord('a')] += 1

            # Convert the list to a tuple because lists are mutable and cannot be keys in a dict.
            # Tuples are immutable and hashable, making them valid dictionary keys.
            pattern_key = tuple(char_counts)
            
            # Append the original string to its matching frequency pattern bucket.
            anagram_groups[pattern_key].append(current_string)

        # Return all the grouped anagram lists.
        return list(anagram_groups.values())