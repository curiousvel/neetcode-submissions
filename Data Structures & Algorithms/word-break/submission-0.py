class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        # Step 1: O(1) lookups for dictionary words
        words = set(wordDict)
        n = len(s)

        # Step 2: dp[i] represents if s[0:i] can be formed using dictionary words
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string

        # Step 3: Expand the prefix boundary end from 1 to n
        for end in range(1, n + 1):
            
            # Step 4: Scan all possible prior starting positions
            for start in range(end):
                
                # Step 5: Skip if 'start' position was never reachable
                if not dp[start]:
                    continue

                # Extract substring from valid start to current end
                word = s[start:end]

                # If substring is a valid dictionary word, mark 'end' reachable
                if word in words:
                    dp[end] = True
                    break  # Found a valid path to 'end', move to next 'end'

        # Step 6: Return whether the full length n was reached
        return dp[n]