class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        # dp[i] stores the number of valid ways to decode the substring s[i:]
        # Size is (n + 1) to accommodate the base case at index n
        dp = [0] * (n + 1)
        
        # Base case: An empty suffix s[n:] has 1 valid way to be decoded (doing nothing)
        dp[n] = 1

        # Iterate backward from the end of the string to the beginning
        for i in range(n - 1, -1, -1):
            # A leading '0' cannot be decoded on its own, so dp[i] remains 0
            if s[i] != '0':
                
                # Option 1: Decode a single digit using s[i]
                # The remaining suffix to decode is s[i+1:], so we add dp[i+1]
                dp[i] = dp[i] + dp[i+1]

                # Option 2: Decode two digits using s[i:i+2]
                # Check if a 2-digit number exists and falls in the valid character range [10, 26]
                if (i + 1) < n and 10 <= int(s[i: i+2]) <= 26:
                    # The remaining suffix to decode is s[i+2:], so we add dp[i+2]
                    dp[i] = dp[i] + dp[i+2]

        # Return total valid decodings starting from index 0
        return dp[0]