class Solution:
    """
    APPROACH: Backtracking (Combinations at Fixed Depth)

    ===========================================================================
    🌳 CHEAT SHEET: COMBINATIONS AT FIXED DEPTH (PHONE NUMBER)
    ===========================================================================
    Input: digits = "23"
    Mapping: '2' -> "abc", '3' -> "def"

    Decision Tree:
                        "" (index 0: '2')
               /        |        \
             "a"       "b"       "c"   (index 1: '3')
            / | \     / | \     / | \
          "ad""ae""af" ...       ...   (index 2: Base Case -> Save)

    👉 State Management (Outer Scope Closure):
       - `res` (results) and `sol` (working path) live in outer function scope.
       - `backtrack(index)` only takes `index` (the changing state variable).
       - Modifying `sol` via .append()/.pop() mutates the outer list directly 
         without needing `nonlocal` (no variable reassignment).
    ===========================================================================

    MENTAL MODEL:
    - `index` tracks our current digit in `digits`.
    - At level `index`, try every available letter mapped to `digits[index]`.
    - Once `len(sol) == len(digits)`, snapshot `sol` into `res`!

    COMPLEXITY:
    - Time:  O(4^N * N) -> N is len(digits). Max 4 branches per digit, N to join string.
    - Space: O(N)       -> Stack depth bounded by N, single mutable `sol` list reused.
    """
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        phone_map = {
            '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
            '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
        }

        # Outer scope accumulators
        res = []
        sol = []

        def backtrack(index: int):
            # Base Case: We've picked a letter for every digit
            if index == len(digits):
                res.append("".join(sol))
                return

            # Explore choices for current digit
            current_digit = digits[index]
            possible_letters = phone_map[current_digit]

            for letter in possible_letters:
                # 1. Choose (mutate shared outer list)
                sol.append(letter)
                
                # 2. Explore
                backtrack(index + 1)
                
                # 3. Unchoose (revert shared outer list)
                sol.pop()

        # Kick off recursion starting at digit index 0
        backtrack(0)
        return res