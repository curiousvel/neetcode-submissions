from typing import List

class Solution:
    """
    APPROACH: Backtracking on 2D Grid (DFS with In-Place Visited Marking)

    ===========================================================================
    🌳 CHEAT SHEET: 2D GRID BACKTRACKING (WORD SEARCH)
    ===========================================================================
    Board:                        Decision Path for "ABCCED":
    [ ['A', 'B', 'C', 'E'],        (0,0) 'A' -> (0,1) 'B' -> (0,2) 'C'
      ['S', 'F', 'C', 'S'],                                     |
      ['A', 'D', 'E', 'E'] ]                                (1,2) 'C'
                                                                |
                                                            (2,2) 'E' -> (2,1) 'D'
    
    👉 Grid Mechanics:
       - 4 Directions: Unrolled explicitly using lazy short-circuiting `or`.
       - Visited Tracking: Temporarily mutate `board[r][c] = '#'` to prevent reusing 
         the same cell in a single path without extra space.
       - Early Exit: Returns `True` instantly up the stack once the word is found.
    ===========================================================================

    MENTAL MODEL:
    - We try starting the search from every cell `(r, c)` that matches `word[0]`.
    - At frame `(r, c, k)`, check if `board[r][c] == word[k]`.
    - Mark visited -> Explore 4 neighbors explicitly via `or` for `k + 1` -> Unchoose.

    COMPLEXITY:
    - Time:  O(M * N * 3^L) -> M*N grid cells. For each, branch up to 3 directions 
                               (excluding back-track) for string length L.
    - Space: O(L)          -> Call stack depth bounded by length of the word L.
    """
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])

        def backtrack(r: int, c: int, k: int) -> bool:
            # Base Case: Found all characters of the word
            if k == len(word):
                return True

            # Boundary check & character matching
            if (r < 0 or r >= ROWS or 
                c < 0 or c >= COLS or 
                board[r][c] != word[k]):
                return False

            # 1. Choose: Save original char & mark cell as visited
            temp = board[r][c]
            board[r][c] = '#'

            # 2. Explore: Try all 4 neighbors with lazy short-circuiting evaluation
            found = (backtrack(r, c + 1, k + 1) or  # Right
                     backtrack(r, c - 1, k + 1) or  # Left
                     backtrack(r + 1, c, k + 1) or  # Down
                     backtrack(r - 1, c, k + 1))    # Up

            # 3. Unchoose: Backtrack and restore original character
            board[r][c] = temp

            return found

        # Try starting from every cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True

        return False