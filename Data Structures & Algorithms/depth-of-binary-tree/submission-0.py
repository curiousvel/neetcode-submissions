# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Base case: If the current node is None (empty tree or end of a branch),
        # its depth is 0. This is the stopping condition for the recursion.
        if not root:
            return 0

        # If current node is valid
        # Recursively calculate the maximum depth of the left subtree.
        # The depth of the left subtree is the number of nodes along the longest
        # path from the current node's left child down to the farthest leaf node.
        left_depth = self.maxDepth(root.left)

        # Recursively calculate the maximum depth of the right subtree.
        # Similarly, this is the depth of the longest path from the current
        # node's right child down to the farthest leaf node.
        right_depth = self.maxDepth(root.right)

        # The maximum depth of the tree rooted at 'root' is 1 (for the root itself)
        # plus the maximum of the depths of its left and right subtrees.
        # We take the maximum of the two subtree depths because we are looking for the *longest* path.
        return 1 + max(left_depth, right_depth)
        