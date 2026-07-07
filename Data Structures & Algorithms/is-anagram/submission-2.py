class Solution:
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