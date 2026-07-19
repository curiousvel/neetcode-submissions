class Solution:
    """
    Problem: Longest Palindromic Substring (LeetCode 5)
    
    ============================================================================
    ALGORITHM: Two-Pointer Expansion Around Center 🧭
    ============================================================================
    A palindrome reads the same backward as forward. Every palindrome has a core center.
    If we choose a center point and expand outward with two pointers (left and right),
    as long as the characters match, we have a valid palindrome.
    
    We must test two scenarios for every single index i:
    1. Odd-Length Palindromes:  The center is a single character (left = i, right = i).
       Example: "aba" -> center is 'b'.
    2. Even-Length Palindromes: The center is between two characters (left = i, right = i + 1).
       Example: "abba" -> center is between 'b' and 'b'.
       
    By iterating through the string and trying both expansions at each index,
    we track and extract the longest substring found.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N^2) -> Where N is the length of the string. We look at N 
      possible center positions, and expanding out from each takes up to O(N) time.
      
    - Space Complexity: O(1) -> We only track indices (left, right, start, max_len).
      We do not allocate a 2D matrix, saving massive memory.
    ============================================================================
    """
    def longestPalindrome(self, s: str) -> str:
        # Guard Clause: An empty string or single character is already its own longest palindrome
        if not s or len(s) < 2:
            return s
            
        start = 0
        max_len = 0
        
        def expand_from_center(left: int, right: int) -> int:
            # Expand outward as long as we are inside boundaries AND characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1   # Push left boundary out
                right += 1  # Push right boundary out
                
            # The loop terminates when boundaries break or characters mismatch.
            # The length of the valid palindrome is: right - left - 1
            return right - left - 1

        # GLOBAL SCANNER: Iterate through every index to treat it as a potential center
        for i in range(len(s)):
            # Scenario A: Check for odd-length palindromes centered at index i
            len1 = expand_from_center(i, i)
            
            # Scenario B: Check for even-length palindromes centered between i and i + 1
            len2 = expand_from_center(i, i + 1)
            
            # Identify the longer result from our two structural scenarios
            current_longest = max(len1, len2)
            
            # If the palindrome found at this center beats our record, update bounds
            if current_longest > max_len:
                max_len = current_longest
                # Calculate the exact starting index of the substring in s
                # (current_longest - 1) // 2 correctly calculates the offset backward from i
                start = i - (current_longest - 1) // 2
                
        # Return the window slicing the longest palindromic substring
        return s[start : start + max_len]