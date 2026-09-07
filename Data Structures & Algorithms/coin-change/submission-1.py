class Solution:
   def coinChange(self, coins: List[int], amount: int) -> int:
       # dp[x] = minimum number of coins needed to make amount x
       dp = [float("inf")] * (amount + 1)

       # Base case:
       # It takes 0 coins to make the amount 0.
       dp[0] = 0

       for x in range(1, amount + 1):

           # Try each coin as the next decision.
           for coin in coins:

               if coin <= x:
                   # Choose this coin.
                   # The remaining amount is x - coin.
                   #
                   # We already know the best way to make
                   # the remaining amount: dp[x - coin].
                   dp[x] = min(
                       dp[x],
                       1 + dp[x - coin]
                   )

       return dp[amount] if dp[amount] != float("inf") else -1