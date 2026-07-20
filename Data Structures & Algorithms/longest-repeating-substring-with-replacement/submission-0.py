from collections import defaultdict

class Solution:
    """
    Problem: Longest Repeating Character Replacement (LeetCode 424)
    
    ============================================================================
    KEY INTUITION: Variable-Size Sliding Window
    ============================================================================
    A window [left, right] is VALID if the number of characters we need to replace 
    is less than or equal to k:
    
        Replacements Needed = Window Length - Frequency of Most Frequent Character
        Formula: (right - left + 1) - max_freq <= k
        
    If (right - left + 1) - max_freq > k, we have too many "minority" characters 
    to replace with our budget 'k', so we must shrink the window from the left.
    
    ============================================================================
    OPTIMIZATION SECRET: Stale `max_freq`
    ============================================================================
    We do NOT need to decrement `max_freq` when shrinking from the left. 
    The window can only set a NEW record max length if `max_freq` grows LARGER 
    than its historical peak. Stale `max_freq` values won't break correctness!
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> Each pointer (left & right) moves at most N times.
    - Space Complexity: O(1) -> Frequency map stores at most 26 uppercase letters.
    ============================================================================
    """
    def characterReplacement(self, s: str, k: int) -> int:
        count = collections.defaultdict(int)
        max_length = 0
        max_freq = 0
        left = 0
        
        # Expand the window using the right pointer
        for right in range(len(s)):
            # 1. Add current character to frequency map
            count[s[right]] += 1
            
            # 2. Track max_freq: highest frequency of ANY single character in current window
            max_freq = max(max_freq, count[s[right]])
            
            # 3. Check validity using: Replacements Needed = Window Length - max_freq
            #    If replacements needed > k, budget is exceeded -> shrink from left.
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                # Note: max_freq is deliberately NOT decremented here!
            
            # 4. Record maximum valid window length seen so far
            max_length = max(max_length, right - left + 1)
            
        return max_length