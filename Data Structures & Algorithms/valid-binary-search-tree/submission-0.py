# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    🧠 MENTAL MODEL: Top-Down Boundary Constraints
    
    A valid BST requires EVERY node to honor the constraints of ALL its ancestors,
    not just its immediate parent. 
    
    Think of passing down an narrowing "allowable range" (min_val, max_val):
    - Going LEFT?  The current node becomes the new UPPER limit.
    - Going RIGHT? The current node becomes the new LOWER limit.
    
    Complexity:
        - Time: O(N) -> We visit every node exactly once.
        - Space: O(N) -> Worst-case call stack for a skewed tree (O(log N) if balanced).
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def helper(node: Optional[TreeNode], min_val: float, max_val: float) -> bool:
            # An empty tree is a valid BST
            if not node:
                return True

            # Check if the current node's value is within the allowed range
            if not (min_val < node.val < max_val):
                return False

            # Recursively check the left and right subtrees
            # For the left subtree, the node's value becomes the new max_val
            # For the right subtree, the node's value becomes the new min_val
            return helper(node.left, min_val, node.val) and \
                helper(node.right, node.val, max_val)

        # Start the validation with an infinitely wide range for the root
        return helper(root, float('-inf'), float('inf'))