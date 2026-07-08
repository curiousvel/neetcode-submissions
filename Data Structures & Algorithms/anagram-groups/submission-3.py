class Solution:
    """
    APPROACH: Character Frequency Hashing
    
    Mental Pattern:
    1. Anagrams have identical character counts. We need a unique "key" to group them.
    2. Instead of sorting each word (O(k log k)), count character frequencies (O(k)) to build a key.
    3. Use an array of size 26 (for 'a'-'z') to count occurrences of each letter.
    4. Convert this count array into a tuple so it can be used as a hash map key.
    5. Group the original strings into a hash map where key = char_count_tuple, value = list of words.
    
    Complexity:
    - Time: O(n * k) where n is the number of strings and k is the maximum length of a string.
    - Space: O(n * k) to store the groups in the hash map.
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