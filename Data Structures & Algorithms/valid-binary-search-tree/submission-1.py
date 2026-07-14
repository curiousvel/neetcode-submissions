# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        ========================================================================
        MENTAL MODEL: The "Shrinking Window" Constraint
        ========================================================================
        Imagine each node in the tree is standing inside a valid range window: 
        (minimum, maximum). Initially, the root is in an infinite universe: (-∞, +∞).
        
        As we travel down the tree, the window of valid values shrinks:
        
          - When we go LEFT: The current node's value becomes the new UPPER ceiling.
            (The values must get smaller, so the 'maximum' shrinks).
            
          - When we go RIGHT: The current node's value becomes the new LOWER floor.
            (The values must get larger, so the 'minimum' shrinks).
            
        If any node's value falls outside its inherited window, the BST is invalid.
        ========================================================================
        """
        # We define a helper function to recursively validate the range limits.
        def isValid(node: Optional[TreeNode], minimum: float, maximum: float) -> bool:
            # An empty node/subtree is always a valid BST
            if not node:
                return True
            
            # The current node's value must stay strictly within the inherited (minimum, maximum) bounds
            if node.val <= minimum or node.val >= maximum:
                return False

            # Left child must be smaller than the current node's value (updates the maximum bound)
            # Right child must be larger than the current node's value (updates the minimum bound)
            return isValid(node.left, minimum, node.val) and isValid(node.right, node.val, maximum)

        # Kick off the recursion starting at the root with infinite bounds
        return isValid(root, float('-inf'), float('inf'))