class Solution:
    """
    Problem: Maximum Subarray (LeetCode 53)

    High-Level Idea:
    1. Dynamic Programming / Greedy approach (Kadane's Algorithm).
    2. At each position `i`, decide whether to extend the existing contiguous subarray 
    (`current_sum + num`) or discard the past sum and start a fresh subarray (`num`).
    3. Maintain a `max_sum` variable to track the global maximum seen across all steps.

    Complexity:
    - Time: O(N) — Single pass through the array.
    - Space: O(1) — Uses constant extra space instead of an explicit DP array.
    """

    def maxSubArray(self, nums: list[int]) -> int:
        # Initialize both with the first element to safely handle all-negative arrays
        max_sum = nums[0]
        current_sum = nums[0]
        
        for num in nums[1:]:
            # Core DP choice: Start fresh at `num` OR extend previous `current_sum`
            current_sum = max(num, current_sum + num)
            
            # Update global maximum
            max_sum = max(max_sum, current_sum)
            
        return max_sum