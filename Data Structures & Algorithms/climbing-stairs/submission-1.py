class Solution:
    """
    Problem: Climbing Stairs (LeetCode 70)
    
    ============================================================================
    ALGORITHM: The Fibonacci Sequence Pattern 🧗‍♂️
    ============================================================================
    To reach the top step (n), you can only arrive from one of two places:
    1. By taking a 1-step jump from the step right below it (n - 1)
    2. By taking a 2-step jump from two steps below it (n - 2)
    
    Therefore: total_ways(n) = total_ways(n - 1) + total_ways(n - 2)
    
    This matches the exact definition of the Fibonacci sequence. Instead of 
    allocating an entire array, we optimize space by only keeping track of the 
    last two calculated values ('prev' and 'cur') and shifting them forward.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> We run a single loop from 2 up to n.
    - Space Complexity: O(1) -> We only use two variables to track the states.
    ============================================================================
    """
    def climbStairs(self, n: int) -> int:
        # BASE CASES: 
        if n <= 0:
            return 0

        # 1 step has exactly 1 way (1)
        if n == 1:
            return 1
        # 2 steps have exactly 2 ways (1+1, or 2)
        if n == 2:
            return 2

        # TRACKING STATE:
        # prev represents ways to reach (n-2) -> initialized to step 1
        # cur represents ways to reach (n-1)  -> initialized to step 2
        prev = 1
        cur = 2

        # SCAN PHASE:
        # Calculate the choices step-by-step up to n.
        # Python's simultaneous assignment let's us shift our trackers forward safely.
        for i in range(2, n):
            # new_current = cur + prev
            # new_previous = old_current
            prev, cur = cur, cur + prev

        return cur  # Return the final accumulated ways to reach step n