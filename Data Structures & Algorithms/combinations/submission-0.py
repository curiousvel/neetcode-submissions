class Solution:
    """
    APPROACH: Decision Tree Backtracking (Fixed Depth Selection)

    MENTAL MODEL:
    We generate combinations of length 'k' from numbers 1 to 'n'.
    We prune branches early if there aren't enough remaining numbers left 
    in the range [start, n] to complete a full 'k'-length set.

    VISUAL WORKFLOW (n = 4, k = 2):
                          []
             /            |            \
        [1]              [2]           [3]
       / | \            /   \           |
    [1,2][1,3][1,4]   [2,3] [2,4]     [3,4]   <- Record only at depth k = 2

    COMPLEXITY:
    - Time:  O(k * C(n, k)) -> Binomial coefficient C(n, k) total combinations.
    - Space: O(k) auxiliary -> Recursion stack depth equals k.
    """
    def combine(self, n: int, k: int) -> List[List[int]]:
        res, sol = [], []

        def backtrack(start: int):
            # Base Case: Target size reached
            if len(sol) == k:
                res.append(sol.copy())
                return

            # --- PRUNING OPTIMIZATION ---
            # needed:    How many more numbers we still need to fill 'sol' up to size 'k'
            # available: How many total numbers are left to choose from in range [start, n]
            # 
            # Example: n=4, k=3. If sol=[1] (len 1, need 2 more) and start=4 (only [4] left, available=1),
            # 'available < needed' (1 < 2) is True -> Stop! We can't possibly reach length k.
            needed = k - len(sol)
            available = n - start + 1
            if available < needed:
                return

            for i in range(start, n + 1):
                sol.append(i)            # Choose
                backtrack(i + 1)         # Explore forward
                sol.pop()                # Unchoose

        backtrack(1)
        return res