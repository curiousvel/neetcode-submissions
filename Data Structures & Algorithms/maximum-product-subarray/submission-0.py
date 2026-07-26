class Solution:
    """
    PATTERN: 1D Dynamic Programming (Space-Optimized / Kadane's Variant)
    PROBLEM: Maximum Product Subarray (LeetCode 152)
    
    ===========================================================================
    💡 MENTAL MODEL:
    Subarrays are contiguous (non-overlapping chunks). Because multiplying 
    two negative numbers yields a positive, a single negative number can flip 
    the smallest negative product into the largest positive product.
    
    At index i, we maintain BOTH:
      1. curr_max: The max contiguous product ending at i
      2. curr_min: The min contiguous product ending at i
    ===========================================================================
    
    COMPLEXITY:
    - Time:  O(N) -> Single pass through array
    - Space: O(1) -> Tracks only scalar max/min state
    """
    def maxProduct(self, nums: list[int]) -> int:
        if not nums:
            return 0

        # Global answer res, curr_max and curr_min starts at the first element
        res = curr_max = curr_min = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            # If num is negative, multiplying flips max and min.
            # You can swap them explicitly or compute both using temp variables.
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            # Decisions at index i:
            # 1. Start a new subarray at `num`
            # 2. Extend the existing product
            curr_max = max(num, num * curr_max)
            curr_min = min(num, num * curr_min)

            # Update overall max
            res = max(res, curr_max)

        return res