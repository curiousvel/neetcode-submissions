class Solution:
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