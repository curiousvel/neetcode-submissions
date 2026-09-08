class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # 1. DEFINE & INITIALIZE STATE
        # dp[i][j] stores LCS length for text1[0...i-1] and text2[0...j-1]
        # Extra row/col padded with 0 handles the base case of empty strings
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # 2. DUAL LOOPS (Traverse both string prefixes)
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                
                # 3. TRANSITION LOGIC
                if text1[i - 1] == text2[j - 1]:
                    # Match found: diagonal lookback + 1
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # No match: take best result from skipping character in text1 OR text2
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # 4. EXTRACT GLOBAL ANSWER
        return dp[m][n]