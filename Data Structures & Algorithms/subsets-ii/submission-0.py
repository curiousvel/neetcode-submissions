from typing import List

class Solution:
    """
    APPROACH: Backtracking with Duplicate-Skip Pruning

    MENTAL MODEL:
    Sort 'nums' first so duplicate values are adjacent. On any single tree level, 
    if a sibling branch picks an identical value (`nums[i] == nums[i-1]`), skip 
    it to avoid generating identical subset branches.

    VISUAL WORKFLOW (nums = [1, 2, 2]):
                            []
                  /         |         \
              [1]          [2]        [2]  <-- SKIP! Duplicate sibling at same level
             /   \          |
        [1, 2]  [1, 2]     [2, 2]
                  ^
                SKIP!

    COMPLEXITY:
    - Time:  O(N * 2^N) -> Worst-case power set traversal, O(N log N) sort overhead.
    - Space: O(N) auxiliary -> Stack depth is at most N.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Critical step: put duplicate values together
        res, sol = [], []

        def backtrack(start: int):
            res.append(sol.copy())

            for i in range(start, len(nums)):
                # Pruning Rule: Skip identical elements at the SAME tree level
                if i > start and nums[i] == nums[i - 1]:
                    continue

                sol.append(nums[i])      # Choose
                backtrack(i + 1)         # Explore forward
                sol.pop()                # Unchoose

        backtrack(0)
        return res