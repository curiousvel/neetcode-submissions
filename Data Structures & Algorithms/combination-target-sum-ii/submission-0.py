"""
Problem: Combination Sum II (LeetCode 40)

High-Level Idea:
1. Sort `candidates` to bring duplicates adjacent to each other.
2. Loop-based Backtracking: Iterate through remaining elements starting at `start`.
3. No Reuse: Recurse with `i + 1` to move to the next distinct element.
4. Duplicate Pruning: `if i > start and candidates[i] == candidates[i - 1]: continue`
   - Skips processing identical numbers at the SAME tree level.
   - Allows picking identical numbers at DEEPER tree levels (e.g., `[1, 1]`).

Complexity:
- Time: O(2^N) — In the worst case, every element yields a binary pick/skip choice.
- Space: O(N) — Recursion call stack depth bounded by array length N.
"""

from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        sol = []

        def backtrack(start: int, total: int) -> None:
            # Base Case 1: Valid target reached
            if total == target:
                res.append(sol.copy())
                return

            # Base Case 2: Exceeded target (prune branch)
            if total > target:
                return

            for i in range(start, len(candidates)):
                # Duplicate Pruning: Skip duplicate values at the current loop level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # Choose
                sol.append(candidates[i])

                # Explore (Pass `i + 1` because element reuse is NOT allowed)
                backtrack(i + 1, total + candidates[i])

                # Unchoose (Backtrack)
                sol.pop()

        backtrack(0, 0)
        return res