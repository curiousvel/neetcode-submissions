class Solution:
    """
    🧠 MENTAL MODEL: The Halving & Odd-Check Shift (DP + Bit Manipulation)
    
    Instead of counting bits from scratch for every number, look at what happens 
    when you shift a binary number to the right by 1 bit (which is integer division by 2).
    
    Example with 6 and 7:
    - 6 in binary is 110. Right shift it (6 >> 1): it becomes 3 (11).
      The number of 1s in 6 is EXACTLY the same as in 3, because the dropped bit was 0.
    - 7 in binary is 111. Right shift it (7 >> 1): it becomes 3 (11).
      The number of 1s in 7 is the same as in 3, PLUS 1, because the dropped bit was 1.
      
    State Transition Equation:
    dp[i] = dp[i >> 1] + (i & 1)
    Where:
    - dp[i >> 1] grabs the precomputed bit count of the halved number.
    - (i & 1) acts as a sneaky +1 if the current number is odd.
    
    Complexity:
        - Time: O(N) -> We calculate the bit count for each number exactly once in a linear loop.
        - Space: O(1) -> If excluding the output array, it uses constant extra space.
    """
    def countBits(self, n: int) -> List[int]:
        # Initialize a dynamic programming array (dp) with size n + 1.
        # dp[i] will store the number of set bits for the integer i.
        dp = [0] * (n + 1)

        # Iterate from 1 up to n to calculate the set bits for each number.
        for i in range(1, n + 1):
            # The number of set bits for 'i' can be derived from a previous number.
            # This formula combines two cases:
            # 1. If 'i' is even: dp[i] = dp[i // 2]
            #    (i >> 1) is equivalent to i // 2. (i & 1) is 0 for even numbers.
            # 2. If 'i' is odd: dp[i] = dp[i // 2] + 1
            #    (i >> 1) is equivalent to i // 2. (i & 1) is 1 for odd numbers.
            # This leverages the fact that i has the same set bits as i // 2, plus an additional bit if i is odd.
            dp[i] = dp[i >> 1] + (i & 1)
        
        # Return the dp array containing the count of set bits for each number from 0 to n.
        return dp