# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    APPROACH: Recursive Depth-First Search (DFS) Tree Inversion
    
    Mental Pattern:
    1. To invert a binary tree, swap the left and right children of every single node.
    2. Base Case: If the current node is None (empty subtree), return None to stop the recursion.
    3. Use a temporary variable to swap the current node's immediate left and right children.
    4. Recursively call the function on the left child and the right child to invert the rest of the subtrees.
    5. Return the root node after all downstream swaps are finalized.
    
    Complexity:
    - Time: O(n) where n is the number of nodes in the tree, since we must visit every node exactly once.
    - Space: O(h) where h is the height of the tree, representing the memory used by the recursive call stack (O(n) in worst-case skewed tree, O(log n) for a balanced tree).
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        temp = root.right
        root.right = root.left
        root.left = temp

        # Without Temp
        # Below line works because Python evaluates the entire right side of the
        # assignment before binding it to the variables on the left.
        # root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root