class Solution:
    """
    Problem: Palindromic Substrings (LeetCode 647)
    
    ============================================================================
    ALGORITHM: Two-Pointer Center Expansion Counter 🧭
    ============================================================================
    Every character and every space between two characters represents a potential
    center of a palindrome. As we expand outward, every single match we find represents
    a distinct, valid palindromic substring.
    
    Instead of calculating a substring slice math window, we just maintain a 
    running count. Every time `s[left] == s[right]`, it means we've uncovered 
    another valid palindrome, so we add 1 to our count.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N^2) -> We scan N indices. Each index tests 2 centers (odd/even).
      An expansion can take up to O(N) steps in the worst case.
      
    - Space Complexity: O(1) -> Only integer pointer references are stored in memory.
    ============================================================================
    """
    def countSubstrings(self, s: str) -> int:
        # Guard Clause: An empty string contains zero palindromic substrings
        if not s:
            return 0
            
        total_palindromes = 0
        
        def expand_and_count(left: int, right: int) -> int:
            count = 0
            # Expand outward from the given center configuration
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # Every step that matches is a unique palindromic substring!
                left -= 1   # Move left pointer outward
                right += 1  # Move right pointer outward
            return count

        # GLOBAL SCANNER: Iterate through the string treating each position as a center
        for i in range(len(s)):
            # Scenario A: Count odd-length palindromes (e.g., "a", "aba", "abcba")
            total_palindromes += expand_and_count(i, i)
            
            # Scenario B: Count even-length palindromes (e.g., "aa", "abba", "abccba")
            total_palindromes += expand_and_count(i, i + 1)
            
        return total_palindromes
        if not s:
            return 0

        total_polindrome = 0

        def expand_from_center(left, right) -> int:
            count = 0

            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1

            return count

        for i in range(len(s)):
                total_polindrome += expand_from_center(i, i)
                total_polindrome += expand_from_center(i, i+1)

        return total_polindrome