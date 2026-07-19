# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
    Problem: Lowest Common Ancestor of a Binary Search Tree (LeetCode 235)
    
    ============================================================================
    ALGORITHM: BST Split-Point Traversal 🌲
    ============================================================================
    We leverage the primary property of a Binary Search Tree (BST):
    - Left subtree values < Parent value
    - Right subtree values > Parent value
    
    Because the tree is sorted, we can find the Lowest Common Ancestor (LCA) by 
    tracing down from the root. The LCA is the exact "split point" where the two 
    target nodes (p and q) are no longer on the same side of the current node.
    
    ============================================================================
    COMPLEXITY ANALYSIS:
    ============================================================================
    - Time Complexity: O(H) -> Where H is the height of the tree. In the worst 
      case (a skewed line-like tree), we might visit all nodes from top to bottom. 
      For a balanced tree, the time complexity optimizes to O(log N).
      
    - Space Complexity: O(1) -> Because we are using an iterative 'while' loop 
      with a single pointer (curr) instead of recursion, we use constant extra memory.
    ============================================================================
    """
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Start our search pointer at the top of the tree
        curr = root

        while curr:
            # CASE 1: Both p and q have values greater than the current node.
            # This means both targets are located somewhere in the right subtree.
            if p.val > curr.val and q.val > curr.val:
                curr = curr.right
                
            # CASE 2: Both p and q have values less than the current node.
            # This means both targets are located somewhere in the left subtree.
            elif p.val < curr.val and q.val < curr.val:
                curr = curr.left
                
            # CASE 3: The Split Point!
            # One target is on the left, one is on the right (or the current node 
            # is equal to either p or q). This current node is the lowest common ancestor.
            else:
                return curr        
        