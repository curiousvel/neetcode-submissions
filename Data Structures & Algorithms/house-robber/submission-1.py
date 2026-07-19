class Solution:
    """
    Problem: House Robber (LeetCode 198)
    
    ============================================================================
    ALGORITHM: Two-State Space-Optimized Dynamic Programming 💰
    ============================================================================
    For any house (i), we have two structural choices to maximize profit:
    1. Rob the current house: total = nums[i] + profit from 2 houses ago (prev)
    2. Skip the current house: total = profit from 1 house ago (curr)
    
    Therefore: max_profit_at(i) = max(nums[i] + prev, curr)
    
    We evaluate this step-by-step. Instead of maintaining an array, we track 
    the choices using just two variables ('prev' and 'curr') and shift them 
    forward simultaneously at each iteration.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> We traverse the list of houses exactly once.
    - Space Complexity: O(1) -> We only maintain two tracking variables.
    ============================================================================
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        # BASE CASES:
        # If there is only 1 house, you must rob it to maximize profit.
        if n == 1:
            return nums[0]
        # If there are only 2 houses, rob the one with the higher value.
        if n == 2:
            return max(nums[0], nums[1])

        # TRACKING STATE:
        # prev represents the maximum cash accumulated 2 houses ago.
        # curr represents the maximum cash accumulated 1 house ago.
        prev = nums[0]
        curr = max(nums[0], nums[1])

        # SCAN PHASE:
        # Iterate through the remaining houses starting from the third house (index 2)
        for i in range(2, n):
            # Evaluate the binary decision for house i, then shift values forward:
            # - new_prev becomes the old_curr
            # - new_curr becomes the max choice at house i
            prev, curr = curr, max(nums[i] + prev, curr)
        
        return curr  # Return the maximum cash accumulated after evaluating all houses