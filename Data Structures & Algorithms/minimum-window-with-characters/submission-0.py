from collections import Counter

class Solution:
    """
    APPROACH: Sliding Window with Dynamic Match Counter

    MENTAL MODEL:
    Expand the right boundary to satisfy requirements; shrink the left 
    boundary to optimize the window size. Track matched unique characters 
    using a 'formed' counter to avoid expensive hash map comparisons in O(1).

    VISUAL WORKFLOW:
    s = "ADOBECODEBANC", t = "ABC"
    
    1. Expand Right until window contains all required chars (A, B, C):
       [A D O B E C] O D E B A N C   -> Valid window length 6 ("ADOBEC")
    
    2. Shrink Left to find smallest valid window:
       A [D O B E C] O D E B A N C   -> Left moves past 'A', becomes invalid.
    
    3. Repeat until end of string:
       A D O B E C O D E [B A N C]   -> Shrinks down to "BANC" (length 4).

    COMPLEXITY:
    - Time:  O(N + M) -> Where N = len(s) and M = len(t). Each character in 's' 
             is visited at most twice (once by right, once by left).
    - Space: O(M) -> Space for target map 't_count' and window map 'window_count'. 
             O(1) auxiliary if alphabet size is fixed (e.g., ASCII).
    """
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ""

        # Step 1: Build target frequency map
        t_count = Counter(t)
        required = len(t_count)  # Number of UNIQUE chars in t that must be satisfied

        # Sliding Window trackers
        window_count = {}
        formed = 0  # Number of unique chars satisfying t's frequency requirement

        # Window result trackers: (window_length, left, right)
        ans = (float("inf"), None, None)
        left = 0

        # Step 2: Expand the right pointer to find a valid window
        for right, char in enumerate(s):
            window_count[char] = window_count.get(char, 0) + 1

            # If current char's frequency matches target frequency, increment formed count
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1

            # Step 3: Shrink left pointer once window is valid to find minimum size
            while left <= right and formed == required:
                current_len = right - left + 1

                # Update best window found so far
                if current_len < ans[0]:
                    ans = (current_len, left, right)

                # Character leaving the window
                left_char = s[left]
                window_count[left_char] -= 1

                # If left_char was required and its count fell below target, decrement formed
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1

                left += 1  # Move left pointer inward

        # Return minimum substring if found, else empty string
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]