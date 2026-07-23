from typing import List

class Solution:
    """
    APPROACH: Decision Tree Backtracking (Cascading Subset Generation)

    MENTAL MODEL:
    Construct the power set by making a binary choice for each element:
    include it in the current subset or move past it. Since every intermediate
    state is a valid subset, we append a snapshot of 'sol' at EVERY recursive call.

    VISUAL WORKFLOW (nums = [1, 2, 3]):

                            []
                  /         |         \
              [1]          [2]        [3]
             /   \          |
        [1, 2]  [1, 3]   [2, 3]
          |
      [1, 2, 3]

    All nodes in the tree above represent a valid unique subset in the result.

    COMPLEXITY:
    - Time:  O(N * 2^N) -> There are 2^N possible subsets (power set size), 
             and copying each subset takes O(N) time.
    - Space: O(N) auxiliary space -> Recursion stack depth is at most N, 
             and 'sol' array uses at most O(N) space (excluding output space).
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(start: int):
            # 1. RECORD: Every node in the decision tree is a valid subset!
            res.append(sol.copy())

            # 2. EXPLORE: Try adding every remaining candidate from 'start' onwards
            for i in range(start, len(nums)):
                # Choose
                sol.append(nums[i])

                # Explore (i + 1 enforces strict ordering, preventing duplicates)
                backtrack(i + 1)

                # Unchoose (Backtrack)
                sol.pop()

        backtrack(0)
        return res