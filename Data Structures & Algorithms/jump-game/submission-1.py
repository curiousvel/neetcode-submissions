class Solution:
    """
    Problem: Jump Game (LeetCode 55) - Backwards Shifted Goal Approach

    High-Level Idea:
    1. Backwards Greedy approach: Start from the target index (last element) and work 
    backwards towards index 0.
    2. Track a shifting `goal` post (initialized to `len(nums) - 1`).
    3. At each index `i` (moving right-to-left), check if `i + nums[i] >= goal`. 
    If it is, index `i` can reach the current goal, so we shift `goal = i`.
    4. If the goal post successfully shifts all the way back to `0`, a valid path exists.

    Complexity:
    - Time: O(N) — Single backward pass through the array.
    - Space: O(1) — Uses constant extra space.
    """

    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1
        
        # Iterate backwards from second-to-last element down to index 0
        for i in range(len(nums) - 2, -1, -1):
            # If current index can reach or cross the goal post, shift goal left
            if i + nums[i] >= goal:
                goal = i
                
        # If the goal post made it all the way back to start, we can jump to the end
        return goal == 0