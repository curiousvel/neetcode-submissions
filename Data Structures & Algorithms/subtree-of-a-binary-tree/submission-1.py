# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Problem: Subtree of Another Tree (LeetCode 572)
    
    ============================================================================
    MENTAL MODEL: The Blueprint Scanner 🔍
    ============================================================================
    - isSubtree: Walk through the mansion ('root') looking for any node that 
      could be the start of our cottage ('subRoot').
      
    - isSameTree: Place the cottage blueprint directly over the structure 
      to verify if every single room (left and right) is an identical match.
    ============================================================================
    """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # If the main tree (mansion) is empty, we can't find our subtree (cottage) anywhere
        if not root:
            return False
            
        # 1. Compare the blueprint at our current location
        if self.isSameTree(root, subRoot):
            return True
            
        # 2. If it doesn't match, walk left or right to keep looking
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # If both nodes are null, they are identical
        if not p and not q:
            return True
            
        # If only one of them is null, they cannot be identical
        if not p or not q:
            return False
            
        # If their values differ, they cannot be identical
        if p.val != q.val:
            return False
            
        # Both the left branch and the right branch must match perfectly
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)