class Solution:
    """
    APPROACH: Dual Hash Map Frequency Comparison
    
    Mental Pattern:
    1. Anagram check requires verifying that two strings have identical character counts.
    2. If their lengths differ upfront, they cannot be anagrams (O(1) early exit).
    3. We traverse both strings in a single pass (O(n)), building a character-to-frequency 
       counter map for each string using hash maps.
    4. Finally, we iterate through the keys of the first map to ensure that every character 
       appears with the exact same frequency in the second map.
    
    Complexity:
    - Time: O(n) where n is the length of string s (and t).
    - Space: O(n) or O(1) if restricted to a fixed alphabet size (e.g., 26 English letters).
    """
    def isAnagram(self, s: str, t: str) -> bool:
        # If the strings have different lengths, they cannot be anagrams.
        if len(s) != len(t):
            return False
        
        # Initialize hash maps (dictionaries) to store the frequency of each character.
        char_count_s = {}
        char_count_t = {}

        # Build the frequency counts for both strings simultaneously.
        # Since lengths are identical, range(len(s)) covers all indices for both strings.
        for i in range(len(s)):
            # .get(character, 0) fetches the current count, defaulting to 0 if not found.
            char_count_s[s[i]] = 1 + char_count_s.get(s[i], 0)
            char_count_t[t[i]] = 1 + char_count_t.get(t[i], 0)

        # Compare the frequency maps.
        # Iterate through every unique character found in string s.
        for char in char_count_s:
            # Check if the character's frequency in 's' matches its frequency in 't'.
            # .get(char, 0) handles cases where 'char' does not exist in 't' at all.
            if char_count_s[char] != char_count_t.get(char, 0):
                return False  # Mismatched frequency means they are not anagrams.
                
        # If all character frequencies match perfectly, the strings are anagrams.
        return True