# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    APPROACH: Divide & Conquer with Index Pointers + Hash Map

    ===========================================================================
    🌳 CHEAT SHEET: THE THREE TRAVERSAL PATTERNS
    ===========================================================================
    Consider the following Binary Tree:
                3
               / \
              9   20
                 /  \
                15   7

    1. PREORDER (Root -> Left -> Right):  [ 3 | 9 | 20, 15, 7 ]
       👉 Key Property: Root is ALWAYS the VERY FIRST element.

    2. INORDER  (Left -> Root -> Right):  [ 9 | 3 | 15, 20, 7 ]
       👉 Key Property: Splitting at Root gives Left & Right subtree windows.

    3. POSTORDER (Left -> Right -> Root): [ 9 | 15, 7, 20 | 3 ]
       👉 Key Property: Root is ALWAYS the VERY LAST element.
    ===========================================================================

    MENTAL MODEL (LEAP OF FAITH):
    Don't trace multi-level depth! Just focus on the local contract for ONE node:
    1. Preorder gives the Root (sequentially at preorder[pre_idx]).
    2. Inorder tells us where the split is (Left window vs. Right window).
    3. Recursively delegate left/right subtrees and let the call stack handle the rest.

    COMPLEXITY:
    - Time:  O(N) -> Hash Map lookup is O(1); each node created exactly once.
    - Space: O(N) -> Hash Map takes O(N); recursion stack takes O(H) where H is height.
    """
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Fast Index Directory: Hash map linking val -> index in 'inorder' for O(1) split lookups
        inorder_map = {val: idx for idx, val in enumerate(inorder)}
        
        # Sequentially tracks the current root candidate in preorder order (0, 1, 2...)
        pre_idx = 0

        def arrayToTree(in_start: int, in_end: int) -> Optional[TreeNode]:
            nonlocal pre_idx

            # Base Case: Invalid range in inorder -> no nodes left in this subtree branch
            if in_start > in_end:
                return None

            # 1. Grab current root value from preorder and advance pointer for the next call
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            pre_idx += 1

            # 2. Find split boundary in inorder array (O(1) time)
            in_split = inorder_map[root_val]

            # 3. Recursively build subtrees by passing updated inorder window boundaries
            #    - Left subtree range:  [in_start, in_split - 1]
            #    - Right subtree range: [in_split + 1, in_end]
            root.left = arrayToTree(in_start, in_split - 1)
            root.right = arrayToTree(in_split + 1, in_end)

            return root

        # Kick off recursion across the full inorder range
        return arrayToTree(0, len(inorder) - 1)