class Solution:
    """
    Problem: House Robber II
    
    ============================================================================
    ALGORITHM: Circular Decomposition via Linear Sub-Problems 🔄
    ============================================================================
    Because the houses form a circle, the first and last houses are adjacent. 
    Therefore, robbing both is strictly forbidden. We break this circular dependency 
    into two standard, linear House Robber I configurations:
    
    1. Slice 1: Include first house, exclude last house -> nums[0 : n-1]
    2. Slice 2: Exclude first house, include last house -> nums[1 : n]
    
    We pass both linear arrays into our space-optimized O(1) tracker, and the 
    global maximum will simply be the greater result of the two slices.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(N) -> We scan two separate linear slices of the array.
    - Space Complexity: O(1) -> The linear helper uses constant space variables.
    ============================================================================
    """
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        # BASE CASES:
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
            
        # SPLIT AND SCAN:
        # Run the standard linear robber logic on both mutually exclusive slices.
        # Max out by choosing either the scenario without the last house, or without the first.
        return max(self.linear_rob(nums[:-1]), self.linear_rob(nums[1:]))

    def linear_rob(self, sub_nums: List[int]) -> int:
        """Standard House Robber I logic operating in O(1) space."""
        length = len(sub_nums)
        
        if length == 1:
            return sub_nums[0]
            
        # STATE TRACKERS
        prev = sub_nums[0]
        curr = max(sub_nums[0], sub_nums[1])

        # LINEAR SCAN LOOP
        # range(2, 2) is completely empty! The loop block never executes.
        for i in range(2, length):
            prev, curr = curr, max(sub_nums[i] + prev, curr)
            
        return curr