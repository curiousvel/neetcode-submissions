class Solution:
    def isPalindrome(self, s: str) -> bool:
        # MENTAL MODEL: Two-Pointer Technique.
        # We place one pointer at the start and one at the end, moving toward the center.
        # We skip any non-alphanumeric characters along the way and compare the valid characters.
        start = 0
        end = len(s) - 1

        while start < end:
            # Move the start pointer right until it hits a valid alphanumeric character
            while start < end and not self.isalphanum(s[start]):
                start += 1
                
            # Move the end pointer left until it hits a valid alphanumeric character
            while start < end and not self.isalphanum(s[end]):
                end -= 1
            
            # Case-insensitive comparison of the characters at both pointers
            if s[start].lower() != s[end].lower():
                return False  # Mismatch found, definitely not a palindrome
            
            # Move both pointers closer to the center for the next check
            start, end = start + 1, end - 1

        return True  # All valid pairs matched perfectly

    def isalphanum(self, c):
        """
        Helper function to check if a character is alphanumeric 
        using ASCII values (avoiding built-in methods like .isalnum()).
        """
        char = ord(c)
        return (
            (char >= ord('A') and char <= ord('Z')) or  # Uppercase A-Z
            (char >= ord('a') and char <= ord('z')) or  # Lowercase a-z
            (char >= ord('0') and char <= ord('9'))    # Digits 0-9
        )