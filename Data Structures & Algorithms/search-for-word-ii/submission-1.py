# ==============================================================================
# Problem: 212. Word Search II
# Category: Tries / Backtracking
# 
# Mental Model: Trie = Map, Grid = Maze
# - Build a Trie from `words` to serve as a prefix map of valid search paths.
# - Perform DFS on the 2D grid, walking the board and the Trie simultaneously.
# - If a grid character is not in the current Trie node's children, PRUNE 
#   the search branch immediately.
# 
# Complexity:
# - Time Complexity: O(M * N * 4^L) where M x N is grid size and L is max word length.
#   (Trie prefix pruning exponentially reduces actual recursive operations).
# - Space Complexity: O(W * L) to build the Trie for W words of length L;
#   recursion call stack depth takes O(L).
# ==============================================================================

from typing import List

class TrieNode:
    """
    Trie Node structure holding child character maps and terminal words.
    Storing 'word' string at leaf nodes avoids manual string building during DFS.
    """
    def __init__(self):
        self.children = {}  # Maps char -> TrieNode
        self.word = None    # Holds full word string at terminal node


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # -------------------------------------------------------------
        # STEP 1: Build Trie from input words dictionary
        # -------------------------------------------------------------
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w  # Attach full word at leaf node

        ROWS, COLS = len(board), len(board[0])
        res = []

        # -------------------------------------------------------------
        # STEP 2: Backtracking DFS walking Grid & Trie simultaneously
        # -------------------------------------------------------------
        def backtrack(r: int, c: int, parent_node: TrieNode):
            char = board[r][c]
            curr_node = parent_node.children[char]

            # 1. Match Found! Append word and clear to prevent duplicate entries
            if curr_node.word:
                res.append(curr_node.word)
                curr_node.word = None

            # 2. Mark current cell visited
            board[r][c] = '#'

            # 3. Explore 4-directional neighbors
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                nr, nc = r + dr, c + dc
                # Check grid bounds & ensure neighbor char exists in Trie branch
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != '#': 
                    if board[nr][nc] in curr_node.children:
                        backtrack(nr, nc, curr_node)

            # 4. Unmark visited (backtrack state)
            board[r][c] = char

            # 5. Trie Pruning: Remove empty leaf nodes to speed up search
            if not curr_node.children:
                parent_node.children.pop(char)

        # -------------------------------------------------------------
        # STEP 3: Kick off DFS from every board cell matching Trie root
        # -------------------------------------------------------------
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] in root.children:
                    backtrack(r, c, root)

        return res