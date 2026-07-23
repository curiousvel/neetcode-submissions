from typing import List

class Solution:
    """
    APPROACH: Unified For-Loop Backtracking with Reuse

    MENTAL MODEL:
    We loop through candidates starting from 'start' index to enforce forward ordering.
    To allow element REUSE, we recurse with 'i' (same index) instead of 'i + 1'.

    VISUAL WORKFLOW (candidates = [2, 3], target = 7):
                          [] (start=0, sum=0)
                   /                 \
               [2] (i=0, sum=2)     [3] (i=1, sum=3)
            /       \
        [2, 2]     [2, 3] 
       /      \
    [2,2,2]  [2,2,3] -> Target 7 hit! Record solution.

    COMPLEXITY:
    - Time:  O(N^(T/M)) -> Where T = target, M = min(candidates).
    - Space: O(T/M) auxiliary -> Call stack depth bounded by T / M.
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(start: int, current_sum: int):
            # Base Case 1: Target reached
            if current_sum == target:
                res.append(sol.copy())
                return
            
            # Base Case 2: Exceeded target (Prune dead-end path)
            if current_sum > target:
                return

            for i in range(start, len(candidates)):
                val = candidates[i]
                
                # Choose
                sol.append(val)
                
                # Recurse with 'i' (STAY on index 'i' to allow infinite element reuse)
                backtrack(i, current_sum + val)
                
                # Unchoose
                sol.pop()

        backtrack(0, 0)
        return res